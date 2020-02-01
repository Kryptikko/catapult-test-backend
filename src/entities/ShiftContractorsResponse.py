from schematics.models import Model
from schematics.types import StringType, URLType

class ShiftContractorsResponse(Model):
    contractors_name = StringType(required=True)
