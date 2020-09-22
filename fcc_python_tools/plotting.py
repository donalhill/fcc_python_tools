from fcc_python_tools.locations import loc
import matplotlib.pyplot as plt
import numpy as np
import awkward1 as ak

def errorbar_hist(P,var,P_name,title,low,high):
    fig, ax = plt.subplots(figsize=(8,8))
    #Number of events, use this to determine bins and thus bin width
    n = np.sum(ak.num(P))
    bins = int(np.sqrt(n))
    bin_w = (high - low)/bins

    counts, bin_edges = np.histogram(ak.to_list(ak.flatten(P[var])), bins, range=(low,high))
    bin_centres = (bin_edges[:-1] + bin_edges[1:])/2.
    err = np.sqrt(counts)
    plt.errorbar(bin_centres, counts, yerr=err, fmt='o', color='k')
    plt.xlabel(title,fontsize=30)
    plt.ylabel("Candidates / (%.4f GeV/$c^2$)" % bin_w,fontsize=30)
    plt.xlim(low,high)
    ax.tick_params(axis='both', which='major', labelsize=25)
    ymin, ymax = plt.ylim()
    plt.ylim(0.,ymax*1.1)
    plt.tight_layout()
    plt.show()
    fig.savefig(f"{loc.PLOTS}/{P_name}_{var}.pdf")
