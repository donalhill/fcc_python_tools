import awkward1 as ak
import numpy as np

#Momentum
def calc_p(array, container, isFCCEDM=False):
    if(isFCCEDM):
        prefix = 'p4.p'
    else:
        prefix = 'momentum.'
    return np.sqrt(array[container,f'{prefix}x']**2 + array[container,f'{prefix}y']**2 + array[container,f'{prefix}z']**2)

#Transverse momentum
def calc_pt(array, container, isFCCEDM=False):
    if(isFCCEDM):
        prefix = 'p4.p'
    else:
        prefix = 'momentum.'
    return np.sqrt(array[container,f'{prefix}x']**2 + array[container,f'{prefix}y']**2)

#Pseudorapidity
def calc_eta(array, container, isFCCEDM=False):
    if(isFCCEDM):
        prefix = 'p4.p'
    else:
        prefix = 'momentum.'
    return np.arcsinh(array[container,f'{prefix}z'] / calc_pt(array, container, isFCCEDM))

#Theta
def calc_theta(array, container, isFCCEDM=False):
    eta = calc_eta(array,container, isFCCEDM)
    return 2 * np.arctan(np.exp(-eta))

#Phi
def calc_phi(array, container, isFCCEDM=False):
    if(isFCCEDM):
        prefix = 'p4.p'
    else:
        prefix = 'momentum.'
    return np.arccos(array[container,f'{prefix}x'] / calc_pt(array, container, isFCCEDM))

#Invariant mass for a list of particles, given a list of corresponding rest masses for each particle
def mass(particles, masses, isFCCEDM=False):
    if(isFCCEDM):
        prefix = 'p4.p'
    else:
        prefix = 'momentum.'

    for i in range(0,len(particles)):
        particles[i]['e'] = np.sqrt(particles[i]['p']**2 + masses[i]**2)

    tot_energy = particles[0]['e']
    tot_px = particles[0][f'{prefix}x']
    tot_py = particles[0][f'{prefix}y']
    tot_pz = particles[0][f'{prefix}z']

    for i in range(1,len(particles)):
        tot_energy = tot_energy + particles[i]['e']
        tot_px = tot_px + particles[i][f'{prefix}x']
        tot_py = tot_py + particles[i][f'{prefix}y']
        tot_pz = tot_pz + particles[i][f'{prefix}z']

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
