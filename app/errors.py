class FileExtNotAllowed(Exception):
    """File extension is not allowed"""

    def __init__(self, extension):
        self.txt = f"file extension \"{extension}\" is not allowed "
