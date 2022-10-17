class Motor:
    name: str
    JointController: JointController
    target_position: float
    present_position: int

    def __init__(self, name: str, JointController: JointController) -> None:
        self.name = name
        self.JointController = JointController
        self.target_position = 0
        self.present_position = 0