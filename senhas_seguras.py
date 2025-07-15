import random
import string


def gerar_senhas(
    tamanho=16,
    usar_maiuscula=True,
    usar_minuscula=True,
    usar_numeros=True,
    usar_simbolos=True,
):
    caracteres = ""

    if usar_numeros:
        caracteres += string.digits

    if usar_maiuscula:
        caracteres += string.ascii_uppercase

    if usar_minuscula:
        caracteres += string.ascii_lowercase

    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Você precisa escolher pelo menos um tipo de caractere.")

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def menu():
    print("GERADOR DE SENHAS SEGURAS (GSS)".center(41, "="))
    try:
        tamanho = int(input("Digite o tamnho da senha: "))
    except ValueError:
        print("Valor invalido.")
        return

    usar_numeros = input("Incluir numeros? (s/n): ").lower() == "s"
    usar_maiuscula = input("Incluir maiúscula? (s/n): ").lower() == "s"
    usar_minuscula = input("Incluir minúscula? (s/n): ").lower() == "s"
    usar_simbolos = input("Incluir simbolos? (s/n): ").lower() == "s"

    try:
        senha = gerar_senhas(
            tamanho=tamanho,
            usar_numeros=usar_numeros,
            usar_maiuscula=usar_maiuscula,
            usar_minuscula=usar_minuscula,
            usar_simbolos=usar_simbolos,
        )

    except ValueError as erro:
        print("Erro:", erro)
        return

    print("Senha Gerada!")
    print(senha)
    print("!! ATENÇÃO !! Sua senha não foi salva em lugar nenhum. Copie com segurança.")


if __name__ == "__main__":
    menu()
