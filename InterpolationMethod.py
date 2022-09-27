from ReadHomPos import ReadHomPos


class calcPosServo():
    def __init__(self):
        self._ReadPosArray = ReadHomPos.ReadServRange()

    def CalcHead(self, GoalPosHeadPer, GoalPosNeckPer):

        HeadRangeMin = self._ReadPosArray[0][0][0]
        HeadRangeMax = self._ReadPosArray[0][1][0]
        NeckRangeMin = self._ReadPosArray[0][2][0]
        NeckRangeMax = self._ReadPosArray[0][3][0]

        CalcGoalPosHead = self._CalcAngle(HeadRangeMax, HeadRangeMin, GoalPosHeadPer)
        CalcGoalPosNeck = self._CalcAngle(NeckRangeMax, NeckRangeMin, GoalPosNeckPer)

        return CalcGoalPosHead, CalcGoalPosNeck

    def CalcArms(self, ArmShoulderAnglRightPer, ArmForearmAnglRightPer, ArmElbowTopAnglRightPer,
                 ArmElbowBottAnglRightPer, ArmElbowAnglRightPer, ArmShoulderAnglLeftPer,
                 ArmForearmAnglLeftPer, ArmElbowTopAnglLeftPer, ArmElbowBottAnglLeftPer,
                 ArmElbowAnglLeftPer, SwitchBothElbow):

        ArmShoulderRightMin = self._ReadPosArray[1][0][0]
        ArmShoulderRightMax = self._ReadPosArray[1][1][0]
        ArmForearmRightMin = self._ReadPosArray[1][2][0]
        ArmForearmRightMax = self._ReadPosArray[1][3][0]
        ArmElbowTopRightMin = self._ReadPosArray[1][4][0]
        ArmElbowTopRightMax = self._ReadPosArray[1][5][0]
        ArmElbowBottRightMin = self._ReadPosArray[1][6][0]
        ArmElbowBottRightMax = self._ReadPosArray[1][7][0]

        ArmShoulderLeftMax = self._ReadPosArray[2][0][0]  # electronic range exclusion
        ArmShoulderLeftMin = self._ReadPosArray[2][1][0]  # electronic range exclusion
        ArmForearmLeftMin = self._ReadPosArray[2][2][0]
        ArmForearmLeftMax = self._ReadPosArray[2][3][0]
        ArmElbowTopLeftMin = self._ReadPosArray[2][4][0]
        ArmElbowTopLeftMax = self._ReadPosArray[2][5][0]
        ArmElbowBottLeftMin = self._ReadPosArray[2][6][0]
        ArmElbowBottLeftMax = self._ReadPosArray[2][7][0]

        if SwitchBothElbow == False:
            CalcGolPosShoulderRight = self._CalcAngle(ArmShoulderRightMax, ArmShoulderRightMin, ArmShoulderAnglRightPer)
            CalcGolPosForearmRight = self._CalcAngle(ArmForearmRightMax, ArmForearmRightMin, ArmForearmAnglRightPer)
            CalcGolPosElbowTopRight = self._CalcAngle(ArmElbowTopRightMax, ArmElbowTopRightMin, ArmElbowTopAnglRightPer)
            CalcGolPosElbowBottRight = self._CalcAngle(ArmElbowBottRightMax, ArmElbowBottRightMin, ArmElbowBottAnglRightPer)

            CalcGolPosShoulderLeft = self._CalcAngle(ArmShoulderLeftMax, ArmShoulderLeftMin, ArmShoulderAnglLeftPer)
            CalcGolPosForearmLeft = self._CalcAngle(ArmForearmLeftMax, ArmForearmLeftMin, ArmForearmAnglLeftPer)
            CalcGolPosElbowTopLeft = self._CalcAngle(ArmElbowTopLeftMax, ArmElbowTopLeftMin, ArmElbowTopAnglLeftPer)
            CalcGolPosElbowBottLeft = self._CalcAngle(ArmElbowBottLeftMax, ArmElbowBottLeftMin, ArmElbowBottAnglLeftPer)

        else:

            CalcGolPosShoulderRight = self._CalcAngle(ArmShoulderRightMax, ArmShoulderRightMin, ArmShoulderAnglRightPer)
            CalcGolPosForearmRight = self._CalcAngle(ArmForearmRightMax, ArmForearmRightMin, ArmForearmAnglRightPer)
            CalcGolPosElbowTopRight = self._CalcAngle(ArmElbowTopRightMax, ArmElbowTopRightMin, ArmElbowAnglRightPer)
            CalcGolPosElbowBottRight = self._CalcAngle(ArmElbowBottRightMax, ArmElbowBottRightMin, ArmElbowAnglRightPer)

            CalcGolPosShoulderLeft = self._CalcAngle(ArmShoulderLeftMax, ArmShoulderLeftMin, ArmShoulderAnglLeftPer)
            CalcGolPosForearmLeft = self._CalcAngle(ArmForearmLeftMax, ArmForearmLeftMin, ArmForearmAnglLeftPer)
            CalcGolPosElbowTopLeft = self._CalcAngle(ArmElbowTopLeftMax, ArmElbowTopLeftMin, ArmElbowAnglLeftPer)
            CalcGolPosElbowBottLeft = self._CalcAngle(ArmElbowBottLeftMax, ArmElbowBottLeftMin, ArmElbowAnglLeftPer)

        return (CalcGolPosShoulderRight, CalcGolPosForearmRight, CalcGolPosElbowTopRight, CalcGolPosElbowBottRight,
                CalcGolPosShoulderLeft, CalcGolPosForearmLeft, CalcGolPosElbowTopLeft, CalcGolPosElbowBottLeft)

    def CalcPress(self, PressTopAnglPer, PressBottAnglPer):

        PressTopAnglMin = self._ReadPosArray[3][0][0]
        PressTopAnglMax = self._ReadPosArray[3][1][0]
        PressBottAnglMin = self._ReadPosArray[3][2][0]
        PressBottAnglMax = self._ReadPosArray[3][3][0]

        CalcGoalPosPressTop = self._CalcAngle(PressTopAnglMax, PressTopAnglMin, PressTopAnglPer)
        CalcGoalPosPressBott = self._CalcAngle(PressBottAnglMax, PressBottAnglMin, PressBottAnglPer)

        return CalcGoalPosPressTop, CalcGoalPosPressBott

    def CalcBody(self, BodyRotPer):

        BodyRotMin = self._ReadPosArray[4][0][0]
        BodyRotMax = self._ReadPosArray[4][1][0]

        CalcGoalPosBody = self._CalcAngle(BodyRotMax, BodyRotMin, BodyRotPer)

        return CalcGoalPosBody

    def CalcLeg(self, HightBothLegPer, HightLeftLegPer, HightRightLegPer, SwitchBothLeg):

        LegHipAngRightMin = self._ReadPosArray[5][4][0]
        LegHipAngRightMax = self._ReadPosArray[5][5][0]
        LegFootAngRightMin = self._ReadPosArray[5][2][0]
        LegFootAngRightMax = self._ReadPosArray[5][3][0]
        LegKneeAngRightMin = self._ReadPosArray[5][0][0]
        LegKneeAngRightMax = self._ReadPosArray[5][1][0]

        LegHipAngLeftMin = self._ReadPosArray[6][4][0]
        LegHipAngLeftMax = self._ReadPosArray[6][5][0]
        LegFootAngLeftMin = self._ReadPosArray[6][2][0]
        LegFootAngLeftMax = self._ReadPosArray[6][3][0]
        LegKneeAngLeftMin = self._ReadPosArray[6][0][0]
        LegKneeAngLeftMax = self._ReadPosArray[6][1][0]

        if SwitchBothLeg == False:

            CalcGoalPosHipRight = self._CalcAngle(LegHipAngRightMax, LegHipAngRightMin, HightRightLegPer)
            CalcGoalPosFootRight = self._CalcAngle(LegFootAngRightMax, LegFootAngRightMin, HightRightLegPer)
            CalcGoalPosKneeRight = self._CalcAngle(LegKneeAngRightMax, LegKneeAngRightMin, HightRightLegPer)

            CalcGoalPosHipLeft = self._CalcAngle(LegHipAngLeftMax, LegHipAngLeftMin, HightLeftLegPer)
            CalcGoalPosFootLeft = self._CalcAngle(LegFootAngLeftMax, LegFootAngLeftMin, HightLeftLegPer)
            CalcGoalPosKneeLeft = self._CalcAngle(LegKneeAngLeftMax, LegKneeAngLeftMin, HightLeftLegPer)

        else:

            CalcGoalPosHipRight = self._CalcAngle(LegHipAngRightMax, LegHipAngRightMin, HightBothLegPer)
            CalcGoalPosFootRight = self._CalcAngle(LegFootAngRightMax, LegFootAngRightMin, HightBothLegPer)
            CalcGoalPosKneeRight = self._CalcAngle(LegKneeAngRightMax, LegKneeAngRightMin, HightBothLegPer)

            CalcGoalPosHipLeft = self._CalcAngle(LegHipAngLeftMax, LegHipAngLeftMin, HightBothLegPer)
            CalcGoalPosFootLeft = self._CalcAngle(LegFootAngLeftMax, LegFootAngLeftMin, HightBothLegPer)
            CalcGoalPosKneeLeft = self._CalcAngle(LegKneeAngLeftMax, LegKneeAngLeftMin, HightBothLegPer)

        return CalcGoalPosHipRight, CalcGoalPosFootRight, CalcGoalPosKneeRight, CalcGoalPosHipLeft, CalcGoalPosFootLeft, CalcGoalPosKneeLeft

    def _CalcAngle(self, angleMax, angleMin, anglePer):
        position = ((angleMax - angleMin) * anglePer) + angleMin
        return position
