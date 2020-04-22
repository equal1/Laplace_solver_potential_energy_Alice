from Laplace_solver_cls import*

number_of_devices = 7
v_gate = 400
v_source = 0
max_iterations = 200
len_source = 40
width_source = 17
len_gate = 20
width_gate = 17
width_structure = 80
dx = 1
dy = 1




potential_energy = LaplaceSolverPotentialEnergy(number_of_devices, v_gate, v_source, max_iterations,
                                                len_source, width_source, len_gate, width_gate, width_structure, dx, dy)

u = potential_energy.calculate_potential_energy()

fig1 = plt.figure(1)
plt.contourf(u)
fig2 = plt.figure(2)
plt.plot(u[int(70)])
plt.show()