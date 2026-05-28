import enum


class LeadStatus(str, enum.Enum):
    new = "new"
    contacted = "contacted"
    booked = "booked"
    lost = "lost"
