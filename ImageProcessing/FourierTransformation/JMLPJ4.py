#Jeremy Lynch

#Utilizes OpenCV-Python to read in and show images.
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Get original image and convert to GS
img = cv2.imread('building.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Perform Fourier transformation on input image
FFT1 = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
FFT1_shift = np.fft.fftshift(FFT1)
mag_spec = 20*np.log(cv2.magnitude(FFT1_shift[:,:,0],FFT1_shift[:,:,1]))

#Display Input Image
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(mag_spec, cmap = 'gray')

#Display FFT1 Spacial Image
plt.title('Magnitude Spectrum FFT1'), plt.xticks([]), plt.yticks([])
plt.show()

#Get Conjugate of FFT1
FFT2 = np.ones_like(FFT1)
FFT2 = cv2.mulSpectrums(FFT1, FFT2, 0, True)

#Display FFT1 for comparison
plt.subplot(121),plt.imshow(mag_spec, cmap = 'gray')
plt.title('Magnitude Spectrum FFT1'), plt.xticks([]), plt.yticks([])

#Display FFT2 Spacial Image
mag_spec2 = 20*np.log(cv2.magnitude(FFT2[:,:,0],FFT2[:,:,1]))
plt.subplot(122),plt.imshow(mag_spec2, cmap = 'gray')
plt.title('Magnitude Spectrum FFT2'), plt.xticks([]), plt.yticks([])
plt.show()

#Set FFT3 center 50 radius to 0 
width = len(img) / 2 - 1
length = len(img[0]) / 2 - 1
FFT3 = np.copy(img)
FFT3[int(width - 49): int(width + 49), int(length - 49): int(length + 49)] = 0

#Display FFT3
plt.subplot(121),plt.imshow(FFT3, cmap = 'gray')
plt.title('FFT3'), plt.xticks([]), plt.yticks([])

#Transform FFT3
FFT3 = cv2.dft(np.float32(FFT3), flags = cv2.DFT_COMPLEX_OUTPUT)
FFT3_shift = np.fft.fftshift(FFT3)

#Display FFT3 Spatial Image
mag_spec3 = 20*np.log(cv2.magnitude(FFT3_shift[:,:,0],FFT3_shift[:,:,1]))
plt.subplot(122),plt.imshow(mag_spec3, cmap = 'gray')
plt.title('Magnitude Spectrum FFT3'), plt.xticks([]), plt.yticks([])
plt.show()

#Find FFT4
FFT4 = np.copy(img)
FFT4[:, :int(length - 49)] = 0
FFT4[:, int(length + 49):] = 0
FFT4[:int(width - 49), :] = 0
FFT4[int(width + 49):, :] = 0

#Display FFT4
plt.subplot(121),plt.imshow(FFT4, cmap = 'gray')
plt.title('FFT4'), plt.xticks([]), plt.yticks([])

#Get Conjugate of FFT4
FFT4 = cv2.dft(np.float32(FFT4), flags = cv2.DFT_COMPLEX_OUTPUT)
FFTemp = np.ones_like(FFT4)
FFT4 = cv2.mulSpectrums(FFTemp, FFT4, 0, True)

#Display FFT4 Spacial Image
mag_spec4 = 20*np.log(cv2.magnitude(FFT4[:,:,0],FFT4[:,:,1]))
plt.subplot(122),plt.imshow(mag_spec4, cmap = 'gray')
plt.title('Magnitude Spectrum FFT4'), plt.xticks([]), plt.yticks([])
plt.show()




