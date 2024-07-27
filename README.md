<h1 align="center">Signals and Systems</h1>
<h6 align="center">Spring-2021 Signals and Systems Course Projects at Amirkabir University of Tech.</h6>


## Introduction
This repository includes all the practical projects of my Signals and Systems course.

### Project 1
This project aims at plotting various discrete and continuous signals and their transformations using the `scipy` and `numpy` libraries.
<p align="center">
  <img src="https://github.com/NegarMov/Signals-and-Systems/blob/master/SS%20-%20P01/figures/Screenshot%20(185).png" alt="Plotted Signals" width="400"/>
</p>

### Project 2
In this project a function is defined to compute the convolution of two signals. Furthermore, this function is tested using various discrete and continuous.
<p align="center">
  <img src="https://github.com/NegarMov/Signals-and-Systems/blob/master/SS%20-%20P02/figures/Figure_1.png" alt="Plotted Signals" width="400"/>
  <img src="https://github.com/NegarMov/Signals-and-Systems/blob/master/SS%20-%20P02/figures/Figure_2.png" alt="Plotted Signals" width="400"/>
</p>

### Project 3
In this project two main functions are implemented:
1. The Fourier series coefficients of the input signal are computed from `0` to `c`.
2. An estimated signal is reconstructed using the computed coefficients.
<p align="center">
  <img src="https://github.com/NegarMov/Signals-and-Systems/blob/master/SS%20-%20P03/figures/Figure_1.png" alt="Plotted Signals" width="500"/>
</p>

### Project 4
In this project a function is defined to compute the real part of the Fourier transform of the input signal. Furthermore, this function is tested using various continuous signals.
<p align="center">
  <img src="https://github.com/NegarMov/Signals-and-Systems/blob/master/SS%20-%20P04/figures/Fourier%20Transform.png" alt="Plotted Signals" width="500"/>
</p>

### Project 5
This project aims at practicing different sampling rates and finding an effective one to preserve important features of the signal.
<p align="center">
  <img src="https://github.com/NegarMov/Signals-and-Systems/blob/master/SS%20-%20P05/figures/Figure_2.png" alt="Plotted Signals" width="500"/>
</p>

### Final Project
This project has two main parts:
1. `Pt.1_Spectral Analysis.py`: In this part spectral analysis is utilized to ditinguish between the voices produced by male and female individuals. This method classifies the sample voices with a 100% accuracy.
<p align="center">
  <img src="https://github.com/NegarMov/Signals-and-Systems/blob/master/SS%20-%20Final%20Project/figures/v0_Figure.png" alt="Plotted Signals" width="400"/>
  <img src="https://github.com/NegarMov/Signals-and-Systems/blob/master/SS%20-%20Final%20Project/figures/v1_Figure.png" alt="Plotted Signals" width="400"/>
</p>
2. `Pt.2_Denoising.py`: This part applys spectral subtraction to denoise the speech files. In this approach the noise is first estimated in each of the STFT windows and then subtracted from it. Finally the denoised signal is reconstructed using iSTFT.
<p align="center">
  <img src="https://github.com/NegarMov/Signals-and-Systems/blob/master/SS%20-%20Final%20Project/figures/Figure_1.png" alt="Plotted Signals" width="500"/>
</p>
