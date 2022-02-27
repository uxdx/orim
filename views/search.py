from flask import Blueprint, render_template, request
from utils.get_data import get_videos_by_search_as_keyword, get_videos_by_search_title,get_videos_by_search_channel_name


bp = Blueprint('search', __name__, url_prefix='/')



@bp.route('/search/')
def view_search_as_keyword():
    search_option = request.args.get('option')
    search_keyword = request.args.get('keyword')
    if search_option == '제목':
        search_video = get_videos_by_search_title(search_keyword)
    else:
        search_video = get_videos_by_search_channel_name(search_keyword)    
    
    return render_template('search.html',
        search_video = search_video

    )
