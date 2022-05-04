import re
from flask import jsonify, request

from flask import jsonify, request

from . import app, db, error_handlers, models, validators, utils

APIException = error_handlers.APIException


@app.route('/api/id/', methods=['POST'])
def new_short_url():
    """запрос на создание новой короткой ссылки
    """
    data = request.get_json()
    if not data or 'url' not in data:
        raise APIException('Отсутствует тело запроса')
    if 'custom_id' not in data:
        custom_id = utils.get_unique_short_id()
        data['custom_id'] = custom_id

    custom_id = data['custom_id']
    if len(custom_id) > 16:
        raise APIException('Указано недопустимое имя для короткой ссылки')
    if models.URL_map.query.filter_by(short=data['custom_id']).first():
        raise APIException('Такое уже имя занято')

    url_map = models.URL_map()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.as_dict()), 201




@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_mapper_url(short_id):
    """получение оригинальной ссылки по короткому идентификатору.

    Args:
        short_id (_type_): _description_
    """
    url_map = models.URL_map.query.filter_by(short=short_id).first()
    if url_map is None:
        raise APIException('Указанный id не найден', 404)
    return dict(url=f'{url_map.original}'), 200