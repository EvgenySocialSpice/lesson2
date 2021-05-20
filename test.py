import ephem
planet = input('enter: ').split()
a = getattr(ephem, planet[1])
mars = a('2000/01/01')
constellation = ephem.constellation(mars)
print(constellation)
