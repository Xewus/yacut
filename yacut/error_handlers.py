from flask import jsonify, render_template

from . import app


class APIException(Exception):
    """Обработчик ошибок для эндпоинтов /api/* .
    """
    def __init__(self, message, status_code=400):
        super().__init__()
        self.message = message
        self.status_code = status_code

    def as_dict(self):
        """Формирует сообщение об ошибке в формате словаря.

        Returns:
            dict: Сообщение об ошибке.
        """
        return dict(message=self.message)

@app.errorhandler(APIException)
def api_exception(error):
    """Обрабатывает ошибки для api.

    Args:
        error (_type_): _description_

    Returns:
        tuple(dict, int): Сообщение об ошибке, HTTP-status
    """
    return jsonify(error.as_dict()), error.status_code


@app.errorhandler(404)
def page_not_found(error):
    """Обработчик ошибки 404.

    Args:
        error (exceptions.NotFound): Ошибка.

    Returns:
        str: html-страница.
    """
    print(type(error))
    return render_template('error_pages/404.html'), 404
