# Numero 1

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

# Numero 2

def potencia(x, n):
    if n == 0:
        return 1
    return x * potencia(x, n - 1)

# Numero 3 

def Inverter_String(s):
    if len(s) <= 1:
        return s
    return s[-1] + Inverter_String(s[:-1])

# Numero 4  

def é_palindromo(s):
    s = "".join(c.lower() for c in s if c.isalnum())

    def checar(sub_s):
        if len(sub_s) <= 1:
            return True
        if sub_s[0] != sub_s[-1]:
            return False
        return checar(sub_s[1:-1])

    return checar(s)

# Numero 5

def somas_digitos(n):
    if n < 10:
        return n
    return (n % 10) + somas_digitos(n // 10)

# Numero 6

def Anagramas(s):
    if len(s) <= 1:
        return [s]

    resultado = []
    for i, char in enumerate(s):
        resto = s[:i] + s[i + 1 :]
        for p in Anagramas(resto):
            resultado.append(char + p)

    return list(set(resultado)) 

