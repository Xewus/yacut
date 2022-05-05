from string import ascii_letters, digits

allowed_symbols = f'{ascii_letters}{digits}'

api_fields = {
    'original': 'url',
    'short': 'custom_id',
}

SHORT_URL_IS_BUSY = 'Имя %s уже занято!'
YOUR_URL_IS_READY = 'Ваша новая ссылка готова:'