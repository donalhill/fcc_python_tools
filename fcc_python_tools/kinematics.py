import awkward1 as ak
import numpy as np

#Momentum
def calc_p(array, container):
    return np.sqrt(array[container,'momentum.x']**2 + array[container,'momentum.y']**2 + array[container,'momentum.z']**2)

#Transverse momentum
def calc_pt(array, container):
    return np.sqrt(array[container,'momentum.x']**2 + array[container,'momentum.y']**2)

#Pseudorapidity
def calc_eta(array, container):
    return np.arcsinh(array[container,'momentum.z'] / calc_pt(array, container))

#Theta
def calc_theta(array, container):
    eta = calc_eta(array,container)
    return 2 * np.arctan(np.exp(-eta))

#Phi
def calc_phi(array, container):
    return np.arccos(array[container,'momentum.x'] / calc_pt(array, container))

#Invariant mass for a list of particles, given a list of corresponding rest masses for each particle
def mass(particles, masses):
    for i in range(0,len(particles)):
        particles[i]['e'] = np.sqrt(particles[i]['p']**2 + masses[i]**2)

    tot_energy = particles[0]['e']
    tot_px = particles[0]['momentum.x']
    tot_py = particles[0]['momentum.y']
    tot_pz = particles[0]['momentum.z']

    for i in range(1,len(particles)):
        tot_energy = tot_energy + particles[i]['e']
        tot_px = tot_px + particles[i]['momentum.x']
        tot_py = tot_py + particles[i]['momentum.y']
        tot_pz = tot_pz + particles[i]['momentum.z']

    return np.sqrt(tot_energy**2 - tot_px**2 - tot_py**2 - tot_pz**2)

# Cosine of angle between two particles
def cos_angle(left, right):
    left_px_mag = left['momentum.x'] / left['p']
    left_py_mag = left['momentum.y'] / left['p']
    left_pz_mag = left['momentum.z'] / left['p']

    right_px_mag = right['momentum.x'] / right['p']
    right_py_mag = right['momentum.y'] / right['p']
    right_pz_mag = right['momentum.z'] / right['p']

    return left_px_mag*right_px_mag + left_py_mag*right_py_mag + left_pz_mag*right_pz_mag
