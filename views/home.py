from flask import Blueprint, render_template

from utils.get_data import get_home_videos

bp = Blueprint('home', __name__, url_prefix='/')

### Routes ###
@bp.route('/', methods=['POST', 'GET'])
def view_index():
    return render_template('home.html',
        video_list=get_home_videos()
    )

