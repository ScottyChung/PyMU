import numpy

class PyMU:
    """A placeholder for now"""
    #Insert Variables here
    angle = [0,0,0]
    def __init__(self,filterType,timestep):
        self.filtType = filterType
        self.timestep = timestep

    def update(self,data):
        self.data = data
        print(data)
        if(self.filtType.lower() == 'complementary'):
            self.comprun()
        elif(self.filtType.lower() == 'mahony'):
            self.mahorun()

    def comprun(self):
        print('Inside comprun')
        print('Using data ')
        print(self.data)
        self.angle = [x+self.data*self.timestep for x in self.data]
        print('Calculated angle')
        print(self.angle)



    def mahorun(self):
        print('Inside mahorun')
