#==============================================================================
# Import of used packages
from numpy.linalg import slogdet
import numpy as np
import pylab as py
from scipy.optimize import nnls
#==============================================================================
# Import of the data (field in [A/m])

H,m,sd=np.genfromtxt("../data/FSL_data.txt", unpack=True, usecols = (0, 1, 2), skip_header=0, skip_footer=0)
        
mu0 = np.pi*4e-7 # Vacuum permeability [V*s/(A*m)]
T = 298.15 # Temperature [K]
kb = 1.38e-23 # Boltzmann constant [J/K]
NH=len(H)

#==============================================================================
# Definition of moment distribution

N=100# number of points of moment distribution
muList = np.logspace(-22,-14,N)   # Moment distrbution with lognormal spacing

#==============================================================================
# generate list for regularization parameter a

Na=100
aList=np.logspace(-4,4,Na)

#==============================================================================
# Plot data

py.errorbar(H,m,sd,color='r',marker='.',ls='None',label='Observed')
py.show()
print('Figure 1: data')   

#==============================================================================
# regularization matrices

L=0.5*(-1*np.eye(N,k=-1)+2*np.eye(N,k=0)-1*np.eye(N,k=1))
L[0,1] = 0
L[N-1,N-2] = 0

#==============================================================================
# Definition of function to generate the system matrix

def Aij(H, mu): # Langevin function
    y= (1/(np.tanh(mu*mu0*H/(kb*T)))-1/(mu*mu0*H/(kb*T)))
    return y

def trans(H,mu): # function to generate the transfer matrix
    A=[]
    for j in range(len(H)):
        A.append([np.sign(H[j]) * Aij(abs(H[j]), mu[i]) for i in range(len(mu))])
    return A 

K = trans(H, muList) # Transfer matrix is determined
K=np.asarray(K) 

#==============================================================================
# Inversion of data
     
evList=[] 
prList=[]   

for ai in range(len(aList)):                              
    sd_sq   = pow(sd,2)         
    sdnorm  = 1/sd            
    sdnorm = NH * sdnorm/sdnorm.sum()
    sdmat = np.diag(sdnorm)
    sdcol  = sdnorm[:,np.newaxis]            

    M = m.dot(sdmat) # normalize data by sigma
    M2 = m
    
    # stacking of matrices            
    C = np.vstack([K*sdcol,np.sqrt(2*aList[ai])*L]) 
    X = np.hstack([M, np.zeros(N)]) 
    B = (K.T).dot(K*pow(sdcol,2))               
    
    # Fit: non-negative constraint
    sol1,resnorm=nnls(C,X)    
    pr=sol1
    
    # determine chisquare            
    Ifit=K.dot(pr)    
    chisq=(pow(M2-Ifit,2)/sd_sq).sum()              

    # calculation of evidence
    S=sum(pow(L.dot(pr),2))
    Lsq=pow(L,2)
    U=2*Lsq+B/aList[ai] 
    detsign,rlogdet=slogdet(U)
    G=-aList[ai]*S-0.5*chisq            
    evidence=(G-0.5*rlogdet) # log of evidence    
        
    evList.append(evidence)       
    prList.append(pr)        

MAX=evList.index(max(evList)) # find maximal evidence
prM=prList[MAX]

prList2=np.reshape(prList,(Na,N))         

H0=np.logspace(1,7,100)
KM0 = trans(H0, muList)
KM0 = np.asarray(KM0)
fitM=KM0.dot(prM) 

#==============================================================================
# Plots

py.plot(muList,prM)
py.xscale('log')
py.show()
print('Figure 2: moment distribution prM')

py.figure()
for i in range(Na):
    py.xscale('log')
    py.plot(muList, prList2[i, :])
py.show()  
print('Figure 3: all distributions')
    
py.errorbar(H,m,sd,color='r',marker='.',ls='None',label='Observed')
py.plot(H0,fitM)
py.xscale('log')
py.axis([10**1,10**7,0,110])
py.show()
print('Figure 4: Data (red points) and fit (blue line)')

py.plot(aList,evList,'k+')
py.xscale('log')
py.show()
print('Figure 5: evidence vs alpha.')