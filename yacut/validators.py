from xml.dom import ValidationErr
from wtforms import validators

DataRequired = validators.DataRequired
Length = validators.Length
Optional = validators.Optional
URL = validators.URL
ValidationErr = validators.ValidationError


class AllOf(validators.AnyOf):
    def __call__(self, form, field):
        if all((symbol in self.values) for symbol in field.data):
            return

        raise ValidationErr(f'{field.data} not in {self.values}')