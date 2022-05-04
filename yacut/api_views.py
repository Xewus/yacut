from flask import jsonify, request, url_for

from . import app, db, utils
from . models import URL_map
from . error_handlers import APIException
from . validators import len_validation, symbols_validation


@app.route('/api/id/', methods=['POST'])
def new_short_url():
    """запрос на создание новой короткой ссылки
    """
    data = request.get_json()
    if not data:
        raise APIException('Отсутствует тело запроса')
    if 'url' not in data:
        raise APIException('\"url\" является обязательным полем!')
    if 'custom_id' not in data or not data['custom_id']:
        custom_id = utils.get_unique_short_id()
        data['custom_id'] = custom_id

    custom_id = data['custom_id']
    if not len_validation(custom_id, max=6) or not symbols_validation(custom_id):
        raise APIException('Указано недопустимое имя для короткой ссылки')
    if URL_map.query.filter_by(short=data['custom_id']).first():
        raise APIException(f'Имя "{custom_id}" уже занято.')

    url_map = URL_map()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    short_link = url_map.short
    response_dict = dict(
        short_link=url_for(
            'mapper', short_url=short_link, _external=True
        ),
        url=url_map.original
    )
    return jsonify(response_dict), 201




@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_mapper_url(short_id):
    """получение оригинальной ссылки по короткому идентификатору.

    Args:
        short_id (_type_): _description_
    """
    url_map = URL_map.query.filter_by(short=short_id).first()
    if url_map is None:
        raise APIException('Указанный id не найден', 404)
    return dict(url=f'{url_map.original}'), 200