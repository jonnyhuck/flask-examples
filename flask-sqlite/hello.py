import sqlite3
from json import dumps
from werkzeug.exceptions import BadRequestKeyError
from flask import Flask, render_template, request, g

app = Flask(__name__)

# set the path tpo the database
DATABASE = './test.db'

def get_db():
    '''
    * This is a helper function to get the current database connection
    '''
    # see if the database connnection exists
    db = getattr(g, '_database', None)
    
    # if not, connect
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    # set it to return data as `Row` objects
    db.row_factory = sqlite3.Row

    # return the database connection
    return db

@app.teardown_appcontext
def close_connection(exception):
    '''
    * This is a helper function to close the current database connection
    '''
    # see if a database connection exists
    db = getattr(g, '_database', None)
    
    # if so, close it
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    '''
    * This is a helper function to query the current database connection
    '''
    # open a database cursor and execute the query
    cur = get_db().execute(query, args)
    
    # fetch all results
    rv = cur.fetchall()
    
    # close the cursor
    cur.close()

    # return the results
    return (rv[0] if rv else None) if one else rv


def insert_db(query, args=()):
    '''
    * This is a helper function to query the current database connection
    '''
    # get ref to the database
    db = get_db()
    
    # open a database cursor and execute the query
    cur = db.execute(query, args)
    
    # commit the changes
    db.commit()
    
    # close the cursor
    cur.close()

    # return the results
    return cur.lastrowid


@app.route("/selectall")
def select_all():
    """
    * This is the web service that returns all entries in the database
    *
    * An example call to this service would be:
    *   http://127.0.0.1:5000/selectall
    """
    
    # output all of the rows in the database to dictionary
    output = []
    for row in query_db('select * from locations'):
        output.append({'lng': row['lng'], 'lat': row['lat']})
        print(output)
    
    # dump to JSON and return
    return dumps(output)


@app.route("/select")
def select_one():
    """
    * This is the web service that returns a single entry that matches a certain criteria
    *
    * An example call to this service would be:
    *   http://127.0.0.1:5000/select?lng=-2.807007&lat=54.065836
    """
    # only works if both lng and lat have been passed and can be converted to floats
    try:
        # this is how you get the coords that were passed in
        lng = float(request.args['lng'])
        lat = float(request.args['lat'])
    except (BadRequestKeyError, ValueError):
        return dumps({'success': False})

    # query the database for a single row
    row = query_db('select * from locations where lat = ? and lng = ?', [lat, lng], one=True)

    # dump to JSON and return
    return dumps({'lng':row['lng'], 'lat':row['lat']})


@app.route("/insert")
def insert():
    """
    * This is the web service that inserts new data into the database
    *
    * An example call to this service would be:
    *   http://127.0.0.1:5000/select?lng=-2.807007&lat=54.065836
    """
    # only works if both lng and lat have been passed and can be converted to floats
    try:
        # this is how you get the coords that were passed in
        lng = float(request.args['lng'])
        lat = float(request.args['lat'])
    except (BadRequestKeyError, ValueError):
        return dumps({'success': False})

    # insert the data into the database
    rowid = insert_db('insert into locations values (?, ?)',[lat, lng])

    # respond the user (encoded as JSON)
    if rowid is None:
        return dumps({'success': False})
    else:
        return dumps({'success': True, 'rowid': rowid})


@app.route("/")
@app.route("/map")
def map():
    """
    * This is the web page that gets the route data
    """
    return render_template('./map.html')