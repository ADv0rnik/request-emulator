class BookshelfBaseException(Exception):
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f"Base exception with {self.args}"


class WrongBookException(BookshelfBaseException):
    def __str__(self):
        return f"Book with id={self.args} doesn't exist"


class OrderException(BookshelfBaseException):
    def __str__(self):
        return f"An error occurred during creating order {Exception}"


class RoleException(BookshelfBaseException):
    def __str__(self):
        return f"An error occurred during creating role {Exception}"
