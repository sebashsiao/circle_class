class Circle:
    pi = 3.1416
    def circumference(self, radius):
        # 2*pi*r
        return 2 * radius * self.pi

    def area(self, radius):
        # pi*r**2
        return self.pi * (radius ** 2)

    def diameter(self, radius):
        return radius * 2




# Instantiate class Circle()
circle = Circle()

print('Circumference =', circle.circumference(5))
print('Area =', circle.area(5))
print('Diameter =', circle.diameter(5))


