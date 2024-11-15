# -*- coding: utf-8 -*-
"""Assignment7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K2WID1KGtfIlkVEn2r6B9FW-OV311PEh

Q1]
"""

def isindependent(jointpmf):
    marginal_x = {x: sum(jointpmf[x].values()) for x in jointpmf}
    marginal_y = {}
    for x in jointpmf:
        for y in jointpmf[x]:
            marginal_y[y] = marginal_y.get(y, 0) + jointpmf[x][y]

    for x in jointpmf:
        for y in jointpmf[x]:
            if jointpmf[x][y] != (marginal_x[x] * marginal_y[y]):
                return False
    return True

def main():
    x_values = input("enter x values ").split(' ')
    y_values = input("enter y values ").split(' ')

    jointpmf = {}
    for x in x_values:
        jointpmf[x] = {}
        for y in y_values:
            jointpmf[x][y] = float(input(f"Enter the joint probability of X={x} and Y={y}: "))

    if isindependent(jointpmf):
        print("The given Joint PMF corresponds to independent random variables (X,Y).")
    else:
        print("The given Joint PMF does not correspond to independent random variables (X,Y).")

if __name__ == "__main__":
    main()

"""Q2]
plotting joint pmf and joint cdf
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def randomjointpmf(x_size, y_size):
    randommat = np.random.rand(x_size, y_size)
    joint_pmf = randommat / randommat.sum()
    return joint_pmf


def jointpmf3d(joint_pmf, x_values, y_values):
    X, Y = np.meshgrid(y_values, x_values)
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(X.ravel(), Y.ravel(),np.zeros_like(joint_pmf).ravel(), 0.5,0.5,joint_pmf.ravel(), shade=True)
    ax.set_title('Joint PMF')
    ax.set_xlabel('Y Values')
    ax.set_ylabel('X Values')
    ax.set_zlabel('Probability')
    ax.view_init(30, 120)  # Adjust viewing angle
    ax.set_box_aspect([1, 1, 2])
    plt.show()


def jointcdf(joint_pmf):
    jointcdf = np.cumsum(np.cumsum(jointpmf, axis=0), axis=1)
    X, Y = np.meshgrid(np.arange(jointcdf.shape[1]), np.arange(jointcdf.shape[0]))
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, jointcdf, cmap='viridis')
    ax.set_title('Joint CDF')
    ax.set_xlabel('Y Values')
    ax.set_ylabel('X Values')
    ax.set_zlabel('Cumulative Probability')
    ax.view_init(30, 120)
    ax.set_box_aspect([1, 1, 1])
    plt.show()

x_values = np.linspace(10, 20, 5)
y_values = np.linspace(-10, -1, 5)

jointpmf = randomjointpmf(len(x_values), len(y_values))
jointpmf3d(jointpmf, x_values, y_values)
jointcdf(jointpmf)

"""plotting marginal pmf and cdfs"""

import numpy as np
import matplotlib.pyplot as plt

def randomjointpmf(x_size, y_size):
    randommat = np.random.rand(x_size, y_size)
    joint_pmf = randommat / randommat.sum()
    return joint_pmf

def marginal_pmfs(joint_pmf, x_values, y_values):
    marginalx = joint_pmf.sum(axis=1)
    marginaly = joint_pmf.sum(axis=0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.bar(x_values, marginalx, color='pink')
    ax1.set_title('Marginal PMF for X')
    ax1.set_xlabel('X Values')
    ax1.set_ylabel('Probability')

    ax2.bar(y_values, marginaly, color='blue')
    ax2.set_title('Marginal PMF for Y')
    ax2.set_xlabel('Y Values')
    ax2.set_ylabel('Probability')

    plt.tight_layout()
    plt.show()

def marginal_cdfs(joint_pmf, xvalues, yvalues):
    marginalcdfx = joint_pmf.sum(axis=1).cumsum()
    marginalcdfy = joint_pmf.sum(axis=0).cumsum()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(xvalues, marginalcdfx, color='b')
    ax1.set_title('Marginal CDF for X')
    ax1.set_xlabel('X Values')
    ax1.set_ylabel('Cumulative Probability')

    ax2.plot(yvalues, marginalcdfy, color='r')
    ax2.set_title('Marginal CDF for Y')
    ax2.set_xlabel('Y Values')
    ax2.set_ylabel('Cumulative Probability')

    plt.tight_layout()
    plt.show()

xvalues = np.linspace(10, 20, 5)
yvalues = np.linspace(-10, -1, 5)

joint_pmf = randomjointpmf(len(xvalues), len(yvalues))

marginal_pmfs(joint_pmf, xvalues, yvalues)
marginal_cdfs(joint_pmf, xvalues, yvalues)

"""Q3]

"""

import numpy as np

def randomjointpmf(x_size, y_size):
    randommat = np.random.rand(x_size, y_size)
    jointpmf = randommat / randommat.sum()
    return jointpmf

def marginal_pmf(jointpmf):
    margx = np.array(np.sum(jointpmf, axis=1))
    margy = np.array(np.sum(jointpmf, axis=0))
    return margx, margy

x = np.arange(1, 3, step=1)
y = np.arange(1, 3, step=1)
jointpmf = randomjointpmf(x.size, y.size)

marginalx, marginaly = marginal_pmf(jointpmf)

EXY = np.sum(x[:, None] * y * jointpmf)
EX = np.sum(x * marginalx)
EY = np.sum(y * marginaly)
EX1Y1 = EXY - EX * EY

print('E[XY] =', EXY)
print('E[X1Y1] =', EX1Y1)