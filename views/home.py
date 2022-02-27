from flask import Blueprint, render_template

from utils.get_data import get_index_videos
from settings import BASE_URL

bp = Blueprint('home', __name__, url_prefix='/')

video_list_Gaming,video_list_Music,video_list_Sports=get_index_videos()
### Routes ###
@bp.route('/', methods=['POST', 'GET'])
def view_index():
    return render_template('home.html',
        video_list_Gaming=video_list_Gaming,
        video_list_Music=video_list_Music,
        video_list_Sports=video_list_Sports,
        BASE_URL = BASE_URL
    )

