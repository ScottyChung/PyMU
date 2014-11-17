import pymu

x=pymu.PyMU('Complementary',1)

print x.filtType
data = [5,5,5]
x.update(data)
