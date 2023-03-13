import matplotlib.pyplot as plt
import numpy as np


#class Circle(object):
#    def _init_(self, radius=3, color='blue'):
#       self.radius = radius
#        self.color = color 
#    def add_radius(self, r):
#        self.radius = self.radius + r
#        return(self.radius)
#    def drawCircle(self):
#        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
#        plt.axis('scaled')
#       plt.show()

#RedCircle = Circle(10, 'red')
#dir (RedCircle)
#RedCircle.radius

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

