import pandas as pd
import csv
import matplotlib.pyplot as plt

df = pd.read_csv("stars_with_gravity.csv")

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()
gravity = df['Gravity'].to_list()

radius.sort()
mass.sort()
gravity.sort()

plt.plot(mass, radius)
plt.title("Mass vs. Radius")
plt.xlabel("Mass") 
plt.ylabel("Radius") 
plt.show()

plt.plot(mass, gravity)
plt.title("Mass vs. Gravity")
plt.xlabel("Mass") 
plt.ylabel("Gravity") 
plt.show()

plt.plot(radius, gravity)
plt.title("Radius vs. Gravity")
plt.xlabel("Radius") 
plt.ylabel("Gravity") 
plt.show()

plt.scatter(radius, gravity)
plt.title("Radius vs. Gravity")
plt.xlabel("Radius") 
plt.ylabel("Gravity") 
plt.show()