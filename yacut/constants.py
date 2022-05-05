from string import ascii_letters, digits

allowed_symbols = f'{ascii_letters}{digits}'

api_fields = {
    'original': 'url',
    'short': 'custom_id',
}
# used in .views
SHORT_URL_IS_BUSY = 'Имя %s%s%s уже занято%s'  # В тестах использованы разные знаки препинания @_@
YOUR_URL_IS_READY = 'Ваша новая ссылка готова:'
BD_ERROR = 'Не удалось создать ссылку'

# used in .api_views
NO_REQUEST_BODY = 'Отсутствует тело запроса'
NO_REQUIRED_FIELD = '\"%s\" является обязательным полем!'
API_EXC_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
NOT_FOUND = 'Указанный id не найден'
