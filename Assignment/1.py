from numpy.random import uniform
'''
Håvard Kråkenes - 23.10.2018
Make a list of 500 temperature sensors, ranging from -100 deg to 100 deg.
Sorting using bubblesort, and check for temperature deviation.
'''
x = uniform(-100, 100, 500)
print(x)

# Sorting using bubble sort
for n in range(len(x)-1, 0, -1):
    for i in range(n):
        if x[i] > x[i+1]:
            tmp = x[i]
            x[i] = x[i+1]
            x[i+1] = tmp
print(x)

# Check for temperature deviation
for n in range(len(x)-1):
    # Check if temperature deviation is larger than 0.6 deg/cm
    if x[n+1]-x[n] > 0.6*2:
        print(
            f'There is a high temperature deviation between sensor {n+1} and {n+2}.')
