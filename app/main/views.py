from flask import render_template
from . import main

# Views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)
    