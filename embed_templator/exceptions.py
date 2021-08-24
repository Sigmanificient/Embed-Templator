class NotInitializedError(Exception):

    def __init__(self):
        self.message = "the embed has not been initialized."


class AlreadyInitializedError(Exception):

    def __init__(self):
        self.message = "an embed already initialized was called."


class MissingContextError(Exception):

    def __init__(self):
        self.message = "ctx is a required argument you didn't passed."
