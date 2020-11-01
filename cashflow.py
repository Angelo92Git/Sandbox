import numpy as np

def create_annuity(amt, periods, start=0, stop=0):
    annuity = np.append(np.zeros(start),np.ones(stop-start)*amt)
    annuity = np.append(np.zeros(stop-periods),np.ones(periods)*amt)
    annuity = np.append(np.zeros(start),np.ones(periods)*amt)
    return annuity

def InstVal(annuity, ir, t=0):
    annuity[0:t]
    annuity[t+1:len(annuity)]



print(np.ones(5))
