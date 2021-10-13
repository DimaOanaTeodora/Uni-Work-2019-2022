# Computer Vision (Materie de laborator)

### Laboratorul 1
- Citire imagine (H, W, R) sau (H, W)- gri
```pyhton
image = cv.imread("nume.extensie")
# Optional cv.IMREAD_GRAYSCALE daca vreau imagine gri
```
- Afisare imagine
```python
cv.waitKey(0) # se asteapta apasarea unei taste ca sa dispara imaginea
cv.imshow("windowName", image)
```
- Extragere dimensiuni
```python
H, W, R = image.shape
```
- Redimensionare
```python
imgResize = cv.resize(image, (100, 100)); # resize la 100 x 100
```
- Transformare matrice de intensitati -> vector
```python
v=img.flatten()
```
- Extragere submatrice
```python
newImage = image[50:,50:].copy() # sfertul din dreapta jos 50 pe 50
```
- Pragul de intensitate medie
```python
t=np.median(x) # aplicare pe un VECTOR SORTAT
```
- Intensitatea medie/minima a imaginii
```python
i_mediu=image.mean()
```
- Imaginea medie a unei colectii de imagini
```python
meanImage = np.uint8(np.mean(color_images,axis=0)) # pe 0 fac medie pe nr lor (impart la cate sunt)
```
- Imaginea STD(Standard deviation)
```python
# Se face mereu pe gray
stdImage = np.uint8(np.std(gray_images,axis=0))
```
- Scriere imagine noua
```python
cv.imwrite('nume.extensie',newImage)
```
