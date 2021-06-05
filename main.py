import matplotlib.pyplot as plt
import numpy as np
from google.colab import drive
drive.mount('/content/drive')
img=plt.imread('/content/drive/MyDrive/craniu_02.bmp')

plt.figure()
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()

def rgb2gri(img_in, format):
   img_in = img_in.astype('float')
   s = img_in.shape
   if len(s) == 3 and s[2] == 3:
       if format == 'png':
           img_out = (0.299 * img_in[:, :, 0] + 0.587 * img_in[:, :, 1] + 0.114 * img_in[:, :, 2]) * 255
       elif format == 'bmp':
           img_out = 0.299 * img_in[:, :, 0] + 0.587 * img_in[:, :, 1] + 0.114 * img_in[:, :, 2]
       img_out = np.clip(img_out, 0, 255)
       ing_out = img_out.astype('uint8')
       return ing_out
   else:
       print('Conversia nu a putut fi realizata deoarece imaginea de intrare nu este color')
       return img_in

gray = rgb2gri(img, 'bmp')
plt.figure('Figura nivele de gri')
plt.imshow(gray, cmap='gray', vmin=0, vmax=255)
plt.show()

# functie putere
def putere(img,r):
  img_putere=255*((img/255)**r)
  return img_putere
img2=putere(img,3)

plt.figure('Functie putere')
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.show()



