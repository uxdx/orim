from flask import Blueprint, render_template

# from utils.get_data import 

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/')
def view_search_as_keyword(keyword:str):
    results = get_videos_by_search_as_keyword()
    return render_template('search.html')