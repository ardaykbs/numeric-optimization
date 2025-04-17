def bisection_method(f, a, b, max_iter=100):
    # f: Fonksiyon
    # a, b: Başlangıç aralığı
    # tol: Tolerans değeri (istenilen doğruluk)
    # max_iter: Maksimum iterasyon sayısı
    
    # İlk olarak, fonksiyonun başlangıçta işaret değiştirip değiştirmediğini kontrol edelim
    if f(a) * f(b) >= 0:
        print("Başlangıç aralığında kök bulunmuyor.")
        return None
    
    # Iterasyon sayısı
    iter_count = 0
    c = a + (b - a) / 2.0

    while not (df(c) == 0 or iter_count > max_iter):
        # Orta nokta c'yi hesapla
        
        
        # Orta noktanın fonksiyon değerini kontrol et
        if f(c) == 0:  # Eğer f(c) sıfırsa, kök bulunmuştur
            return c
        
        # Yeni aralığı belirle
        elif f(a) * f(c) < 0:
            b = c  # Kök a ile c arasında
        else:
            a = c  # Kök c ile b arasında
        
        c = a + (b - a) / 2.0
        iter_count += 1
    
    return c

# Örnek kullanım:
def f(x):
    return x**2 - 3

def df(x):
    return 2 * x

# Başlangıç aralığı
a = 2
b = 1

# Kökü bulma
root = bisection_method(f, a, b)

print("Kök:", root)
