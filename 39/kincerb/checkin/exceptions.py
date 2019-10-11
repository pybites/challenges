class CheckinError(Exception):
    """Base exception for checkin package"""
    pass


class DatabaseError(CheckinError):
    """Exception for Database errors"""
    pass
