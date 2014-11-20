import numpy as np

class Pymu:
    """Uses the user defined filtering for IMU

    Args:
    filterType(str): String naming desired filter name
    timestep(float): timestep the filter should operate
    """
    angle = np.array([0.0,0.0,0.0])
    def __init__(self,filterType,timestep):
        self.filtType = filterType
        self.timestep = timestep
        self.compPara = {'gyroConst':0.98}

    def update(self,data):
        self.data = data
        if(self.filtType.lower() == 'complementary'):
            self.comprun()
        elif(self.filtType.lower() == 'mahony'):
            self.mahorun()

    def comprun(self):
        print('Inside comprun')
        gAngle = np.array(self.data[0:3])*self.timestep
        accAngle = np.array(self.data[3:6])
        self.angle += self.compPara['gyroConst']*gAngle
        print('Calculated angle')
        print(self.angle)

    def mahorun(self):
        print('Inside mahorun')
