from Servo import Servo


class JsonDeserialize:

    @staticmethod
    def commands(jsonCommands):

        try:
            servos = []
            for servoJson in jsonCommands['motors']:
                servos.append(Servo(servoJson['name'], servoJson['goal_position']))

            return servos

        except AttributeError:
            pass



