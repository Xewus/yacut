from string import ascii_letters, digits

ALLOWED_SYMBOLS = f'{ascii_letters}{digits}'

API_REQUEST_FIELDS = {
    'original': 'url',
    'short': 'custom_id'
}

API_RESPONSE_FIELDS = {
    'original': 'url',
    'short': 'short_link'
}

MAX_LEN_SHORT = 16
LEN_AUTO_SHORT = 6

# used in .views
SHORT_URL_IS_BUSY = 'Имя %s%s%s уже занято%s'
YOUR_URL_IS_READY = 'Ваша новая ссылка готова:'
BD_ERROR = 'Не удалось создать ссылку'

# used in .api_views
NO_REQUEST_BODY = 'Отсутствует тело запроса'
NO_REQUIRED_FIELD = '\"%s\" является обязательным полем!'
API_EXC_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
NOT_FOUND = 'Указанный id не найден'
