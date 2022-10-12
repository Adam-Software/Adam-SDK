import InterpolationUtils
from InterpolationMethodsLegs import InterpolationMethodsLegs
from ParsingRangeArray import ParsingRangeArray


class InterpolationMethods:
    def __init__(self):
        self._positionRange = ParsingRangeArray()
        self._interpolationMethodsLegs = InterpolationMethodsLegs(self._positionRange)

    def CalcHead(self, GoalPosHeadPer, GoalPosNeckPer):
        headRange = self._positionRange.GetHeadRange
        CalcGoalPosHead = InterpolationUtils.CalcAngle(headRange.HeadRangeMax,
                                                       headRange.HeadRangeMin,
                                                       GoalPosHeadPer)
        CalcGoalPosNeck = InterpolationUtils.CalcAngle(headRange.NeckRangeMax,
                                                       headRange.HeadRangeMin,
                                                       GoalPosNeckPer)

        return CalcGoalPosHead, CalcGoalPosNeck

    def CalcArms(self, ArmShoulderAngleRightPer, ArmForearmAngleRightPer, ArmElbowTopAngleRightPer,
                 ArmElbowBottAngleRightPer, ArmElbowAngleRightPer, ArmShoulderAngleLeftPer,
                 ArmForearmAngleLeftPer, ArmElbowTopAngleLeftPer, ArmElbowBottAngleLeftPer,
                 ArmElbowAngleLeftPer, SwitchBothElbow):

        armRangeRight = self._positionRange.GetArmRangeRight
        armRangeLeft = self._positionRange.GetArmRangeLeft

        if not SwitchBothElbow:
            CalcGolPosShoulderRight = InterpolationUtils.CalcAngle(armRangeRight.ArmShoulderRightMax,
                                                                   armRangeRight.ArmShoulderRightMin,
                                                                   ArmShoulderAngleRightPer)
            CalcGolPosForearmRight = InterpolationUtils.CalcAngle(armRangeRight.ArmForearmRightMax,
                                                                  armRangeRight.ArmForearmRightMin,
                                                                  ArmForearmAngleRightPer)
            CalcGolPosElbowTopRight = InterpolationUtils.CalcAngle(armRangeRight.ArmElbowTopRightMax,
                                                                   armRangeRight.ArmElbowTopRightMin,
                                                                   ArmElbowTopAngleRightPer)
            CalcGolPosElbowBottRight = InterpolationUtils.CalcAngle(armRangeRight.ArmElbowBottRightMax,
                                                                    armRangeRight.ArmElbowBottRightMin,
                                                                    ArmElbowBottAngleRightPer)

            CalcGolPosShoulderLeft = InterpolationUtils.CalcAngle(armRangeLeft.ArmShoulderLeftMax,
                                                                  armRangeLeft.ArmShoulderLeftMin,
                                                                  ArmShoulderAngleLeftPer)
            CalcGolPosForearmLeft = InterpolationUtils.CalcAngle(armRangeLeft.ArmForearmLeftMax,
                                                                 armRangeLeft.ArmForearmLeftMin, ArmForearmAngleLeftPer)
            CalcGolPosElbowTopLeft = InterpolationUtils.CalcAngle(armRangeLeft.ArmElbowTopLeftMax,
                                                                  armRangeLeft.ArmElbowTopLeftMin,
                                                                  ArmElbowTopAngleLeftPer)
            CalcGolPosElbowBottLeft = InterpolationUtils.CalcAngle(armRangeLeft.ArmElbowBottLeftMax,
                                                                   armRangeLeft.ArmElbowBottLeftMin,
                                                                   ArmElbowBottAngleLeftPer)
        else:
            CalcGolPosShoulderRight = InterpolationUtils.CalcAngle(armRangeRight.ArmShoulderRightMax,
                                                                   armRangeRight.ArmShoulderRightMin,
                                                                   ArmShoulderAngleRightPer)
            CalcGolPosForearmRight = InterpolationUtils.CalcAngle(armRangeRight.ArmForearmRightMax,
                                                                  armRangeRight.ArmForearmRightMin,
                                                                  ArmForearmAngleRightPer)
            CalcGolPosElbowTopRight = InterpolationUtils.CalcAngle(armRangeRight.ArmElbowTopRightMax,
                                                                   armRangeRight.ArmElbowTopRightMin,
                                                                   ArmElbowAngleRightPer)
            CalcGolPosElbowBottRight = InterpolationUtils.CalcAngle(armRangeRight.ArmElbowBottRightMax,
                                                                    armRangeRight.ArmElbowBottRightMin,
                                                                    ArmElbowAngleRightPer)

            CalcGolPosShoulderLeft = InterpolationUtils.CalcAngle(armRangeLeft.ArmShoulderLeftMax,
                                                                  armRangeLeft.ArmShoulderLeftMin,
                                                                  ArmShoulderAngleLeftPer)
            CalcGolPosForearmLeft = InterpolationUtils.CalcAngle(armRangeLeft.ArmForearmLeftMax,
                                                                 armRangeLeft.ArmForearmLeftMin, ArmForearmAngleLeftPer)
            CalcGolPosElbowTopLeft = InterpolationUtils.CalcAngle(armRangeLeft.ArmElbowTopLeftMax,
                                                                  armRangeLeft.ArmElbowTopLeftMin, ArmElbowAngleLeftPer)
            CalcGolPosElbowBottLeft = InterpolationUtils.CalcAngle(armRangeLeft.ArmElbowBottLeftMax,
                                                                   armRangeLeft.ArmElbowBottLeftMin,
                                                                   ArmElbowAngleLeftPer)

        return (CalcGolPosShoulderRight, CalcGolPosForearmRight, CalcGolPosElbowTopRight, CalcGolPosElbowBottRight,
                CalcGolPosShoulderLeft, CalcGolPosForearmLeft, CalcGolPosElbowTopLeft, CalcGolPosElbowBottLeft)

    def CalcPress(self, PressTopAnglePer, PressBottAnglePer):
        pressRange = self._positionRange.GetPressRange
        CalcGoalPosPressTop = InterpolationUtils.CalcAngle(pressRange.PressTopAngleMax,
                                                           pressRange.PressTopAngleMin,
                                                           PressTopAnglePer)
        CalcGoalPosPressBott = InterpolationUtils.CalcAngle(pressRange.PressBottAngleMax,
                                                            pressRange.PressBottAngleMin,
                                                            PressBottAnglePer)

        return CalcGoalPosPressTop, CalcGoalPosPressBott

    def CalcBody(self, BodyRotPer):
        bodyRange = self._positionRange.GetBodyRange
        CalcGoalPosBody = InterpolationUtils.CalcAngle(bodyRange.BodyRotMax,
                                                       bodyRange.BodyRotMin,
                                                       BodyRotPer)

        return CalcGoalPosBody

    def CalcLeg(self, HighBothLegPer, HighLeftLegPer, HighRightLegPer, SwitchBothLeg):

        if SwitchBothLeg:
            right = self._interpolationMethodsLegs.CalcLegRightElbow(HighBothLegPer)
            left = self._interpolationMethodsLegs.CalcLegLeftElbow(HighBothLegPer)

            return right.__add__(left)

        right = self._interpolationMethodsLegs.CalcLegRight(HighRightLegPer)
        left = self._interpolationMethodsLegs.CalcLegLeft(HighLeftLegPer)

        return right.__add__(left)
