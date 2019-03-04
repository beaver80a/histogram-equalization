import numpy as np
from scipy.misc import imresize 
import matplotlib.pyplot as plt
from imageio import imread, imsave  
import time 


curntTime=time.time()

#Enter the number of bits
Bits= 8

L=list(range(2**Bits))

#length of L
OriginalLenOfL = len(L)
LenOfL = len(L)-1

im1 = plt.imread('C:\\Users\\Gaming\\Desktop\\test.jpg')

x = im1.shape[0]
y = im1.shape[1]

im2=np.zeros([x,y], dtype=np.uint8)
im3=np.zeros([x,y], dtype=np.uint8)
im4=np.zeros([x,y], dtype=np.uint8)

# frequency OF the Pixle 
freqOfClr=np.zeros(OriginalLenOfL)

# probability of frequency 
ProbOfFreq=np.zeros(OriginalLenOfL)

C=np.zeros(OriginalLenOfL)

CbyLengthOfL=np.zeros(OriginalLenOfL,dtype=np.uint8)


MN=x*y

        
        
#to gray image
for i in range(x):
    for j in range(y):
        gray=int((im1[i,j,0]*0.21 +im1[i,j,1]*0.72+im1[i,j,2]*0.07))
        im2[i,j]=gray
        avgpixl=int(round(gray%LenOfL))
        im3[i,j]=avgpixl
        freqOfClr[avgpixl]=freqOfClr[avgpixl]+1
        
plt.imshow(im3,cmap='gray')


#ايجاد نسبة كل بكسل
for i in range(OriginalLenOfL):
    ProbOfFreq[i]=freqOfClr[i]/MN
    C[0]=ProbOfFreq[0]
    if i>=1:
        C[i]=ProbOfFreq[i]+C[i-1]
            



for i in range(OriginalLenOfL):
    CbyLengthOfL[i]=round(C[i]*LenOfL)



for i in range(x):
    for j in range(y):
        t=im3[i,j]
        im4[i,j]=CbyLengthOfL[t]

            






print('Gray Image')
plt.imshow(im2,cmap='gray')
plt.show()

print('Image after applying '+str(Bits)+' Bits')
plt.imshow(im3,cmap='gray')
plt.show()

print('Image after Histogram Equalization' )
plt.imshow(im4,cmap='gray')
plt.show()
            
endTime=time.time()


print(endTime-curntTime)
