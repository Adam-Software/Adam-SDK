from ParsingRangeArray import ParsingRangeArray


def _CalcAngle(angleMax, angleMin, anglePer):
    position = ((angleMax - angleMin) * anglePer) + angleMin
    return position


class InterpolationMethods:
    def __init__(self):
        self._positionRange = ParsingRangeArray()

    def CalcHead(self, GoalPosHeadPer, GoalPosNeckPer):
        headRange = self._positionRange.GetHeadRange
        CalcGoalPosHead = _CalcAngle(headRange.HeadRangeMax,
                                     headRange.HeadRangeMin,
                                     GoalPosHeadPer)
        CalcGoalPosNeck = _CalcAngle(headRange.NeckRangeMax,
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
            CalcGolPosShoulderRight = _CalcAngle(armRangeRight.ArmShoulderRightMax, armRangeRight.ArmShoulderRightMin, ArmShoulderAngleRightPer)
            CalcGolPosForearmRight = _CalcAngle(armRangeRight.ArmForearmRightMax, armRangeRight.ArmForearmRightMin, ArmForearmAngleRightPer)
            CalcGolPosElbowTopRight = _CalcAngle(armRangeRight.ArmElbowTopRightMax, armRangeRight.ArmElbowTopRightMin, ArmElbowTopAngleRightPer)
            CalcGolPosElbowBottRight = _CalcAngle(armRangeRight.ArmElbowBottRightMax, armRangeRight.ArmElbowBottRightMin, ArmElbowBottAngleRightPer)

            CalcGolPosShoulderLeft = _CalcAngle(armRangeLeft.ArmShoulderLeftMax, armRangeLeft.ArmShoulderLeftMin, ArmShoulderAngleLeftPer)
            CalcGolPosForearmLeft = _CalcAngle(armRangeLeft.ArmForearmLeftMax, armRangeLeft.ArmForearmLeftMin, ArmForearmAngleLeftPer)
            CalcGolPosElbowTopLeft = _CalcAngle(armRangeLeft.ArmElbowTopLeftMax, armRangeLeft.ArmElbowTopLeftMin, ArmElbowTopAngleLeftPer)
            CalcGolPosElbowBottLeft = _CalcAngle(armRangeLeft.ArmElbowBottLeftMax, armRangeLeft.ArmElbowBottLeftMin, ArmElbowBottAngleLeftPer)
        else:
            CalcGolPosShoulderRight = _CalcAngle(armRangeRight.ArmShoulderRightMax, armRangeRight.ArmShoulderRightMin, ArmShoulderAngleRightPer)
            CalcGolPosForearmRight = _CalcAngle(armRangeRight.ArmForearmRightMax, armRangeRight.ArmForearmRightMin, ArmForearmAngleRightPer)
            CalcGolPosElbowTopRight = _CalcAngle(armRangeRight.ArmElbowTopRightMax, armRangeRight.ArmElbowTopRightMin, ArmElbowAngleRightPer)
            CalcGolPosElbowBottRight = _CalcAngle(armRangeRight.ArmElbowBottRightMax, armRangeRight.ArmElbowBottRightMin, ArmElbowAngleRightPer)

            CalcGolPosShoulderLeft = _CalcAngle(armRangeLeft.ArmShoulderLeftMax, armRangeLeft.ArmShoulderLeftMin, ArmShoulderAngleLeftPer)
            CalcGolPosForearmLeft = _CalcAngle(armRangeLeft.ArmForearmLeftMax, armRangeLeft.ArmForearmLeftMin, ArmForearmAngleLeftPer)
            CalcGolPosElbowTopLeft = _CalcAngle(armRangeLeft.ArmElbowTopLeftMax, armRangeLeft.ArmElbowTopLeftMin, ArmElbowAngleLeftPer)
            CalcGolPosElbowBottLeft = _CalcAngle(armRangeLeft.ArmElbowBottLeftMax, armRangeLeft.ArmElbowBottLeftMin, ArmElbowAngleLeftPer)

        return (CalcGolPosShoulderRight, CalcGolPosForearmRight, CalcGolPosElbowTopRight, CalcGolPosElbowBottRight,
                CalcGolPosShoulderLeft, CalcGolPosForearmLeft, CalcGolPosElbowTopLeft, CalcGolPosElbowBottLeft)

    def CalcPress(self, PressTopAnglePer, PressBottAnglePer):
        pressRange = self._positionRange.GetPressRange
        CalcGoalPosPressTop = _CalcAngle(pressRange.PressTopAngleMax, pressRange.PressTopAngleMin, PressTopAnglePer)
        CalcGoalPosPressBott = _CalcAngle(pressRange.PressBottAngleMax, pressRange.PressBottAngleMin, PressBottAnglePer)

        return CalcGoalPosPressTop, CalcGoalPosPressBott

    def CalcBody(self, BodyRotPer):
        bodyRange = self._positionRange.GetBodyRange
        CalcGoalPosBody = _CalcAngle(bodyRange.BodyRotMax, bodyRange.BodyRotMin, BodyRotPer)

        return CalcGoalPosBody

    def CalcLeg(self, HighBothLegPer, HighLeftLegPer, HighRightLegPer, SwitchBothLeg):

        legRangeRight = self._positionRange.GetLegRightRange
        legRangeLeft = self._positionRange.GetLegLeftRange

        if not SwitchBothLeg:
            # right
            CalcGoalPosHipRight = _CalcAngle(legRangeRight.LegHipAngRightMax, legRangeRight.LegHipAngRightMin, HighRightLegPer)
            CalcGoalPosFootRight = _CalcAngle(legRangeRight.LegFootAngRightMax, legRangeRight.LegFootAngRightMin, HighRightLegPer)
            CalcGoalPosKneeRight = _CalcAngle(legRangeRight.LegKneeAngRightMax, legRangeRight.LegKneeAngRightMin, HighRightLegPer)
            # left
            CalcGoalPosHipLeft = _CalcAngle(legRangeLeft.LegHipAngLeftMax, legRangeLeft.LegHipAngLeftMin, HighLeftLegPer)
            CalcGoalPosFootLeft = _CalcAngle(legRangeLeft.LegFootAngLeftMax, legRangeLeft.LegFootAngLeftMin, HighLeftLegPer)
            CalcGoalPosKneeLeft = _CalcAngle(legRangeLeft.LegKneeAngLeftMax, legRangeLeft.LegKneeAngLeftMin, HighLeftLegPer)

        else:
            # right
            CalcGoalPosHipRight = _CalcAngle(legRangeRight.LegHipAngRightMax, legRangeRight.LegHipAngRightMin, HighBothLegPer)
            CalcGoalPosFootRight = _CalcAngle(legRangeRight.LegFootAngRightMax, legRangeRight.LegFootAngRightMin, HighBothLegPer)
            CalcGoalPosKneeRight = _CalcAngle(legRangeRight.LegKneeAngRightMax, legRangeRight.LegKneeAngRightMin, HighBothLegPer)
            # left
            CalcGoalPosHipLeft = _CalcAngle(legRangeLeft.LegHipAngLeftMax, legRangeLeft.LegHipAngLeftMin, HighBothLegPer)
            CalcGoalPosFootLeft = _CalcAngle(legRangeLeft.LegFootAngLeftMax, legRangeLeft.LegFootAngLeftMin, HighBothLegPer)
            CalcGoalPosKneeLeft = _CalcAngle(legRangeLeft.LegKneeAngLeftMax, legRangeLeft.LegKneeAngLeftMin, HighBothLegPer)

        return CalcGoalPosKneeRight, CalcGoalPosFootRight, CalcGoalPosHipRight, CalcGoalPosKneeLeft, CalcGoalPosFootLeft, CalcGoalPosHipLeft