"Path Integration"

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

"""Suppose that an ant wandered randomly by taking steps (x,y), one per second,
where at each ant step, x and y come from a normal distribution with a mean of 0
and a standard deviation of 1.0mm (assume this for all questions below).
Plot a trace of the ant’s path over the course of an hour."""

mu = 0
sigma = 1
x_steps = []
y_steps = []
xPos = 0
yPos = 0
for step in range(3600):
    xPos = xPos + np.random.normal(mu, sigma)
    yPos = yPos + np.random.normal(mu, sigma)
    x_steps.append(xPos)
    y_steps.append(yPos)

plt.title('Trace of the ant’s path (over the course of an hour)')
plt.xlabel('x-location of ant')
plt.ylabel('y-location of ant')
plt.axis()
plt.plot(x_steps, y_steps,'-b', label='path')
plt.legend()
plt.show()

"""
Let’s think about why ants need to perform path integration.
Suppose that instead of path integration, when an ant found food,
it just continued to wander with random steps until it got back to the nest.
Using a simulation, find the probability that an ant who finds food after 1 hour
will make its way back to within 10mm of the nest over the course of the next
hour (note that if it comes within 10mm of a nest, it stops).
Is this a good strategy? Why or why not?"""

def distance(x1,x2,y1,y2):
    return np.sqrt(np.square(x2-x1) + np.square(y2-y1))

nest = [0, 0]
count = 0

for i in range(1000):
    random_path_X = np.cumsum(np.random.normal(mu, sigma, 3600))
    random_path_Y = np.cumsum(np.random.normal(mu, sigma, 3600))

    for j in range(3600):
        if distance(nest[0],random_path_X[i],nest[1],random_path_Y[i]) <= 10:
            count += 1
            break
probability = count/1000
print(probability)
