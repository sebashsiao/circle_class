from Circle import circle
from Circle import circumference
from Circle import area
from Circle import diameter

# from Circle import circle.diameter as dm


radius = 3

print('Radius of circle =', radius)
print('Circumference =', circle.circumference(radius))
print('Area =', circle.area(radius))
print('Diameter =', circle.diameter(radius))

print(circumference(radius))
print(area(radius))
print(diameter(radius))