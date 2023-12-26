# -*- coding: utf-8 -*-
"""domSystem4(final).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1At5OyXBvirlxy4Qy2Y_Z8H7iYjawB3LU
"""

#we imported the essential libraries numpy and matplotlib and also imported the solve_ivp funcction
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the equations of motion for a double pendulum
def double_pendulum(t, state, l1, l2, m1, m2, g):
    theta1, omega1, theta2, omega2 = state

    delta = theta2 - theta1
    den1 = (m1 + m2) * l1 - m2 * l1 * np.cos(delta) ** 2
    den2 = (l2 / l1) * den1
   #these are the denominators of the two equation of motion den1 and den2

    dtheta1 = omega1
    domega1 = (m2 * l1 * omega1 ** 2 * np.sin(delta) * np.cos(delta) +
               m2 * g * np.sin(theta2) * np.cos(delta) +
               m2 * l2 * omega2 ** 2 * np.sin(delta) -
               (m1 + m2) * g * np.sin(theta1)) / den1

    dtheta2 = omega2
    domega2 = (-l2 / l1 * omega1 ** 2 * np.sin(delta) * np.cos(delta) +
               (m1 + m2) * g * np.sin(theta1) * np.cos(delta) -
               (m1 + m2) * l1 * omega1 ** 2 * np.sin(delta) -
               (m1 + m2) * g * np.sin(theta2)) / den2

    return [dtheta1, domega1, dtheta2, domega2]

#initial conditions
l1, l2 = 1.0, 1.0  # Lengths of the pendulum rods
m1, m2 = 1.0, 1.0  # Masses of the pendulum bobs
g = 9.81  # Acceleration due to gravity

initial_state = [np.pi / 3, 0, np.pi / 2, 1.5]  # Initial angles and angular velocities(the second parameter)

# Time span
t_span = (0, 20)
num_points = 10000

# Solve the ODE using solve_ivp (initial value problem)
sol = solve_ivp(double_pendulum, t_span, initial_state, args=(l1, l2, m1, m2, g), t_eval=np.linspace(t_span[0], t_span[1], num_points))

# Plots the motion of the double pendulum
plt.plot(sol.t, sol.y[0], label="Pendulum 1")
plt.plot(sol.t, sol.y[2], label="Pendulum 2")
plt.xlabel('Time (in seconds)')
plt.ylabel('Theta (Radians)')
plt.legend()
plt.title('Double Pendulum Motion for theta vs time graph')
plt.show()
plt.plot(sol.t, sol.y[1], label="Pendulum 1")
plt.plot(sol.t, sol.y[3], label="Pendulum 2")
plt.xlabel('Time (in seconds)')
plt.ylabel('Omega (in radians/seconds)')
plt.title('Double Pendulum Motion for Omega vs time graph')
plt.legend()
plt.show()