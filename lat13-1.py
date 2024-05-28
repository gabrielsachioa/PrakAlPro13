def cek_bilangan_prima(n, i = 2):
    if n <= 1:
        return "Bukan Prima"
    else:
        if i > n:
            return "Prima"
        else:
            if n == 2:
                return "Prima"
            elif n % 2 == 1:
                return cek_bilangan_prima(n, i + 1)
            else:
                return "Bukan Prima"
            
print(cek_bilangan_prima(19))
print(cek_bilangan_prima(6))