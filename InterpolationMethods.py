import InterpolationUtils
from InterpolationMethodsLegs import InterpolationMethodsLegs
from InterpolationMethodsArms import InterpolationMethodsArms
from ParsingRangeArray import ParsingRangeArray


class InterpolationMethods:
    def __init__(self):
        self._positionRange = ParsingRangeArray()
        self._interpolationMethodsLegs = InterpolationMethodsLegs(self._positionRange)
        self._interpolationMethodsArms = InterpolationMethodsArms(self._positionRange)

    #
    # Head calculation
    #
    def CalcHead(self, GoalPosHeadPer):
        headRange = self._positionRange.GetHeadRange
        CalcGoalPosHead = InterpolationUtils.CalcAngle(headRange.HeadRangeMax,
                                                       headRange.HeadRangeMin,
                                                       GoalPosHeadPer)

        return CalcGoalPosHead

    #
    # Head calculation
    #
    def CalcNeck(self, GoalPosNeckPer):
        headRange = self._positionRange.GetHeadRange
        CalcGoalPosNeck = InterpolationUtils.CalcAngle(headRange.NeckRangeMax,
                                                       headRange.HeadRangeMin,
                                                       GoalPosNeckPer)

        return CalcGoalPosNeck

    #
    # Arms calculation
    #
    def CalcArms(self,
                 ArmShoulderAngleRightPer, ArmForearmAngleRightPer,
                 ArmElbowTopAngleRightPer, ArmElbowBottAngleRightPer, ArmElbowAngleRightPer,
                 ArmShoulderAngleLeftPer, ArmForearmAngleLeftPer,
                 ArmElbowTopAngleLeftPer, ArmElbowBottAngleLeftPer, ArmElbowAngleLeftPer,
                 SwitchBothElbow):

        if SwitchBothElbow:
            right = self._interpolationMethodsArms.CalcArmRightElbow(ArmShoulderAngleRightPer,
                                                                     ArmForearmAngleRightPer,
                                                                     ArmElbowAngleRightPer)
            left = self._interpolationMethodsArms.CalcArmLeftElbow(ArmShoulderAngleLeftPer,
                                                                   ArmForearmAngleLeftPer,
                                                                   ArmElbowAngleLeftPer)

            return right.__add__(left)

        right = self._interpolationMethodsArms.CalcArmRight(ArmShoulderAngleRightPer,
                                                            ArmForearmAngleRightPer,
                                                            ArmElbowTopAngleRightPer,
                                                            ArmElbowBottAngleRightPer)
        left = self._interpolationMethodsArms.CalcArmLeft(ArmShoulderAngleLeftPer,
                                                          ArmForearmAngleLeftPer,
                                                          ArmElbowTopAngleLeftPer,
                                                          ArmElbowBottAngleLeftPer)

        return right.__add__(left)

    def CalcArmRight(self, ArmShoulderAngleRightPer, ArmForearmAngleRightPer,
                     ArmElbowTopAngleRightPer, ArmElbowBottAngleRightPer):
        return self._interpolationMethodsArms.CalcArmRight(ArmShoulderAngleRightPer, ArmForearmAngleRightPer,
                                                           ArmElbowTopAngleRightPer, ArmElbowBottAngleRightPer)

    def CalcArmRightElbow(self, ArmShoulderAngleRightPer, ArmForearmAngleRightPer, ArmElbowAngleRightPer):
        return self._interpolationMethodsArms.CalcArmRightElbow(ArmShoulderAngleRightPer, ArmForearmAngleRightPer,
                                                                ArmElbowAngleRightPer)

    def CalcArmLeft(self, ArmShoulderAngleLeftPer, ArmForearmAngleLeftPer,
                    ArmElbowAngleLeftPer, ArmElbowBottAngleRightPer):
        return self._interpolationMethodsArms.CalcArmLeft(ArmShoulderAngleLeftPer, ArmForearmAngleLeftPer,
                                                          ArmElbowAngleLeftPer, ArmElbowBottAngleRightPer)

    def CalcArmLeftElbow(self, ArmShoulderAngleLeftPer, ArmForearmAngleLeftPer, ArmElbowAngleLeftPer):
        return self._interpolationMethodsArms.CalcArmLeftElbow(ArmShoulderAngleLeftPer, ArmForearmAngleLeftPer,
                                                               ArmElbowAngleLeftPer)

    #
    # Press calculation
    #
    def CalcPress(self, PressTopAnglePer, PressBottAnglePer):
        pressRange = self._positionRange.GetPressRange
        CalcGoalPosPressTop = InterpolationUtils.CalcAngle(pressRange.PressTopAngleMax,
                                                           pressRange.PressTopAngleMin,
                                                           PressTopAnglePer)
        CalcGoalPosPressBott = InterpolationUtils.CalcAngle(pressRange.PressBottAngleMax,
                                                            pressRange.PressBottAngleMin,
                                                            PressBottAnglePer)

        return CalcGoalPosPressTop, CalcGoalPosPressBott

    #
    # Body calculation
    #
    def CalcBody(self, BodyRotPer):
        bodyRange = self._positionRange.GetBodyRange
        CalcGoalPosBody = InterpolationUtils.CalcAngle(bodyRange.BodyRotMax,
                                                       bodyRange.BodyRotMin,
                                                       BodyRotPer)

        return CalcGoalPosBody

    #
    # Leg calculation
    #
    def CalcLeg(self, HighBothLegPer, HighLeftLegPer, HighRightLegPer, SwitchBothLeg):

        if SwitchBothLeg:
            right = self._interpolationMethodsLegs.CalcLegRightElbow(HighBothLegPer)
            left = self._interpolationMethodsLegs.CalcLegLeftElbow(HighBothLegPer)

            return right.__add__(left)

        right = self._interpolationMethodsLegs.CalcLegRight(HighRightLegPer)
        left = self._interpolationMethodsLegs.CalcLegLeft(HighLeftLegPer)

        return right.__add__(left)
