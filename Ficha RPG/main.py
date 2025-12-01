from ficha import Ficha  # importa a classe Ficha

def main():
    ficha = Ficha()

    print("Ver Alpha 1.0 - Inicializada.")

    # Primeiro loop — preenchimento da ficha
    while True:
        ficha.nome = input("Digite Nome (texto): ")

        while True:
            try:
                ficha.hp_max = float(input("Hp (número): "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Hp.")

        while True:
            try:
                ficha.mp_max = float(input("Mp (número): "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Mp.")

        while True:
            try:
                ficha.xp = float(input("Xp (número): "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Xp.")

        while True:
            try:
                ficha.str = float(input("Defina os Atributos, Força: "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Força.")

        while True:
            try:
                ficha.dex = float(input("Destreza: "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Destreza.")

        while True:
            try:
                ficha.sap = float(input("Inteligencia: "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Inteligencia.")

        while True:
            try:
                ficha.sab = float(input("Sabedoria: "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Sabedoria.")

        while True:
            try:
                ficha.car = float(input("Carisma: "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Carisma.")

        while True:
            try:
                ficha.ouro = float(input("Moedas - Ouro: "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Ouro.")

        while True:
            try:
                ficha.prata = float(input("Prata: "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Prata.")

        while True:
            try:
                ficha.cobre = float(input("Cobre: "))
                break
            except ValueError:
                print("Por favor, digite um número válido para Cobre.")

        print(f"\n{ficha.view_ficha()}")

        resposta = input("Essa ficha está correta? Digite 1 para Sim: ")

        if resposta == "1":
            print("Salvo")
            break
        else:
            print("Preencha novamente.")

    # Segundo Loop — Menu
    while True:
        print("\nEscolha uma Opção:")
        print("1 - Aumentar Atributos")
        print("2 - Diminuir Atributos")
        print("3 - Mostrar a ficha")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao in {"1", "2"}:
            print("\nAtributos disponíveis:")
            atributos_validos = {
                "hp_max", "mp_max", "xp", "str", "dex", "sap", "sab", "car",
                "ouro", "prata", "cobre"
            }

            print(", ".join(atributos_validos))

            attr = input("Digite o atributo que deseja modificar: ")

            while attr not in atributos_validos:
                print("Atributo inválido. Tente novamente.")
                attr = input("Digite o atributo que deseja modificar: ")

            while True:
                try:
                    valor = float(input("Digite o valor: "))
                    break
                except ValueError:
                    print("Por favor, digite um número válido.")

            if opcao == "1":
                ficha.add(attr, valor)
            else:
                ficha.sub(attr, valor)

            print("\nAtributo atualizado!")
            print(ficha.view_ficha())

        elif opcao == "3":
            print(f"\n{ficha.view_ficha()}")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()