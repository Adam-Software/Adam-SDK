import InterpolationUtils


class InterpolationMethodsLegs:

    def __init__(self, positionRange):
        self._legRangeRight = positionRange.GetLegRightRange
        self._legRangeLeft = positionRange.GetLegLeftRange

    #
    # Right leg calculation
    #

    def CalcLegRight(self, HighRightLegPer):

        CalcGoalPosHipRight = InterpolationUtils.CalcAngle(self._legRangeRight.LegHipAngRightMax,
                                                           self._legRangeRight.LegHipAngRightMin,
                                                           HighRightLegPer)
        CalcGoalPosFootRight = InterpolationUtils.CalcAngle(self._legRangeRight.LegFootAngRightMax,
                                                            self._legRangeRight.LegFootAngRightMin,
                                                            HighRightLegPer)
        CalcGoalPosKneeRight = InterpolationUtils.CalcAngle(self._legRangeRight.LegKneeAngRightMax,
                                                            self._legRangeRight.LegKneeAngRightMin,
                                                            HighRightLegPer)

        return CalcGoalPosKneeRight, CalcGoalPosFootRight, CalcGoalPosHipRight

    def CalcLegRightElbow(self, HighBothLegPer):

        CalcGoalPosHipRight = InterpolationUtils.CalcAngle(self._legRangeRight.LegHipAngRightMax,
                                                           self._legRangeRight.LegHipAngRightMin,
                                                           HighBothLegPer)
        CalcGoalPosFootRight = InterpolationUtils.CalcAngle(self._legRangeRight.LegFootAngRightMax,
                                                            self._legRangeRight.LegFootAngRightMin,
                                                            HighBothLegPer)
        CalcGoalPosKneeRight = InterpolationUtils.CalcAngle(self._legRangeRight.LegKneeAngRightMax,
                                                            self._legRangeRight.LegKneeAngRightMin,
                                                            HighBothLegPer)

        return CalcGoalPosKneeRight, CalcGoalPosFootRight, CalcGoalPosHipRight

    #
    # Left leg calculation
    #

    def CalcLegLeft(self, HighLeftLegPer):

        CalcGoalPosHipLeft = InterpolationUtils.CalcAngle(self._legRangeLeft.LegHipAngLeftMax,
                                                          self._legRangeLeft.LegHipAngLeftMin,
                                                          HighLeftLegPer)
        CalcGoalPosFootLeft = InterpolationUtils.CalcAngle(self._legRangeLeft.LegFootAngLeftMax,
                                                           self._legRangeLeft.LegFootAngLeftMin,
                                                           HighLeftLegPer)
        CalcGoalPosKneeLeft = InterpolationUtils.CalcAngle(self._legRangeLeft.LegKneeAngLeftMax,
                                                           self._legRangeLeft.LegKneeAngLeftMin,
                                                           HighLeftLegPer)

        return CalcGoalPosKneeLeft, CalcGoalPosFootLeft, CalcGoalPosHipLeft

    def CalcLegLeftElbow(self, HighBothLegPer):

        CalcGoalPosHipLeft = InterpolationUtils.CalcAngle(self._legRangeLeft.LegHipAngLeftMax,
                                                          self._legRangeLeft.LegHipAngLeftMin,
                                                          HighBothLegPer)
        CalcGoalPosFootLeft = InterpolationUtils.CalcAngle(self._legRangeLeft.LegFootAngLeftMax,
                                                           self._legRangeLeft.LegFootAngLeftMin,
                                                           HighBothLegPer)
        CalcGoalPosKneeLeft = InterpolationUtils.CalcAngle(self._legRangeLeft.LegKneeAngLeftMax,
                                                           self._legRangeLeft.LegKneeAngLeftMin,
                                                           HighBothLegPer)

        return CalcGoalPosKneeLeft, CalcGoalPosFootLeft, CalcGoalPosHipLeft
