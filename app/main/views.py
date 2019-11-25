from flask import render_template
from . import main
from flask_login import login_required


# Views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    title = 'Home - welcome to world of Pitches'
    return render_template('index.html',title = title)

@main.route('/pitch/<int:pitch_id>',methods =['GET','POST'])
@login_required
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)
    