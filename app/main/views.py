from flask import render_template, redirect, url_for, abort, request
from . import main
from ..models import Pitch, Comment, User
from .forms import PitchForm, UpdateProfile, CommentForm
from flask_login import login_required, current_user
from .. import db, photos



#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its content
    '''
    title = "mimi, picth yourself!"
    return render_template('index.html', title = title)


@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):
    '''
    View pitch function that returns the pitch details page and its data
    '''
    title = f'Pitch {pitch_id}'
    return render_template('pitch.html', id = pitch_id)

@main.route('/create',methods = ['GET', 'POST'])
@login_required
def create_pitch():
    '''
    Function that will create a pitch
    '''
    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        pitch = Pitch(pitch = pitch_form.pitch.data, pitch_category = pitch_form.pitch_category.data)
        db.session.add(pitch)
        db.session.commit()

        return redirect(url_for('main.show_pitch'))

    return render_template('new_pitch.html', pitch_form = pitch_form)

@main.route('/pitch')
def show_pitch():
    '''Function that will display all pitches
    '''
    interview_pitches = Pitch.query.filter_by(pitch_category = 'Interview').all()
    promotion_pitches = Pitch.query.filter_by(pitch_category = 'promotion').all()
    pickup_lines = Pitch.query.filter_by(pitch_category = 'Pickup Lines').all()
    comedic_quips = Pitch.query.filter_by(pitch_category = 'Comedy').all()
    pitches = Pitch.query.all()
    print(pitches)

    title = 'mimi, all pitches'
    return render_template('pitch.html', pitches = pitches, title = title, interview_pitches = interview_pitches, promotion_pitches = promotion_pitches, pickup_lines = pickup_lines, comedic_quips = comedic_quips)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname = uname))


@main.route('/comment/<pitch_id>', methods = ['GET', 'POST'])
@login_required
def comment(pitch_id):
    '''
    Will create a comment for an individual pitch
    '''
    pitches = Pitch.query.all()
    comment_form = CommentForm()
    comments = Comment.query.all()
    if comment_form.validate_on_submit():
        comment = Comment(comment = comment_form.comment.data, pitch_id = pitch_id,  user_id = current_user.id)
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('main.comment', pitch_id = pitch_id))
    return render_template('comment.html', comment_form = comment_form, comments = comments, pitches = pitches, pitch_id = pitch_id)

    

