from schematics.models import Model
from schematics.types import NumberType, StringType, URLType

class GetShiftsResponse(Model):
    roleId = NumberType(required=True)
    shiftDate = StringType(required=True)
    startTime = StringType(required=True)
    endTime = StringType(required=True)
    staff_required = NumberType(required=True)
    number_of_invited_staff = NumberType(required=True)
    jobType = StringType(required=True)
