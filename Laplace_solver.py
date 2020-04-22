#  set normalized dimensions, unit of length is in [nm], unit of fields in meV
import numpy as np
import matplotlib.pyplot as plt

dx = 1
dy = 1
max_iterations = 200

len_source = 25 / dx
width_source = 17 / dy

len_gate = 40 / dx
width_gate = width_source
width_structure = 80 / dy

number_of_devices = 5
v_gate = 400
v_source = 0

v_bottom = 0
v_left = 0
v_right = 0

# set dimensions of grid
len_x = int(number_of_devices * (len_source + len_gate) + len_source)
len_y = int(width_structure)
grid_x = range(0, len_x)
grid_y = range(0, len_y)

# initialize solution
u_guess = 10
rows_init = len(grid_y)
columns_init = len(grid_x)
u = np.full((rows_init, columns_init), u_guess)

# set boundary conditions

# bottom grid
u[0, :] = v_bottom

# left and right grid
u[:, -1] = v_right
u[:, 0] = v_left

# top grid
for row in range(rows_init):
    for column in range(columns_init):
        if row >= rows_init - width_gate:
            for j in range(number_of_devices):
                if len_source * (j + 1) + len_gate * j < column <= (len_gate + len_source) * (j + 1):
                    u[row][column] = v_gate
                if len_source * (j + 1) + len_gate * (j + 1) < column <= (len_source + len_gate + len_source) * (j + 1):
                    u[row][column] = v_source

fig = plt.figure(1)
plt.contourf(u)


test_init = 0
for kk in range(max_iterations):
    for row in range(1, rows_init - 1):
        for column in range(1, columns_init - 1):
            if row >= rows_init - width_gate:
                for j in range(number_of_devices):
                    if len_source * (j + 1) + len_gate * j < column <= (len_gate + len_source) * (j + 1):
                        u[row][column] = v_gate
                    if len_source * (j + 1) + len_gate * (j + 1) < column <= (len_source + len_gate + len_source)\
                            * (j + 1):
                        u[row][column] = v_source
                test_init = 1
            if test_init == 1:
                test_init = 0
            else:
                u[row][column] = 0.25 * (u[row + 1][column] + u[row - 1][column] + u[row][column+1] + u[row][column - 1])
        #u[0][0] = 0.5 * (u[0][1] + u[1][0])
        #u[-1][0] = 0.5 * (u[-2][0] + u[-1][1])
        #u[0][-1] = 0.5 * (u[0][-2] + u[1][-1])
        #u[-1][-1] = 0.5 *(u[-1][-2] + u[-2][-1])

fig2 = plt.figure(2)
plt.contourf(u)
fig3 = plt.figure(3)
plt.plot(u[int(70/dy)])
plt.show()
