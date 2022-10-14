class Joint:
    lover_limit: int
    upper_limit: int
    speed: int

    def __init__(self, lover_limit: int, upper_limit: int, speed: int) -> None:
        self.lover_limit = lover_limit
        self.upper_limit = upper_limit
        self.speed = speed