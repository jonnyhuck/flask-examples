# Minimal example use of `SQLite` with `Flask`

## `SQLite` Database Setup:
Before you can do anything with a database, you need to create one! To do this, you will need to install sqlite3 onto your machine (downloads [here](https://www.sqlite.org/download.html){:target="_blank"}), then run the following commands one at a time using the command line interface:

First, open the SQLite command line interface (specifying a location for the .db file for your database):
```bash
sqlite3 test.db
```

Next, add a table to the database (the .db file will not actually appear until this happens):
```sql
create table locations(lat double, lng double);
```

Finally, exit ther SQLite command line interface:
```
.exit
```

This will create a **database** file called `test.db`, which contains a **table** called `locations` with two **columns**: `lng` and `lat`.


## References
* This example largely based on the [Using SQLite3 with Flask tutorial](https://flask.palletsprojects.com/en/2.1.x/patterns/sqlite3/) in the Flask documentation.
* You can learn more about the command line interface for `SQLite` [here](https://www.sqlite.org/cli.html){:target="_blank"}. 
* A comprehensive guide the the 'flavour' of SQL that is understood by SQLite is available [here](https://www.sqlite.org/lang.html){:target="_blank"}.
* Some slightly easier-reading examples oif using SQLite with Python are given [here](https://www.sqlitetutorial.net/sqlite-python/insert/){:target="_blank"}