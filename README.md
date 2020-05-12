# Data-analysis[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PBenderLux/Data-analysis/master)
A collection of python programs (Jupyter notebooks) for the analysis of magnetization and scattering data of magnetic nanoparticle samples. \
The programs can be run without downloading anything in a executable environment using mybinder.org by clicking on the link above. However, the computational time is very low, therefore, I recommend to download the repository and to run the notebooks on your own computer. The following link provides all the necessary information on how to execute jupyter notebooks: https://jupyter.readthedocs.io/en/latest/install.html#install

The repository contains examples published in the following papers:  
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
"Using the singular value decomposition to extract 2D correlation functions from scattering patterns"

# Data Files
**MC-DCM_data.txt**: Initial branch of the isothermal DC-magnetization (DCM) curve of the colloidal dispersion of multicore (MC) particles from [1]. column 1: magnetic field in [A/m], column 2: magnetization, column 3: measurement uncertainty.

**SC-SAXS_data.txt**: Small-angle X-ray scattering (SAXS) measurement of the dispersion of iron oxide single cores (SC) from [2]. column 1: scattering vector in [1/nm], column 2: scattering intensity, column 3: measurement uncertainty.

**NF-ACS_data.txt**: AC scusceptibility (ACS) data of the nanoflower (NF) sample from [3]. column 1: rotational frequency in [rad/s], column 2/3: real part of the complex susceptibility/measurement uncertainty, column 4/5: real part of the complex susceptibility/measurement uncertainty (we assumed constant values for the measurement uncertainties).

**FSL-DCM_data.txt**: Initial branch of the isothermal DC-magnetization (DCM) curve of sample FS-L from [4]. column 1: magnetic field in [A/m], column 2: magnetization, column 3: measurement uncertainty.

**FSL-SAXS_data.txt**: Small-angle X-ray scattering (SAXS) measurement of sample FS-L from [4]. column 1: scattering vector in [1/nm], column 2: scattering intensity, column 3: measurement uncertainty.

**NC-SANS_data.txt**: Magnetic small-angle neutron scattering (SANS) measurement of a sample of magnetic nanoparticle clusters from [5]. column 1: scattering vector in [1/nm], column 2: purely magnetic scattering intensity, column 3: measurement uncertainty.

**MTB_2DSAXS_data.txt**: 2D small-angle X-ray scattering (SAXS) pattern of a colloidal dispersion of aligned magnetotactic bacteria (MTB) in polar coordinates from [6]. column 1: angle theta between scattering vector q and alignment direction (from 0° to 180°), column 2: magnitude of scattering vector q in [1/nm], column 3: scattering intensity.

# Notebooks
**DCM-numerical_inversion-MC**: Jupyter notebook to extract the underlying moment distribution from the DC-magnetization curve MC-DCM_data.txt (basically identical to DCM-numerical_inversion) from [1].

**SAXS-numerical_inversion-sphere**: Jupyter notebook to extract the underlying particle size distribution from the SAXS measurement SC-SAXS_data.txt assuming spherical particle shape from [2].

**ACS-numerical_inversion**: Jupyter notebook to extract the underlying relaxation time distribution function from the ACS measurement NF-ACS_data.txt from [3].

**DCM-numerical_inversion**: Jupyter notebook to extract the underlying moment distribution from the DC-magnetization curve FSL-DCM_data.txt (basically identical to DCM-numerical_inversion-MC) from [4].

**SAXS-numerical_inversion**: Jupyter notebook to extract the underlying pair distance distribution function from the SAXS measurement FSL-SAXS_data.txt (i.e., an indirect Fourier transform) from [4].

**SANS-numerical_inversion**: Jupyter notebook to extract the underlying pair distance distribution function from the magnetic SANS measurement NC-SANS_data.txt (basically identical to SAXS-numerical_inversion) from [5].

**SAXS-2D_SVD**: Jupyter notebook to extract the underlying 2D pair distance distribution function from the 2D SAXS pattern MTB_2DSAXS_data.txt by a singular value decoposition (SVD, truncated and standard SVD) from [6].
