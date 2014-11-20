from pymu import Pymu
import time

x=Pymu('Complementary',0.5)

data = [5,5,5,1,1,1]
x.update(data)
x.update(data)
