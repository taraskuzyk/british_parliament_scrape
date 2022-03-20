import enum


class Status(enum.Enum):
    open = "open"
    closed = "closed"
    rejected = "rejected"
    not_available = "not_available"