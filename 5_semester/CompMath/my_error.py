class MyError(Exception):
    """Base class for exceptions in this module."""
    pass


class SubZeroError(MyError):
    """Class for exceptions that are not greater than zero."""
    def __init__(self, *values):
        self.msg = "All of values " + str(values) + " must be greater than zero"

    def check(*values):
        """Checks if the value is greater than zero."""
        for value in values:
            if value <= 0:
                return 0
        return 1
