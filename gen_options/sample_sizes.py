import sys,os
import json

#Production rates in Pythia e+ e- -> Z0 -> f fbar
prod_fracs = {"Bu": 0.43,
              "Bd": 0.43,
              "Bs": 0.096,
              "Bc": 0.0004*10, #actual production is 10x lower than this, so we will get 10x less than N below
              "Tau": 1.,
              "D": 0.43
             }

modes = {"Bu2D0Pi": "Bu",
         "Bd2KstTauTau": "Bd",
         "Bs2TauTau": "Bs",
         "Bd2MuMu": "Bd",
         "Bd2DstTauNu": "Bd",
         "Bd2DTauNu": "Bd",
         "Bd2KstEE": "Bd",
         "Bc2TauNu": "Bc",
         "BdKstNuNu": "Bd",
         "Bs2PhiGamma": "Bs",
         "Tau2MuMuMu": "Tau",
         "Tau2MuGamma": "Tau",
         "Bd2KsPi0": "Bd",
         "D2PiPi0": "D"
         }

#Number of signal events required
N = 100000.

sample_sizes = {}

for m in modes:
    print(m)

    prod_frac = 0.
    for p in prod_fracs:
        if(p == modes[m]):
            prod_frac = prod_fracs[p]

    n = N/prod_frac
    sample_sizes[m] = round(n, -3)

with open("sample_sizes.json","w") as f:
    json.dump(sample_sizes, f)
