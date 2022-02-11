from flask import Blueprint, render_template, request, session

from views.authentication import login_is_required

bp = Blueprint('profile', __name__, url_prefix='/')

@login_is_required
@bp.route('/my-profile/')
def view_my_profile():
    """각자의 session에 따라 결과가 달라짐
    """
    name = session['name']

    return render_template(
        'my_profile.html'
    )