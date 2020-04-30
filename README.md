# Data-analysis [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PBenderLux/Data-analysis/master)
A collection of python programs (Jupyter notebooks) for the analysis of magnetization and scattering data of magnetic nanoparticle samples. 
This repository contains examples published in the following papers:  
[1] "Structural and magnetic properties of multi-core nanoparticles analysed using a generalised numerical inversion method"\
https://doi.org/10.1038/srep45990  
[2] "Distribution functions of magnetic nanoparticles determined by a numerical inversion method"\
https://doi.org/10.1088/1367-2630/aa73b4  
[3] "Relating Magnetic Properties and High Hyperthermia Performance of Iron Oxide Nanoflowers"\
https://doi.org/10.1021/acs.jpcc.7b11255  
[4] "Influence of clustering on the magnetic properties and hyperthermia performance of iron oxide nanoparticles"\
https://doi.org/10.1088/1361-6528/aad67d.
# Data Files
**MC-DCM_data.txt**: Initial branch of the isothermal DC-magnetization (DCM) curve of the colloidal dispersion of multicore (MC) particles from [1]. column 1: magnetic field in [A/m], column 2: magnetization, column 3: measurement uncertainty.

**SC-SAXS_data.txt**: Small-angle X-ray scattering (SAXS) measurement of the dispersion of iron oxide single cores (SC) from [2]. column 1: scattering vector in [1/nm], column 2: scattering intensity, column 3: measurement uncertainty.

**NF-ACS_data.txt**: AC scusceptibility (ACS) data of the nanoflower (NF) sample from [3]. column 1: rotational frequency in [rad/s], column 2/3: real part of the complex susceptibility/measurement uncertainty, column 4/5: real part of the complex susceptibility/measurement uncertainty (we assumed constant values for the measurement uncertainties).

**FSL-DCM_data.txt**: Initial branch of the isothermal DC-magnetization (DCM) curve of sample FS-L from [4]. column 1: magnetic field in [A/m], column 2: magnetization, column 3: measurement uncertainty.

**FSL-SAXS_data.txt**: Small-angle X-ray scattering (SAXS) measurement of sample FS-L from [4]. column 1: scattering vector in [1/nm], column 2: scattering intensity, column 3: measurement uncertainty.

# Notebooks
**DCM-numerical_inversion-MC**: Jupyter notebook to extract the underlying moment distribution from the DC-magnetization curve MC-DCM_data.txt (basically identical to DCM-numerical_inversion).

**SAXS-numerical_inversion-sphere**: Jupyter notebook to extract the underlying particle size distribution from the SAXS measurement SC-SAXS_data.txt assuming spherical particle shape.

**ACS-numerical_inversion**: Jupyter notebook to extract the underlying relaxation time distribution function from the ACS measurement NF-ACS_data.txt.

**DCM-numerical_inversion**: Jupyter notebook to extract the underlying moment distribution from the DC-magnetization curve FSL-DCM_data.txt (basically identical to DCM-numerical_inversion-MC).

**SAXS-numerical_inversion**: Jupyter notebook to extract the underlying pair distance distribution function from the SAXS measurement FSL-SAXS_data.txt (i.e., an indirect Fourier transform).
