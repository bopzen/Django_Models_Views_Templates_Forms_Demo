from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_symbols(value):
    if '_' in value:
        raise ValidationError("'_' symbols are not allowed!")


@deconstructible
class ValueInRangeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < 1 or value > 10:
            raise ValidationError(f"Priority must be in the range {self.min_value}-{self.max_value}")

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.min_value == other.min_value
            and self.max_value == other.max_value
        )