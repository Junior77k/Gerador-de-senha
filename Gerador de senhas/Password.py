import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits 
    password: str = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return password

tamanho = int(input("Quantos digitos?"))
senha = gerar_senha(tamanho)
print("Sua senha aleatoria é!" , senha)