from wtforms import validators

from . constants import allowed_symbols

DataRequired = validators.DataRequired
Length = validators.Length
Optional = validators.Optional
URL = validators.URL
ValidationErr = validators.ValidationError


def len_validation(sequense, min=1, max=1):
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
    return min <= len(sequense) <= max


def symbols_validation(string):
    if not isinstance(string, str):
        return False
    return all((symbol in allowed_symbols) for symbol in string)


class AllOf(validators.AnyOf):
    def __call__(self, form, field):
        if symbols_validation(field.data):
            return

        if self.message is None:
            self.message = f'Some element of {field.data} not in {self.values}'

        raise validators.ValidationError(self.message)
