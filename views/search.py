from flask import Blueprint, render_template, request
from utils.get_data import get_videos_by_search_as_keyword, get_videos_by_search_title


bp = Blueprint('search', __name__, url_prefix='/')



@bp.route('/search/')
def view_search_as_keyword():
    search_keyword = request.args.get('keyword')
    search = get_videos_by_search_title(search_keyword)    
    
    return render_template('search.html',
        search = search,
        search_keyword = search_keyword
    )
