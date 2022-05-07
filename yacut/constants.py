"""Постоянные значения и литералы для приложения.
"""
from collections import namedtuple
from string import ascii_letters, digits

ALLOWED_SYMBOLS = f'{ascii_letters}{digits}'

# Кортеж с именами полей к в модели UrlMap
URL_MAP_FIELDS = namedtuple('Fields', 'id original short timestamp')

# Кортеж, связывающий поля API-запроса с полями модели UrlMap
API_REQUEST_FIELDS = URL_MAP_FIELDS(None, 'url', 'custom_id', None)

# Кортеж, свзывающий поля API-ответа с полями модели UrlMap
API_RESPONSE_FIELDS = URL_MAP_FIELDS(None, 'url', 'short_link', None)

MAX_LEN_SHORT = 16
LEN_AUTO_SHORT = 6

# used in .views
SHORT_URL_IS_BUSY = 'Имя %s уже занято!'
YOUR_URL_IS_READY = 'Ваша новая ссылка готова:'
BD_ERROR = 'Не удалось создать ссылку'

# used in .api_views
NO_REQUEST_BODY = 'Отсутствует тело запроса'
NO_REQUIRED_FIELD = '\"%s\" является обязательным полем!'
API_EXC_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
NOT_FOUND = 'Указанный id не найден'
