from wtforms import validators

from . constants import allowed_symbols

DataRequired = validators.DataRequired
Length = validators.Length
Optional = validators.Optional
URL = validators.URL
ValidationErr = validators.ValidationError


def len_validation(sequense, exception, min=1, max=1):
    """_summary_

    Args:
        sequense (_type_): _description_
        min (int, optional): _description_. Defaults to 1.
        max (int, optional): _description_. Defaults to 1.

    Returns:
        _type_: _description_
    """
    try:
        getattr(sequense, '__len__')
    except AttributeError:
        return False
    if min <= len(sequense) <= max:
        return
    raise exception


def symbols_validation(string, exception):
    if isinstance(string, str) and all((symbol in allowed_symbols) for symbol in string):
        return
    raise exception


class AllOf(validators.AnyOf):
    def __call__(self, form, field):
        if self.message is None:
            self.message = f'Some element of {field.data} not in {self.values}'
        symbols_validation(field.data, validators.ValidationError(self.message))
