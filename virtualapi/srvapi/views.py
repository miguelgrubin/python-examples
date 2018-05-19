import sys

import arrow
from flask import Blueprint
from flask import jsonify

base_web = Blueprint('base_web', __name__)


@base_web.route('/', methods=['GET'])
def index():
    response = {
        'status': True,
        'now': arrow.now().isoformat(),
        'venv': False
    }
    if is_venv():
        response['venv'] = True
    return jsonify(response)


def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))
