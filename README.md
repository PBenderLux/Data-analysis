# Data-analysis [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PBenderLux/Data-analysis/master)
A collection of python 3 programs (Jupyter notebooks) for the analysis of magnetization and scattering data of magnetic nanoparticle samples. When you encouter problems, need help running the problems or want to discuss your results do not hesitate to contact me.

The programs can be run without downloading anything in an executable environment using mybinder.org by clicking on the link above (note: seems to work best with Firefox or Edge, I personally have problems when using Chrome). However, the loading may take quite long and the computational speed is very slow. Thus, I recommend to download the repository and to run the notebooks directly on your own computer. The following link provides all the necessary information on how to execute jupyter notebooks: https://jupyter.readthedocs.io/en/latest/tryjupyter.html \
When you are new to python I recommend to first install Anaconda which conveniently installs Python, the Jupyter Notebook, and other commonly used packages for scientific computing and data science: https://www.anaconda.com/products/individual

This repository is subdivided into two different folders. 
The first folder **1 Inverse problems** contains examples published in:  
[1] P. Bender et al., Sci. Rep. 7 (2017) 45990 https://doi.org/10.1038/srep45990 \
"Structural and magnetic properties of multi-core nanoparticles analysed using a generalised numerical inversion method"\
[2] P. Bender et al., New J. Phys. 19 (2017) 073012 https://doi.org/10.1088/1367-2630/aa73b4 \
"Distribution functions of magnetic nanoparticles determined by a numerical inversion method"\
[3] P. Bender et al., J. Phys. Chem C. 122 (2018) 3068-3077 https://doi.org/10.1021/acs.jpcc.7b11255 \
"Relating Magnetic Properties and High Hyperthermia Performance of Iron Oxide Nanoflowers"\
[4] P. Bender et al., Nanotechnology 29 (2018) 425705 https://doi.org/10.1088/1361-6528/aad67d \
"Influence of clustering on the magnetic properties and hyperthermia performance of iron oxide nanoparticles"\
[5] P. Bender et al., Phys. Rev. B 98 (2018) 224420 https://doi.org/10.1103/PhysRevB.98.224420 \
"Dipolar-coupled moment correlations in clusters of magnetic nanoparticles" \
[6] P. Bender et al., Acta Cryst. A75 (2019) 766-771 https://doi.org/10.1107/S205327331900891X \
"Using the singular value decomposition to extract 2D correlation functions from scattering patterns" \
[7] P. Bender & J. Leliaert et al., Small Science 1 (2021) 2000003 https://doi.org/10.1002/smsc.202000003 \
"Unraveling nanostructured spin textures in bulk magnets"

The second folder **2 Bayesian analysis** contains examples published in: \
[8] M. Bersweiler et al., Nanotechnology 31 (2020) 435704 https://doi.org/10.1088/1361-6528/aba57b \
"The benefits of a Bayesian analysis for the characterization of magnetic nanoparticles"

# 1 Inverse problems
# data
**MC-DCM_data.txt**: Initial branch of the isothermal DC-magnetization (DCM) curve of the colloidal dispersion of multicore (MC) particles from [1]. column 1: magnetic field in [A/m], column 2: magnetization, column 3: measurement uncertainty.

**SC-SAXS_data.txt**: Small-angle X-ray scattering (SAXS) measurement of the dispersion of iron oxide single cores (SC) from [2]. column 1: scattering vector in [1/nm], column 2: scattering intensity, column 3: measurement uncertainty.

**NF-ACS_data.txt**: AC scusceptibility (ACS) data of the nanoflower (NF) sample from [3]. column 1: rotational frequency in [rad/s], column 2/3: real part of the complex susceptibility/measurement uncertainty, column 4/5: real part of the complex susceptibility/measurement uncertainty (we assumed constant values for the measurement uncertainties).

**FSL-DCM_data.txt**: Initial branch of the isothermal DC-magnetization (DCM) curve of sample FS-L from [4]. column 1: magnetic field in [A/m], column 2: magnetization, column 3: measurement uncertainty.

**FSL-SAXS_data.txt**: Small-angle X-ray scattering (SAXS) measurement of sample FS-L from [4]. column 1: scattering vector in [1/nm], column 2: scattering intensity, column 3: measurement uncertainty.

**NC-SANS_data.txt**: Magnetic small-angle neutron scattering (SANS) measurement of a sample of magnetic nanoparticle clusters from [5]. column 1: scattering vector in [1/nm], column 2: purely magnetic scattering intensity, column 3: measurement uncertainty.

**MTB_2DSAXS_data.txt**: 2D small-angle X-ray scattering (SAXS) pattern of a colloidal dispersion of aligned magnetotactic bacteria (MTB) in polar coordinates from [6]. column 1: angle theta between scattering vector q and alignment direction (from 0° to 180°), column 2: magnitude of scattering vector q in [1/nm], column 3: scattering intensity.

**Nanoperm_2DSANS_data.txt**: 2D magnetic small-angle neutron scattering (SANS) pattern of the nanocrystalline ferromagnet Nanoperm from [7]. column 1: angle theta between scattering vector q and alignment direction (from 0° to 180°), column 2: magnitude of scattering vector q in [1/nm], column 3: residual magnetic scattering intensity.

# notebooks
**DCM-numerical_inversion-MC**: Jupyter notebook to extract the underlying moment distribution from the DC-magnetization curve MC-DCM_data.txt from [1] (basically identical to DCM-numerical_inversion).

**SAXS-numerical_inversion-sphere**: Jupyter notebook to extract the underlying particle size distribution from the SAXS measurement SC-SAXS_data.txt assuming spherical particle shape from [2].

**ACS-numerical_inversion**: Jupyter notebook to extract the underlying relaxation time distribution function from the ACS measurement NF-ACS_data.txt from [3].

**DCM-numerical_inversion**: Jupyter notebook to extract the underlying moment distribution from the DC-magnetization curve FSL-DCM_data.txt from [4] (basically identical to DCM-numerical_inversion-MC).

**SAXS-numerical_inversion**: Jupyter notebook to extract the underlying pair distance distribution function from the SAXS measurement FSL-SAXS_data.txt (i.e., an indirect Fourier transform) from [4] (basically identical to SANS-numerical_inversion).

**SANS-numerical_inversion**: Jupyter notebook to extract the underlying pair distance distribution function from the magnetic SANS measurement NC-SANS_data.txt from [5] (basically identical to SAXS-numerical_inversion).

**SAXS-2D_SVD**: Jupyter notebook to extract the underlying 2D pair distance distribution function from the 2D SAXS pattern MTB_2DSAXS_data.txt by a singular value decoposition (SVD, truncated and standard SVD) from [6].

**SANS-2D_experiment_Kaczmarz**: Jupyter notebook to extract the underlying 2D (magnetic) pair distance distribution function from the 2D (magnetic) SANS pattern Nanoperm_2DSANS_data.txt by the Kaczmarz algorithm from [7].

# 2 Bayesian analysis
# data
**Magnetization_data.txt**: First branch from 5 to -5 T of the isothermal DC-magnetization (DCM) curve of the powder sample of superparamagnetic core-shell nanoparticles (iron oxide cores with a thick silica shells) from [8]. column 1: magnetic field in [T], column 2: magnetization in [Am^2/kg_Fe]. 

**SANS-0.002/0.1/1/5T_data.txt**: Field-dependent nuclear-magnetic cross term of the SANS intensity of the superparamagnetic core-shell nanoparticles (iron oxide cores with a thick silica shells) from [8]. column 1: scattering vector in [1/nm], column 2: scattering intensity in [arb. units], column 3: measurement uncertainty.

# notebooks
**DCM-Langevin-Bayes_fit**: Jupyter notebook in which the DCM measurement Magnetization_data.txt is fitted with the Langevin function under assumption of lognormal size distributions for core and total particle size. First, a standard least-squares fit is performed and then the fit results are used as starting values for the Bayesian refinement.

**SANS-CoreShell-Bayes_fit**: Jupyter notebook in which the nuclear-magnetic cross term SANS-5T_data.txt is fitted with a form factor model for core-shell spheres under assumption of a homogeneous magnetization of the core and lognormal size distributions for the core and the total particle size. First, a standard least-squares fit is performed and then the fit results are used as starting values for the Bayesian refinement.

**SANS-CoreShell_Bayes_global_fit**: Jupyter notebook in which all four field-dependent nuclear-magnetic cross terms SANS-0.002/0.1/1/5T_data.txt are fitted globally with a form factor model for core-shell spheres under assumption of a homogeneous magnetization of the core and lognormal size distributions for the core and the total particle size. First, a standard least-squares fit is performed and then the fit results are used as starting values for the Bayesian refinement.

**SANS+DCM-Bayes_global_fit**: Jupyter notebook in which the DCM measurement Magnetization_data.txt and the four field-dependent nuclear-magnetic cross terms SANS-0.002/0.1/1/5T_data.txt are fitted with the same models as before but together (i.e. globally). First, a standard least-squares fit is performed and then the fit results are used as starting values for the Bayesian refinement.
