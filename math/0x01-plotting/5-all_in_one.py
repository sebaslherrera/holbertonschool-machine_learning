#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig = plt.figure(tight_layout=True)
plt.suptitle('All in One')


fig.add_subplot(321)
plt.xlim(0, 10)
plt.plot(y0, 'r-')

fig.add_subplot(322)
plt.title("Men's Height vs Weight", fontsize="x-small")
plt.xlabel("Height (in)", fontsize="x-small")
plt.ylabel("Weight (lbs)", fontsize="x-small")
plt.plot(x1, y1, color="magenta", marker=".", linestyle="")

fig.add_subplot(323)
plt.title("Exponential Decay of C-14", fontsize="x-small")
plt.xlabel("Time (years)", fontsize="x-small")
plt.ylabel("Fraction Remaining", fontsize="x-small")
plt.xlim(0, max(x2))
plt.plot(x2, y2)
plt.yscale('log')

fig.add_subplot(324)
plt.title("Exponential Decay of C-14", fontsize="x-small")
plt.xlabel("Time (years)", fontsize="x-small")
plt.ylabel("Fraction Remaining", fontsize="x-small")
plt.ylim(bottom=0)
plt.xlim(0, max(x3))
plt.plot(x3, y31, label="C-14", linestyle="dashed", color="red")
plt.plot(x3, y32, label="Ra-226", color="green")
plt.legend(loc='upper right', fontsize='x-small')

fig.add_subplot(313)
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.hist(student_grades, range=(0, 100), edgecolor='black')
plt.title("Project A", fontsize='x-small')
plt.xlabel("Grades", fontsize='x-small')
plt.ylabel("Number of Students", fontsize='x-small')

plt.show()
