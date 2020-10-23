"""
Simple Flask web site 
"""
import flask  # The basic framework for http requests, storing cookies, etc
import logging  # For monitoring and debugging
from werkzeug.utils import secure_filename

import os
import tempfile

from skeleton import runner, runner2 ### import our project file
import pandas
UPLOAD_FOLDER = tempfile.gettempdir()
ALLOWED_EXTENSIONS = {'gpx'}

###
# Globals
###

import config  # Separate out per-machine configuration

app = flask.Flask(__name__)
app.secret_key = config.COOKIE_KEY
app.debug = config.DEBUG
app.logger.setLevel(logging.DEBUG)


#################
# Pages and request handling:
# We "route" URLs to functions by attaching
# the app.route 'decorator'.
#################

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('form.html')


@app.route("/display")
def display():
    flask.g.rants = read_rants()
    return flask.render_template('display.html')


#################
# Handle a file upload
#################

@app.route("/_upload", methods=['POST'])
def upload():
    app.logger.debug("Uploaded form")
    if 'file' not in flask.request.files:
        app.logger.debug("file not in request.files")
        flask.flash('No file part')
        return flask.redirect(flask.url_for("index"))
    file = flask.request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        app.logger.debug("file.filename is empty")
        flask.flash('No selected file')
        return flask.redirect(flask.url_for("index"))
    if not allowed_file(file.filename):
        app.logger.debug(f"Rejecting file name {file.filename}")
        flask.flash(f'File name "{file.filename}" not permitted')
        return flask.redirect(flask.url_for("index"))
    ## Passed all checks
    app.logger.debug("Looks like there is a valid file name")
    filename = secure_filename(file.filename)
    full_path = os.path.join(UPLOAD_FOLDER, filename)
    app.logger.debug(f"Saving the file to {full_path}")
    file.save(full_path)

    APIkey = flask.request.form['text']
    

    ApiType= flask.request.form.get('APIs')
    if (str(ApiType) == 'GoogleAPI'):
        cue_sheet = do_something2(full_path, APIkey)
    else:
        cue_sheet = do_something(full_path, APIkey)

    
    # flask.g.mystuff = cue_sheet.to_html()
    flask.g.result = cue_sheet.to_html()
    # flask.g.result = cue_sheet
    app.logger.debug("Rendering result")
    return flask.render_template("display.html")


def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def do_something(full_path: str, APIkey: str) -> str:
    """This is where I would call a function
    that reads the uploaded file and returns something
    """
    cue_sheet = runner(full_path, APIkey)
    return cue_sheet

def do_something2(full_path: str, APIkey: str) -> str:
    """This is where I would call a function
    that reads the uploaded file and returns something
    """
    cue_sheet = runner2(full_path, APIkey)
    return cue_sheet

###################
#   Error handlers
#   These are pages we display when something goes wrong
###################
@app.errorhandler(404)
def error_404(e):
    app.logger.warning("++ 404 error: {}".format(e))
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    app.logger.warning("++ 500 error: {}".format(e))
    assert app.debug == False  ## Crash me please, so I can debug!
    return flask.render_template('500.html'), 500


@app.errorhandler(403)
def error_403(e):
    app.logger.warning("++ 403 error: {}".format(e))
    return flask.render_template('403.html'), 403


#############
# Filters
# These process some text before inserting into a page
#############
@app.template_filter('humanize')
def humanize(date):
    """Humanize an ISO date string"""
    as_arrow = arrow.get(date)
    return as_arrow.humanize()


# Set up to run from cgi-bin script, from
# gunicorn, or stand-alone.
#
if __name__ == "__main__":
    # Running standalone
    print("Opening for global access on port {}".format(config.PORT))
    app.run(port=config.PORT, host="0.0.0.0")

# We could also be running from the gunicorn WSGI server,
# which makes the call to app.run.  Gunicorn may invoke more than
# one instance for concurrent service, so make sure the application
# is thread safe!
