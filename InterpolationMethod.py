from ReadHomPos import ReadHomPos

class calcPosServo():
    def __init__(self):
        super().__init__()


    def CalcHead(self, GoalPosHeadPer, GoalPosNeckPer):

        ReadPosArray = ReadHomPos()
             
        HeadRangeArray = ReadPosArray.ReadServRange()
    
        HeadRangeMin = HeadRangeArray[0][0][0]
        HeadRangeMax = HeadRangeArray[0][1][0]
        NeckRangeMin = HeadRangeArray[0][2][0]
        NeckRangeMax = HeadRangeArray[0][3][0]
    
        CalcGoalPosHead = ((HeadRangeMax - HeadRangeMin) * GoalPosHeadPer) + HeadRangeMin
        CalcGoalPosNeck = ((NeckRangeMax - NeckRangeMin) * GoalPosNeckPer) + NeckRangeMin
     
        return CalcGoalPosHead, CalcGoalPosNeck

    def CalcArms(self, ArmShoulderAnglRightPer, ArmForearmAnglRightPer, ArmElbowTopAnglRightPer, ArmElbowBottAnglRightPer, ArmElbowAnglRightPer,
                 ArmShoulderAnglLeftPer, ArmForearmAnglLeftPer, ArmElbowTopAnglLeftPer, ArmElbowBottAnglLeftPer, ArmElbowAnglLeftPer, SwitchBothElbow):

        ReadPosArray = ReadHomPos()

        ArmRangeArray  = ReadPosArray.ReadServRange()
  
        ArmShoulderRightMin = ArmRangeArray[1][0][0]
        ArmShoulderRightMax = ArmRangeArray[1][1][0]
        ArmForearmRightMin  = ArmRangeArray[1][2][0]
        ArmForearmRightMax  = ArmRangeArray[1][3][0]
        ArmElbowTopRightMin = ArmRangeArray[1][4][0]
        ArmElbowTopRightMax = ArmRangeArray[1][5][0]
        ArmElbowBottRightMin = ArmRangeArray[1][6][0]
        ArmElbowBottRightMax = ArmRangeArray[1][7][0]

        ArmShoulderLeftMax = ArmRangeArray[2][0][0] #electronic range exclusion
        ArmShoulderLeftMin = ArmRangeArray[2][1][0] #electronic range exclusion
        ArmForearmLeftMin  = ArmRangeArray[2][2][0]
        ArmForearmLeftMax  = ArmRangeArray[2][3][0]
        ArmElbowTopLeftMin = ArmRangeArray[2][4][0]
        ArmElbowTopLeftMax = ArmRangeArray[2][5][0]
        ArmElbowBottLeftMin = ArmRangeArray[2][6][0]
        ArmElbowBottLeftMax = ArmRangeArray[2][7][0]

        if SwitchBothElbow == False:

            CalcGolPosShoulderRight = ((ArmShoulderRightMax - ArmShoulderRightMin) * ArmShoulderAnglRightPer) + ArmShoulderRightMin
            CalcGolPosForearmRight = ((ArmForearmRightMax - ArmForearmRightMin) * ArmForearmAnglRightPer) + ArmForearmRightMin
            CalcGolPosElbowTopRight = ((ArmElbowTopRightMax - ArmElbowTopRightMin) * ArmElbowTopAnglRightPer) + ArmElbowTopRightMin
            CalcGolPosElbowBottRight = ((ArmElbowBottRightMax - ArmElbowBottRightMin) * ArmElbowBottAnglRightPer) + ArmElbowBottRightMin

            CalcGolPosShoulderLeft = ((ArmShoulderLeftMax - ArmShoulderLeftMin) * ArmShoulderAnglLeftPer) + ArmShoulderLeftMin
            CalcGolPosForearmLeft = ((ArmForearmLeftMax - ArmForearmLeftMin) * ArmForearmAnglLeftPer) + ArmForearmLeftMin
            CalcGolPosElbowTopLeft = ((ArmElbowTopLeftMax - ArmElbowTopLeftMin) * ArmElbowTopAnglLeftPer) + ArmElbowTopLeftMin
            CalcGolPosElbowBottLeft = ((ArmElbowBottLeftMax - ArmElbowBottLeftMin) * ArmElbowBottAnglLeftPer) + ArmElbowBottLeftMin

        else:

            CalcGolPosShoulderRight = ((ArmShoulderRightMax - ArmShoulderRightMin) * ArmShoulderAnglRightPer) + ArmShoulderRightMin
            CalcGolPosForearmRight = ((ArmForearmRightMax - ArmForearmRightMin) * ArmForearmAnglRightPer) + ArmForearmRightMin
            CalcGolPosElbowTopRight = ((ArmElbowTopRightMax - ArmElbowTopRightMin) * ArmElbowAnglRightPer) + ArmElbowTopRightMin
            CalcGolPosElbowBottRight = ((ArmElbowBottRightMax - ArmElbowBottRightMin) * ArmElbowAnglRightPer) + ArmElbowBottRightMin

            CalcGolPosShoulderLeft = ((ArmShoulderLeftMax - ArmShoulderLeftMin) * ArmShoulderAnglLeftPer) + ArmShoulderLeftMin
            CalcGolPosForearmLeft = ((ArmForearmLeftMax - ArmForearmLeftMin) * ArmForearmAnglLeftPer) + ArmForearmLeftMin
            CalcGolPosElbowTopLeft = ((ArmElbowTopLeftMax - ArmElbowTopLeftMin) * ArmElbowAnglLeftPer) + ArmElbowTopLeftMin
            CalcGolPosElbowBottLeft = ((ArmElbowBottLeftMax - ArmElbowBottLeftMin) * ArmElbowAnglLeftPer) + ArmElbowBottLeftMin
     
        return (CalcGolPosShoulderRight, CalcGolPosForearmRight, CalcGolPosElbowTopRight, CalcGolPosElbowBottRight,
                CalcGolPosShoulderLeft, CalcGolPosForearmLeft, CalcGolPosElbowTopLeft, CalcGolPosElbowBottLeft)

    def CalcPress(self, PressTopAnglPer, PressBottAnglPer):
    
        ReadPosArray = ReadHomPos()
             
        PressRangeArray  = ReadPosArray.ReadServRange()

        PressTopAnglMin  =  PressRangeArray[3][0][0]
        PressTopAnglMax  =  PressRangeArray[3][1][0]
        PressBottAnglMin =  PressRangeArray[3][2][0]
        PressBottAnglMax =  PressRangeArray[3][3][0]

        CalcGoalPosPressTop = ((PressTopAnglMax - PressTopAnglMin) * PressTopAnglPer) + PressTopAnglMin
        CalcGoalPosPressBott = ((PressBottAnglMax - PressBottAnglMin) * PressBottAnglPer) + PressBottAnglMin

        return CalcGoalPosPressTop, CalcGoalPosPressBott

    def CalcBody(self, BodyRotPer):

        ReadPosArray = ReadHomPos()
             
        BodyRotArray  = ReadPosArray.ReadServRange()
    
        BodyRotMin  =  BodyRotArray[4][0][0]
        BodyRotMax  =  BodyRotArray[4][1][0]

        CalcGoalPosBody = ((BodyRotMax - BodyRotMin) * BodyRotPer) + BodyRotMin

        return CalcGoalPosBody

    def CalcLeg(self, HightBothLegPer, HightLeftLegPer, HightRightLegPer, SwitchBothLeg):

        ReadPosArray = ReadHomPos()

        LegRangeArray = ReadPosArray.ReadServRange()

        LegHipAngRightMin = LegRangeArray[5][4][0]
        LegHipAngRightMax = LegRangeArray[5][5][0]
        LegFootAngRightMin = LegRangeArray[5][2][0]
        LegFootAngRightMax = LegRangeArray[5][3][0]
        LegKneeAngRightMin = LegRangeArray[5][0][0]
        LegKneeAngRightMax = LegRangeArray[5][1][0]

        LegHipAngLeftMin = LegRangeArray[6][4][0]
        LegHipAngLeftMax = LegRangeArray[6][5][0]
        LegFootAngLeftMin = LegRangeArray[6][2][0]
        LegFootAngLeftMax = LegRangeArray[6][3][0]
        LegKneeAngLeftMin = LegRangeArray[6][0][0]
        LegKneeAngLeftMax = LegRangeArray[6][1][0]

        if SwitchBothLeg == False:

             CalcGoalPosHipRight = ((LegHipAngRightMax - LegHipAngRightMin) * HightRightLegPer) + LegHipAngRightMin
             CalcGoalPosFootRight = ((LegFootAngRightMax - LegFootAngRightMin) * HightRightLegPer) + LegFootAngRightMin
             CalcGoalPosKneeRight = ((LegKneeAngRightMax - LegKneeAngRightMin) * HightRightLegPer) + LegKneeAngRightMin

             CalcGoalPosHipLeft = ((LegHipAngLeftMax - LegHipAngLeftMin) * HightLeftLegPer) + LegHipAngLeftMin
             CalcGoalPosFootLeft = ((LegFootAngLeftMax - LegFootAngLeftMin) * HightLeftLegPer) + LegFootAngLeftMin
             CalcGoalPosKneeLeft = ((LegKneeAngLeftMax - LegKneeAngLeftMin) * HightLeftLegPer) + LegKneeAngLeftMin
          
        else:
         
             CalcGoalPosHipRight = ((LegHipAngRightMax - LegHipAngRightMin) * HightBothLegPer) + LegHipAngRightMin
             CalcGoalPosFootRight = ((LegFootAngRightMax - LegFootAngRightMin) * HightBothLegPer) + LegFootAngRightMin
             CalcGoalPosKneeRight = ((LegKneeAngRightMax - LegKneeAngRightMin) * HightBothLegPer) + LegKneeAngRightMin

             CalcGoalPosHipLeft = ((LegHipAngLeftMax - LegHipAngLeftMin) * HightBothLegPer) + LegHipAngLeftMin
             CalcGoalPosFootLeft = ((LegFootAngLeftMax - LegFootAngLeftMin) * HightBothLegPer) + LegFootAngLeftMin
             CalcGoalPosKneeLeft = ((LegKneeAngLeftMax - LegKneeAngLeftMin) * HightBothLegPer) + LegKneeAngLeftMin

        return CalcGoalPosHipRight, CalcGoalPosFootRight, CalcGoalPosKneeRight, CalcGoalPosHipLeft, CalcGoalPosFootLeft, CalcGoalPosKneeLeft

