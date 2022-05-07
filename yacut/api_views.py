"""Обработка запросов к api-интерфейсу.
"""

from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app
from . import constants as const
from . import utils
from .error_handlers import APIException
from .models import UrlMap
from .validators import len_validation, symbols_validation


@app.route('/api/id/', methods=['POST'])
def new_short_url():
    """Обработка запроса на создание новой короткой ссылки.

    Raises:
        APIException: При получении некорректных данных.

    Returns:
        Responce: json.
    """
    original = const.API_REQUEST_FIELDS.original
    short = const.API_REQUEST_FIELDS.short
    data = request.get_json()

    if not data:
        raise APIException(const.NO_REQUEST_BODY)

    if data.get(original) is None:
        raise APIException(const.NO_REQUIRED_FIELD % original)

    original = data.get(original)
    short = data.get(short)

    if short:
        len_validation(short, APIException(const.API_EXC_MESSAGE), max=const.MAX_LEN_SHORT)
        symbols_validation(short, APIException(const.API_EXC_MESSAGE))
        if utils.short_url_exist(short):
            raise APIException(const.SHORT_URL_IS_BUSY % short)
    else:
        short = utils.get_unique_short_id()

    utils.add_url_map(original, short)

    response_dict = {
        const.API_RESPONSE_FIELDS.short: url_for(
            'mapper', short_url=short, _external=True
        ),
        const.API_RESPONSE_FIELDS.original: original
    }
    return jsonify(response_dict), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_mapper_url(short_id):
    """получение оригинальной ссылки по короткому идентификатору.

    Args:
        short_id (str): Короткое имя ссылки.

    Raises:
        APIException: Ссылка не найдена.

    Returns:
        tuple(str, int): Оригинальная ссылка, статус-код.
    """
    url_map = UrlMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise APIException(const.NOT_FOUND, HTTPStatus.NOT_FOUND)

    response_dict = {
        const.API_RESPONSE_FIELDS.original: url_map.original
    }
    return response_dict, HTTPStatus.OK
