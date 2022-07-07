# Minimal Flask Examples

This repository contains a set of examples for how to use a Flask Python Server, intended to provide simple illustrations of how to integrate flask with other technologies for my students.

Each directory is a separate Flask Server instance, and should be run using the following command:

## Running Flask
Inside each directory, you can run Flask by typing the following commands into the terminal / command line:

Mac / Linux etc:
```bash
export FLASK_APP=hello
export FLASK_ENV=development
flask run
```
(or, in a single line...)
```bash
export FLASK_APP=hello && export FLASK_ENV=development && flask run
```

Windows:
```cmd
set FLASK_APP=hello
set FLASK_ENV=development
flask run
```

In all cases, if it has worked, you should get the following response:
```txt
 * Serving Flask app 'hello' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

Once this happens, you should be able to find your server by typing [http://127.0.0.1:5000](http://127.0.0.1:5000) into your web browser (or clicking the link).

In each example directory, the server code is in `hello.py` and the HTML (web page) is stored in `templates`.

More information on the basics of running Flask can be found in the Flask documentation [here](https://flask.palletsprojects.com/en/2.1.x/quickstart/).
