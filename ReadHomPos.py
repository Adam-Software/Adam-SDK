
class ReadHomPos():

    def ReadServRange(self):
        
        line = []
        with open('positionrange.txt', 'r') as f:
            line = f.read() 
        line = line.split('\n')
        data = []

        for l in line:
            get = l.split(',')
            for i in range(len(get)):
                if get[i]: get[i] = int(get[i]),
                else: get.remove('')
            data.append(get)

        HeadRange     = [data[0][0], data[0][1], data[0][2], data[0][3]]
        ArmRangeRight = [data[1][0], data[1][1], data[1][2], data[1][3], data[1][4], data[1][5], data[1][6], data[1][7]]
        ArmRangeLeft  = [data[2][0], data[2][1], data[2][2], data[2][3], data[2][4], data[2][5], data[2][6], data[2][7]]
        PressRange    = [data[3][0], data[3][1], data[3][2], data[3][3]]
        BodyRange     = [data[4][0], data[4][1]]
        LegRightRange = [data[5][0], data[5][1], data[5][2], data[5][3], data[5][4], data[5][5]]
        LegLeftRange  = [data[6][0], data[6][1], data[6][2], data[6][3], data[6][4], data[6][5]]
        HandsRange    = [data[7][0], data[7][1], data[7][2], data[7][3]]

        return HeadRange, ArmRangeRight, ArmRangeLeft, PressRange, BodyRange, LegRightRange, LegLeftRange, HandsRange
   