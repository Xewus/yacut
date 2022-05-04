from flask import jsonify, render_template

from . import app, db


class APIException(Exception):
    def __init__(self, message, status_code=400):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def as_dict(self):
        return dict(message=self.message)

@app.errorhandler(APIException)
def api_exception(error):
    return jsonify(error.as_dict()), error.status_code


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_pages/404.html'), 404
