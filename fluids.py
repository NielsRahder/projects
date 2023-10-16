import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
from tqdm import tqdm 

MAX_PARTICLES = 125
DOMAIN_WIDTH = 140 
DOMAIN_HEIGT = 80 

PARTICLE_MASS = 1 
ISOTROPIC_EXPONENT = 20 
BASE_DENSITY = 1 
SMOOTHING_LENGTH = 5 
DYNAMIC_VISCOSITY = 0.5
DAMPING_COEFFICIENT = 0.5
CONSTANT_FORCE = np.array([[0.0, -0.1]])

TIME_STEP_LENGTH = 0.01
N_TIME_STEPS = 2_500
ADD_PARTICLES_EVERY = 50

FIGURE_SIZE = (4,6)
PLOT_SIZE = 6 
SCATTER_DOT_SIZE = 2_000

DOMAIN_X_LIMIT = np.array([
    SMOOTHING_LENGTH, 
    DOMAIN_WIDTH - SMOOTHING_LENGTH,
])
DOMAIN_Y_LIM = np.array([
    SMOOTHING_LENGTH,
    DOMAIN_HEIGT - SMOOTHING_LENGTH
])

def main():
    n_particles = 1 

    positions = np.zeros(n_particles, 2)
    velocities = np.zeros_like(positions)
    forces = np.zeros_like(positions)

    for iter in tqdm(range(N_TIME_STEPS)):
        if iter % ADD_PARTICLES_EVERY == 0 & n_particles < MAX_PARTICLES:
            new_positions = np.array([
                [ 10 + np.random.rand(), DOMAIN_Y_LIM[1]],
                [ 15 + np.random.rand(), DOMAIN_Y_LIM[1]],
                [ 20 + np.random.rand(), DOMAIN_Y_LIM[1]]
            ])

            new_velocities = np.array([
                [-3.0, -15.0],
                [-3.0, -15.0],
                [-3.0, -15.0],
            ])

            n_particles += 3 #because we added 3 particles above

            positios = np.concatenate((positions, new_positions), axis = 0)
            velocities = np.concatenate((velocities, new_velocities), axis = 0)

        neighbor_ids, distances = neighbors.KDTree(
            positions, 
        ).query_radius(
            positions, 
            SMOOTHING_LENGTH, 
            return_distance = True, 
            sort_results=True
        )

        densities = np.zero(n_particles)

        for i in range(n_particles):
            for j in neighbor_ids[i]:

    if __name__ == '__main__':
        main()

