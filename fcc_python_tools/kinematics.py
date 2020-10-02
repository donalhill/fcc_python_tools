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

#Invariant mass of 2 particles
def mass_2body(left, right, left_mass, right_mass):
    left_energy = np.sqrt(left['p4.p']**2 + left_mass**2)
    right_energy = np.sqrt(right['p4.p']**2 + right_mass**2)
    return np.sqrt(((left_energy + right_energy)**2 -
            (left['p4.px'] + right['p4.px'])**2 -
            (left['p4.py'] + right['p4.py'])**2 -
            (left['p4.pz'] + right['p4.pz'])**2))

#Invariant mass of 3 particles
def mass_3body(a, b, c, a_mass, b_mass, c_mass):
    a_energy = np.sqrt(a['p4.p']**2 + a_mass**2)
    b_energy = np.sqrt(b['p4.p']**2 + b_mass**2)
    c_energy = np.sqrt(c['p4.p']**2 + c_mass**2)
    return np.sqrt(((a_energy + b_energy + c_energy)**2 -
            (a['p4.px'] + b['p4.px'] + c['p4.px'])**2 -
            (a['p4.py'] + b['p4.py'] + c['p4.py'])**2 -
            (a['p4.pz'] + b['p4.pz'] + c['p4.pz'])**2))

#Invariant mass of 4 particles
def mass_4body(a, b, c, d, a_mass, b_mass, c_mass, d_mass):
    a_energy = np.sqrt(a['p4.p']**2 + a_mass**2)
    b_energy = np.sqrt(b['p4.p']**2 + b_mass**2)
    c_energy = np.sqrt(c['p4.p']**2 + c_mass**2)
    d_energy = np.sqrt(d['p4.p']**2 + d_mass**2)
    return np.sqrt(((a_energy + b_energy + c_energy + d_energy)**2 -
            (a['p4.px'] + b['p4.px'] + c['p4.px'] + d['p4.px'])**2 -
            (a['p4.py'] + b['p4.py'] + c['p4.py'] + d['p4.py'])**2 -
            (a['p4.pz'] + b['p4.pz'] + c['p4.pz'] + d['p4.pz'])**2))

# Cosine of angle between two particles
def cos_angle(left, right):
    left_px_mag = left['p4.px'] / left['p4.p']
    left_py_mag = left['p4.py'] / left['p4.p']
    left_pz_mag = left['p4.pz'] / left['p4.p']

    right_px_mag = right['p4.px'] / right['p4.p']
    right_py_mag = right['p4.py'] / right['p4.p']
    right_pz_mag = right['p4.pz'] / right['p4.p']

    return left_px_mag*right_px_mag + left_py_mag*right_py_mag + left_pz_mag*right_pz_mag
