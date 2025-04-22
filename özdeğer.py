
import numpy as np
from sympy import diff, symbols


# Sayfa 37'ye göre olan fonksiyon
def f(x1, x2):
    return (x1)**2 - 2 * x1 - 3 * x2 * x1 + 12 * x2

# Verilen sembole göre türevi hesapla
def turev(f, sembol):
    return diff(f, sembol)


# Türevleri hesaplamak için semboller oluştur
x, y = symbols('x y')

# Fonksiyonu al
f = f(x, y)

# İlk kısmi türevleri hesapla
df_dx = turev(f, x)
df_dy = turev(f, y)

print("x'e göre türev: ", df_dx)
print("y'ye göre türev: ", df_dy)

# İkinci kısmi türevleri hesapla
df_dxdx = turev(df_dx, x)
df_dxdy = turev(df_dx, y)

df_dydx = turev(df_dy, x)
df_dydy = turev(df_dy, y)


print("x^2'ye göre türev: ", df_dxdx)
print("x*y'ye göre türev: ", df_dxdy)

print("y*x'ye göre türev: ", df_dydx)
print("y^2'ye göre türev: ", df_dydy)

# İkinci kısmi türevler matrisini tanımla
# Not: özdeğerleri hesaplamak için türev dizisini float dizisine dönüştürün
H = np.matrix([[df_dxdx, df_dxdy], [df_dydx, df_dydy]]).astype(float)

print(" ", H)

# Özdeğerleri bul
ozdegerler = np.linalg.eig(H).eigenvalues

print("Özdeğerler:", ozdegerler)

# Bir tanesi negatif, diğeri pozitif
if (ozdegerler[0] * ozdegerler[1] < 0):
    print("Eğer noktası")

# İkisi de negatif
if (ozdegerler[0] < 0 and ozdegerler[1] < 0):
    print("Yerel maksimum noktası")

# İkisi de pozitif
print("Yerel minimum noktası")