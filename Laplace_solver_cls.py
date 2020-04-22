#  set normalized dimensions, unit of length is in [nm], unit of fields in meV
import numpy as np
import matplotlib.pyplot as plt


class LaplaceSolverPotentialEnergy:
    def __init__(self, number_of_devices=5, v_gate=400, v_source=0, max_iterations=200, len_source=25,
                 width_source=17, len_gate=40, width_gate=17, width_structure=80, dx=1, dy=1):
        """
        This class calculates the potential energy profile of a chain of devices of a quantum core
        by solving the Laplace equation
        :type dy: object
        """
        self.number_of_devices = number_of_devices
        self.v_gate = v_gate
        self.v_source = v_source
        self.max_iterations = max_iterations
        self.len_source = len_source
        self.width_source = width_source
        self.len_gate = len_gate
        self.width_gate = width_gate
        self.width_structure = width_structure
        self.dx = dx
        self.dy = dy

        self.len_source = self.len_gate / self. dx
        self.width_source = self.width_source / self.dy
        self.len_gate = self.len_gate / self.dx
        self.width_gate = width_source
        self.width_structure = self.width_structure / self.dy

        self.v_bottom = 0
        self.v_left = 0
        self.v_right = 0

        # set dimensions of grid
        self.len_x = int(self.number_of_devices * (self.len_source + self.len_gate) + self.len_source)
        self.len_y = int(self.width_structure)
        self.grid_x = range(0, self.len_x)
        self.grid_y = range(0, self.len_y)

        # initialize solution
        self.rows_init = len(self.grid_y)
        self.columns_init = len(self.grid_x)

    def calculate_potential_energy(self):
        # set boundary conditions
        u_guess = 10
        u = np.full((self.rows_init, self.columns_init), u_guess)
        # bottom grid
        u[0, :] = self.v_bottom

        # left and right grid
        u[:, -1] = self.v_right
        u[:, 0] = self.v_left

        # top grid
        for row in range(self.rows_init):
            for column in range(self.columns_init):
                if row >= self.rows_init - self.width_gate:
                    for j in range(self.number_of_devices):
                        if self.len_source * (j + 1) + self.len_gate * j < column <= (self.len_gate + self.len_source) * (j + 1):
                            u[row][column] = self.v_gate
                        if self.len_source * (j + 1) + self.len_gate * (j + 1) < column <= (
                                self.len_source + self.len_gate + self.len_source) * (j + 1):
                            u[row][column] = self.v_source

        # iterate for max iterations
        for kk in range(self.max_iterations):
            for row in range(1, self.rows_init - 1):
                for column in range(1, self.columns_init - 1):
                    if row >= self.rows_init - self.width_gate:
                        for j in range(self.number_of_devices):
                            if self.len_source * (j + 1) + self.len_gate * j < column <= (self.len_gate
                                                                                          + self.len_source) * (j + 1):
                                u[row][column] = self.v_gate
                            if self.len_source * (j + 1) + self.len_gate * (j + 1) < column <= (
                                    self.len_source + self.len_gate + self.len_source) * (j + 1):
                                u[row][column] = self.v_source

                        u[row][column] = 0.25 * (
                                u[row + 1][column] + u[row - 1][column] + u[row][column + 1] + u[row][column - 1])
        return u


#potential_energy = LaplaceSolverPotentialEnergy()

#u = potential_energy.calculate_potential_energy()

#fig1 = plt.figure(2)
#plt.contourf(u)
#fig2 = plt.figure(3)
#plt.plot(u[int(70)])
#plt.show()
