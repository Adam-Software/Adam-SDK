class MotorCommand:
    name: str
    goal_position: float
    def __init__(self, name: str,goal_position:float) -> None:
        self.name = name
        self.goal_position = goal_position