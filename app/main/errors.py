from flask import render_template
from . import main

@main.app_errorhandeler(404)
def fourOwfour(error):
    '''
    Render the 404 error page
    '''
    return render_template('fourOwfour.html'),404