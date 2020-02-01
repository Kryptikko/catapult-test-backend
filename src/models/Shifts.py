from sqlalchemy import (
    Integer,
    Column,
    String,
    Table,
    ForeignKey)
from sqlalchemy.orm import relationship
from . import Base
from .ShiftInvitations import ShiftInvitations


# association_table = Table('shift_invitations', Base.metadata,
#     Column('shift_id', Integer, ForeignKey('shifts.role_id')),
#     Column('contractor_id', Integer, ForeignKey('contractors.id'))
# )

class Shift(Base):
    __tablename__ = 'shifts'

    role_id = Column(Integer, primary_key=True)
    staff_required = Column(Integer)
    # TODO: seprate unique table for job_types?
    job_type = Column(String)
    shift_date = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    contractors = relationship(
        "Contractor",
        back_populates="shifts",
        # lazy="dynamic"
        secondary=ShiftInvitations)

    def __repr__(self):
        return "<Shift(id='%s', job_type='%s')>" % (self.role_id, self.job_type)


# class Contractor(Base):
#     __tablename__ = 'contractors'
#     id = Column(Integer, primary_key=True)
#     candidate_name = Column(String)
#     shifts = relationship(
#         "Shift",
#         back_populates="contractors",
#         # lazy="dynamic"
#         secondary=association_table)
#
#     def __repr__(self):
#         return "<Contractor(name='%s', shifts='%s')>" % (self.candidate_name, len(self.shifts))
