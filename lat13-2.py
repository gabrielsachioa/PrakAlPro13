def cek_palindrom(string):
    if len(string) == 1:
        return "Palindrom"
    else:               # len(string) > 1
        if string == string[::-1]:
            return cek_palindrom(string[1:-1])
        else:
            return "Bukan Palindrom"


print(cek_palindrom("kasurinirusak"))
print(cek_palindrom("babu"))