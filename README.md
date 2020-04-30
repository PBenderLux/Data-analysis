# Data-analysis [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PBenderLux/Data-analysis/master)
A collection of python programs for the analysis of magnetization and scattering data of magnetic nanoparticle samples. 
This repository contains various examples from the following papers:  
[1] "Structural and magnetic properties of multi-core nanoparticles analysed using a generalised numerical inversion method" https://doi.org/10.1038/srep45990  
[2] "Distribution functions of magnetic nanoparticles determined by a numerical inversion method" https://doi.org/10.1088/1367-2630/aa73b4  
[3] "Relating Magnetic Properties and High Hyperthermia Performance of Iron Oxide Nanoflowers" https://doi.org/10.1021/acs.jpcc.7b11255  
[4] "Influence of clustering on the magnetic properties and hyperthermia performance of iron oxide nanoparticles" https://doi.org/10.1088/1361-6528/aad67d.
# Data Files
FSL-DCM_data.txt: Initial branch of the isothermal DC-magnetization (DCM) curve of sample FS-L from [4]. Column 1: magnetic field in [A/m], column 2: magnetization, column 3: measurement uncertainty.

FSL-SAXS_data.txt: Small-angle X-ray scattering (SAXS) measurement of sample FS-L from [4]. Column 1: scattering vector in [nm^-1], column 2: scattering intensity, column 3: measurement uncertainty.
# Notebooks
DCM-numerical_inversion: Jupyter notebook to extract the underlying moment distribution from the DC-magnetization curve.

SAXS-numerical_inversion: Jupyter notebook to extract the underlying pair distance distribution function from the SAXS measurement (i.e., indirect Fourier transform).
