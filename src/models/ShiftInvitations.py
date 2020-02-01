from sqlalchemy import Column, Table, ForeignKey
from . import Base


ShiftInvitations = Table('shift_invitations', Base.metadata,
    Column('shift_id', Integer, ForeignKey('shifts.role_id')),
    Column('contractor_id', Integer, ForeignKey('contractors.id'))
)
