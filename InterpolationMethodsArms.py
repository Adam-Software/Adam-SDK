import InterpolationUtils


class InterpolationMethodsArms:

    def __init__(self, positionRange):
        self._armRangeRight = positionRange.GetArmRangeRight
        self._armRangeLeft = positionRange.GetArmRangeLeft

    #
    # Right arm calculation
    #

    def CalcArmRight(self, ArmShoulderAngleRightPer, ArmForearmAngleRightPer,
                     ArmElbowTopAngleRightPer, ArmElbowBottAngleRightPer):

        CalcGolPosShoulderRight = InterpolationUtils.CalcAngle(self._armRangeRight.ArmShoulderRightMax,
                                                               self._armRangeRight.ArmShoulderRightMin,
                                                               ArmShoulderAngleRightPer)
        CalcGolPosForearmRight = InterpolationUtils.CalcAngle(self._armRangeRight.ArmForearmRightMax,
                                                              self._armRangeRight.ArmForearmRightMin,
                                                              ArmForearmAngleRightPer)
        CalcGolPosElbowTopRight = InterpolationUtils.CalcAngle(self._armRangeRight.ArmElbowTopRightMax,
                                                               self._armRangeRight.ArmElbowTopRightMin,
                                                               ArmElbowTopAngleRightPer)
        CalcGolPosElbowBottRight = InterpolationUtils.CalcAngle(self._armRangeRight.ArmElbowBottRightMax,
                                                                self._armRangeRight.ArmElbowBottRightMin,
                                                                ArmElbowBottAngleRightPer)

        return CalcGolPosShoulderRight, CalcGolPosForearmRight, CalcGolPosElbowTopRight, CalcGolPosElbowBottRight

    def CalcArmRightElbow(self, ArmShoulderAngleRightPer, ArmForearmAngleRightPer, ArmElbowAngleRightPer):

        CalcGolPosShoulderRight = InterpolationUtils.CalcAngle(self._armRangeRight.ArmShoulderRightMax,
                                                               self._armRangeRight.ArmShoulderRightMin,
                                                               ArmShoulderAngleRightPer)
        CalcGolPosForearmRight = InterpolationUtils.CalcAngle(self._armRangeRight.ArmForearmRightMax,
                                                              self._armRangeRight.ArmForearmRightMin,
                                                              ArmForearmAngleRightPer)
        CalcGolPosElbowTopRight = InterpolationUtils.CalcAngle(self._armRangeRight.ArmElbowTopRightMax,
                                                               self._armRangeRight.ArmElbowTopRightMin,
                                                               ArmElbowAngleRightPer)
        CalcGolPosElbowBottRight = InterpolationUtils.CalcAngle(self._armRangeRight.ArmElbowBottRightMax,
                                                                self._armRangeRight.ArmElbowBottRightMin,
                                                                ArmElbowAngleRightPer)

        return CalcGolPosShoulderRight, CalcGolPosForearmRight, CalcGolPosElbowTopRight, CalcGolPosElbowBottRight

    #
    # Left arm calculation
    #

    def CalcArmLeft(self, ArmShoulderAngleLeftPer, ArmForearmAngleLeftPer,
                    ArmElbowAngleLeftPer, ArmElbowBottAngleRightPer):

        CalcGolPosShoulderLeft = InterpolationUtils.CalcAngle(self._armRangeLeft.ArmShoulderLeftMax,
                                                              self._armRangeLeft.ArmShoulderLeftMin,
                                                              ArmShoulderAngleLeftPer)
        CalcGolPosForearmLeft = InterpolationUtils.CalcAngle(self._armRangeLeft.ArmForearmLeftMax,
                                                             self._armRangeLeft.ArmForearmLeftMin,
                                                             ArmForearmAngleLeftPer)
        CalcGolPosElbowTopLeft = InterpolationUtils.CalcAngle(self._armRangeLeft.ArmElbowTopLeftMax,
                                                              self._armRangeLeft.ArmElbowTopLeftMin,
                                                              ArmElbowAngleLeftPer)
        CalcGolPosElbowBottLeft = InterpolationUtils.CalcAngle(self._armRangeLeft.ArmElbowBottLeftMax,
                                                               self._armRangeLeft.ArmElbowBottLeftMin,
                                                               ArmElbowBottAngleRightPer)

        return CalcGolPosShoulderLeft, CalcGolPosForearmLeft, CalcGolPosElbowTopLeft, CalcGolPosElbowBottLeft

    def CalcArmLeftElbow(self, ArmShoulderAngleLeftPer, ArmForearmAngleLeftPer, ArmElbowAngleLeftPer):

        CalcGolPosShoulderLeft = InterpolationUtils.CalcAngle(self._armRangeLeft.ArmShoulderLeftMax,
                                                              self._armRangeLeft.ArmShoulderLeftMin,
                                                              ArmShoulderAngleLeftPer)
        CalcGolPosForearmLeft = InterpolationUtils.CalcAngle(self._armRangeLeft.ArmForearmLeftMax,
                                                             self._armRangeLeft.ArmForearmLeftMin,
                                                             ArmForearmAngleLeftPer)
        CalcGolPosElbowTopLeft = InterpolationUtils.CalcAngle(self._armRangeLeft.ArmElbowTopLeftMax,
                                                              self._armRangeLeft.ArmElbowTopLeftMin,
                                                              ArmElbowAngleLeftPer)
        CalcGolPosElbowBottLeft = InterpolationUtils.CalcAngle(self._armRangeLeft.ArmElbowBottLeftMax,
                                                               self._armRangeLeft.ArmElbowBottLeftMin,
                                                               ArmElbowAngleLeftPer)

        return CalcGolPosShoulderLeft, CalcGolPosForearmLeft, CalcGolPosElbowTopLeft, CalcGolPosElbowBottLeft
