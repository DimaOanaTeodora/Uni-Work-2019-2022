import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# Citire imagine
image = cv.imread("butterfly.jpeg") #Dimensiunea: H W 3(RGB)
image2 = cv.imread("butterfly.jpeg", cv.IMREAD_GRAYSCALE) #Dimensiunea: H W 

# Extragere dimensiuni
H, W, R = image.shape
print("Dimensiuni: ", H,W,R, sep=" ")

H2, W2 = image2.shape
print("Dimensiuni: ", H,W)

# Afisare imagine
'''
cv.imshow("windowName", image)
cv.waitKey(0) # se asteapta apasarea unei taste ca sa dispara imaginea
cv.imshow("windowName", image2)
cv.waitKey(0) # se asteapta apasarea unei taste ca sa dispara imaginea
cv.destroyAllWindows()
'''
# Resize
imgResize = cv.resize(image, (100, 100)); #resize la 100 x 100

# ------ Exercitiul 1.6 Matrice de intensitati-------

# Citire color si convertire la gri
img = cv.resize(cv.cvtColor(cv.imread("football.jpg"), cv.COLOR_BGR2GRAY),
                (100, 100)); #resize la 100 x 100
# cv.imshow("Football",img)
# cv.waitKey(0)

# Sortare imagine in vectorul x(1, 10 000) + plotare

# Nu pot sa sortez o matrice am nevoie de un vector
v=img.flatten() # transforma din matrice in vector 
print("Valori pixeli matrice-> vector: ", v)
# Sortare pixeli
x=np.sort(v)
print("Valori pixeli sortati: ", x)
plt.plot(np.arange(len(x)),x) # generare grafic = plotare
plt.show()

# Afisare submatrice 50 x 50 (sfertul din partea dreapta jos)
A=img[50:,50:].copy() # imagine gray => matrice bidimensionala
cv.imshow("Football", img)
cv.imshow("A - Cropare 50 x 50", A)
cv.waitKey(0)

# Pragul de intensitate t: jumatate din elementele matricei <= t
t=np.median(x) # aplicare pe un vector SORTAT
print("Pragul de intensitate: ", t)

# culoare alba = intensitate 255
# culoarea neagra = intensitate 0
B=img.copy()
B[B<t]=0
B[B>=t]=255
cv.imshow("B- Colorare",B)
cv.waitKey(0)

# Colorare in functie de t
i_mediu=img.mean() # intensitatea medie a pozei != mediana pozei
print("Intensitatea medie: ", i_mediu)

C=img-i_mediu 
C[C<0]=0 # pixeli negativi, n-am voie sa am negativi ci INT-uri [0,255]
C=np.uint8(C) # convertire la INT 
cv.imshow("Operatii cu intensitatea medie",C)
cv.waitKey(0)

# Unde apare valoarea minima a intensitatii
i_min=img.min() #intensitatea minima
print("Intesitatea minima: ", i_min)
linie,coloana=np.where(img==i_min)
print(linie,coloana)


# ----------- Ex 1.7 Imaginea medie a unei colectii de imagini -----------
dir_path='set2'
files=os.listdir(dir_path)

color_images=[]
gray_images=[]
for image_name in files[1:]:

    # Citire
    path=dir_path+"\\"+image_name
    img=cv.imread(path) #citeste imaginea asa cum e (color)

    # Prelucrare
    img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) # citeste imaginea in format gray
    color_images.append(img)
    gray_images.append(img_gray)

# Dimensiunea color_images: (cate poze am, inaltimea, latimea, RGB)
color_images=np.array(color_images) 
print("Dimensiuni vector de imagini colorate: ", color_images.shape)
gray_images=np.array(gray_images)
print("Dimensiuni vector de imagini gri: ", gray_images.shape)

# Imagine medie color
# uint8 ca sa nu faca devieri
mean_color_image=np.uint8(np.mean(color_images,axis=0)) # pe 0 fac medie pe nr lor (impart la cate sunt)
cv.imshow("Imaginea medie colorate",mean_color_image)
cv.waitKey(0)

# Imagine medie gri
mean_gray_image=np.uint8(np.mean(gray_images,axis=0)) # pe 0 fac medie pe nr lor
cv.imshow("Imaginea medie gri",mean_gray_image)
cv.waitKey(0)

# Matricea X = deviatia standard a intensitatii pixelilor 
# Se face mereu pe gray
# std = standard deviation 
X=np.uint8(np.std(gray_images,axis=0)) # pe 0 fac medie pe nr lor (impart la cate sunt)
cv.imshow("X",X)
cv.waitKey(0)

# ---------- Ex 1.8 Modificarea unei imagini ----------

# tai 5000 de bucatele de 20 x 20 
img=cv.imread('butterfly.jpeg')
ws=20 #windows size

# tai bucatica
img_crop=img[250:250+ws, 250:250+ws,:].copy() # tai patch color

#  tai 5000 de bucatele random
nw=5000
H,W,_=img.shape
y=np.random.randint(0,H-ws,size=(nw))
x=np.random.randint(0,W-ws,size=(nw))
print("Cate randomuri am generat: ", len(y)) #nw

dist=np.zeros(nw) #vector de 0-uri
for i in range(nw):
    # tai patch
    patch=img[y[i]:y[i]+ws,x[i]:x[i]+ws,:].copy()
    # distanta euclidiana
    dist[i]=np.sqrt(np.sum((np.float64(patch)-np.float64(img_crop))**2))

index=np.argmin(dist) #iau care e patch-ul cu distanta cea mai mica
print("Bucata cu distanta cea mai mica are nr: ", index)
print("Distanta minima: ", dist.min())
print("Bucata cu distanta cea mai mica are nr: ",dist[index])

# Fac o copie a imaginii pe care sa o pot modifica
img_noua=img.copy()

# Inlocuiesc patch-ul
img_noua[250:250+ws,250:250+ws,:]=img[y[index]:y[index]+ws,x[index]:x[index]+ws,:].copy()

cv.imshow("Imaginea nou formata: ",img_noua)
cv.waitKey(0)

# daca vreau sa salvez poza noua
cv.imwrite('poza_noua_albina.jpg',img_noua)