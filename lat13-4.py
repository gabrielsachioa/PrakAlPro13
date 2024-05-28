def jumlah_digit(n):
    if n < 10 and not n < 0:
        # kalau 1 digit, return digit itu             
        return n  
    else:
        # dua atau lebih baru jumlahkan                        
        return n % 10 + jumlah_digit(n // 10)

# PROGRAM UTAMA
print(jumlah_digit(2))
print(jumlah_digit(23))
print(jumlah_digit(234))