class NotInitializedError(Exception):
    """An Exception raised when the embed is not initialized/called."""

    def __init__(self):
        self.message = "the embed has not been initialized."


class AlreadyInitializedError(Exception):
    """An Exception raised when init then call with kwargs."""

    def __init__(self):
        self.message = "an embed already initialized was called."


class MissingContextError(Exception):
    """An exception raised when calling embed without a context."""

    def __init__(self):
        self.message = "ctx is a required argument you didn't passed."
