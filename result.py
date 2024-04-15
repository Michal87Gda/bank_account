class Result:
    def __init__(self, message, value=None):
        self.is_succed = None
        self.message = message
        self.value = value

    def is_ok(self):
        return self.is_succed

class Error(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.is_succed = False


class Success(Result):
    def __init__(self, message, value=None):
        super().__init__(message, value)
        self.is_succed = True

