from flask import Blueprint, render_template, request

from utils.get_data import get_video_by_vid

bp = Blueprint('detail', __name__, url_prefix='/')

@bp.route('/video/')
def view_video_detail():
    """/video?vid=[VID]
    [VID]값에 따라 다른 영상의 페이지가 표시됨.
    """
    video_id = request.args.get('vid')

    video = get_video_by_vid()
    return render_template(
        video=video
    )