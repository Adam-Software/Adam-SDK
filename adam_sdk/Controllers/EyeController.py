from robot_eye_display import RobotEyeDisplay

class EyeController:
    def __init__(self):
        self.robot_eye_display = RobotEyeDisplay()

    def display_eyes(self, gif_paths_R, gif_paths_L):
            self.robot_eye_display.run(gif_paths_R, gif_paths_L)
