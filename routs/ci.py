from flask import Blueprint, render_template

from flask import Blueprint, render_template

ci_bp = Blueprint('ci', __name__)


@ci_bp.route('/CI')
def index():
    return render_template('CI.html')



