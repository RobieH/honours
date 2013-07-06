import numpy as np
import matplotlib.pyplot as plt

i=plt.imread('farther2.png')
i=plt.imread('screw2.png')
i=plt.imread('screwfar2.png')
i=plt.imread('dice.png')
one=plt.imread('withObject1.png')
two=plt.imread('withoutObject1.png')
#i=one-two
#i=np.mean(i,2)

ifft=np.fft.ifftshift(np.real(np.fft.ifft2(i)))

plt.subplot(1,1,1)
plt.imshow(ifft)
plt.show()

'''
FFT1=(np.fft.fftshift(np.fft.fft2(i)))
IFFT1=np.real(np.fft.ifft2(np.fft.ifftshift(FFT1)))

plt.subplot(1,2,1)
plt.imshow(np.log(abs(FFT1))**2)
plt.subplot(1,2,2)
plt.imshow(IFFT1)
plt.show()
'''
