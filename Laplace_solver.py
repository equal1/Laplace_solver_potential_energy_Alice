#  set normalized dimensions, unit of length is in [nm], unit of fields in meV
import numpy as np
import matplotlib.pyplot as plt

dx = 1
dy = 1

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
                print(j)
                if len_source * (j + 1) + len_gate * j < column <= (len_gate + len_source) * (j + 1):
                    u[row][column] = v_gate
                if len_source * (j + 1) + len_gate * (j + 1) < column <= (len_source + len_gate + len_source) * (j + 1):
                    u[row][column] = v_source


plt.contourf(u)
plt.show()