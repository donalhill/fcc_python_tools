import awkward1 as ak
import numpy as np

#Momentum
def calc_p(array, container):
    return np.sqrt(array[container,'p4.px']**2 + array[container,'p4.py']**2 + array[container,'p4.pz']**2)

#Transverse momentum
def calc_pt(array, container):
    return np.sqrt(array[container,'p4.px']**2 + array[container,'p4.py']**2)

#Pseudorapidity
def calc_eta(array, container):
    return np.arcsinh(array[container,'p4.pz'] / calc_pt(array, container))

#Theta
def calc_theta(array, container):
    eta = calc_eta(array,container)
    return 2 * np.arctan(np.exp(-eta))

#Phi
def calc_phi(array, container):
    return np.arccos(array[container,'p4.px'] / calc_pt(array, container))

#Invariant mass for a list of particles, given a list of corresponding rest masses for each particle
def mass(particles, masses):
    for i in range(0,len(particles)):
        particles[i]['p4.e'] = np.sqrt(particles[i]['p4.p']**2 + masses[i]**2)

    tot_energy = particles[0]['p4.e']
    tot_px = particles[0]['p4.px']
    tot_py = particles[0]['p4.py']
    tot_pz = particles[0]['p4.pz']

    for i in range(1,len(particles)):
        tot_energy = tot_energy + particles[i]['p4.e']
        tot_px = tot_px + particles[i]['p4.px']
        tot_py = tot_py + particles[i]['p4.py']
        tot_pz = tot_pz + particles[i]['p4.pz']

    return np.sqrt(tot_energy**2 - tot_px**2 - tot_py**2 - tot_pz**2)

# Cosine of angle between two particles
def cos_angle(left, right):
    left_px_mag = left['p4.px'] / left['p4.p']
    left_py_mag = left['p4.py'] / left['p4.p']
    left_pz_mag = left['p4.pz'] / left['p4.p']

    right_px_mag = right['p4.px'] / right['p4.p']
    right_py_mag = right['p4.py'] / right['p4.p']
    right_pz_mag = right['p4.pz'] / right['p4.p']

    return left_px_mag*right_px_mag + left_py_mag*right_py_mag + left_pz_mag*right_pz_mag
