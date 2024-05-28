def jumlah_deret_ganjil(n):
    if n < 1:
        return 0
    elif n % 2 != 0:
        return n + jumlah_deret_ganjil(n - 2)
    else:
        return jumlah_deret_ganjil(n - 1)

print(jumlah_deret_ganjil(7))