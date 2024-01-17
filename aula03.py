def produto(a, b):

   c = a*b
   return c

print (produto (2,4))

#Parte 2
print("===PARTE 2===")

def login(so, usuario="root", senha="123"):
    print(so)
    print(usuario)
    print(senha)

login("Ubuntu")
login("Ubuntu","bruno")
login("Windows", "bruno", "ifrn@123")

#Parte 3
print("===PARTE 3===")

def func():
        return 23, 24, 56, 78

x, y, z, w = func()
print(x)
print(y)
print(z)
print(w)

for letra in "IFRN":
    print(letra)