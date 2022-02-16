import string
import secrets
import hashlib

# Generează o parolă de minim 10 caractere care conține cel puțin o literă mare, o
# literă mică, o cifră și un caracter special (.!$@)
# Utilizare: generare parola sigura
def verifyPassword(password):
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in ",.!$@" for c in password)):
        return True
    return False

while True:
    password = ""
    for i in range(10):
        password += secrets.choice(string.ascii_letters + string.digits + ",.!$@")
    
    if verifyPassword(password):
        break
print("Parola generata este: ", password)

# Generează un string URL-safe de (cel puțin) 32 caractere.
# Utilizare: forgot password?, confirm email
url_safe = secrets.token_urlsafe(32)
print("Stringul Url_safe generat: ", url_safe)

# token hexazecimal de (cel puțin) 32 cifre hexazecimale
# Utilizare: sistem de autentificare
token = secrets.token_hex(32)
print("Token-ul hexazecimal generat: ", token)

# verifica daca doua string uri sunt egale si minimizeaza riscul unui atac in timp
s1 = secrets.token_hex(32)
s2 = secrets.token_hex(32)
result = secrets.compare_digest(s1, s2)
print("Verificare daca doua secvente sunt identice: ", result)

# cheie binara fluida(100 de caractere)
# Utilizare: cripatera unui mesaj
key = secrets.token_bytes(100)
print("Cheia generata este:", key)

# Stochează parole folosind un modul / o librărie care 
# să ofere un nivel suficient de securitate
# Utilizare: prevenirea spargerii conturilor
raw_password = "!Admin01"
salt = 'f1nd1ngn3m0'
hashed_password = hashlib.sha256((raw_password + salt).encode('utf-8'))
print ('Parola criptata este:', hashed_password.hexdigest())