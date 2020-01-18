class AdonaiClientException(Exception):
    def __init__(self, name: str, description: str = None):
        if description is not None:
            self.description = f": {description}"

        self.name = name

    def __str__(self) -> str:
        return f"{self.name}{self.description}"
