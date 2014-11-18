import numpy as np

class PyMU:
    """A placeholder for now"""
    #Insert Variables here
    angle = np.array([0,0,0])
    def __init__(self,filterType,timestep):
        self.filtType = filterType
        self.timestep = timestep

    def update(self,data):
        self.data = data
        if(self.filtType.lower() == 'complementary'):
            self.comprun()
        elif(self.filtType.lower() == 'mahony'):
            self.mahorun()

    def comprun(self):
        print('Inside comprun')
        self.angle += np.array(self.data)
        print('Calculated angle')
        print(self.angle)



    def mahorun(self):
        print('Inside mahorun')
