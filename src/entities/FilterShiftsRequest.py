import re
from schematics.models import Model
from schematics.types import NumberType, StringType
from schematics.exceptions import ValidationError


# def validate_time_foramt(value):
#     if not re.match("^[0-9]{2}:[0-9]{2}$", value):
#         raise ValidationError("Value must be valid time format (ex. 12:00)")
#     return value


class FilterShiftsRequest(Model):
    # startTime = StringType(required=False, validators=[validate_time_foramt])
    startTime = StringType(required=False, choices=["AM", "PM"])
    jobType = StringType(required=False)
