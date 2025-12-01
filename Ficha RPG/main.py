from ficha import Ficha  # importa a classe Ficha

def main():
    ficha = Ficha()

    print("Ver Alpha 1.0 - Inicializada.")

    # Primeiro loop — preenchimento da ficha
    while True:
        ficha.nome = input("Digite Nome: ")

        ficha.hp_max = float(input("Hp: "))
        ficha.mp_max = float(input("Mp: "))
        ficha.xp = float(input("Xp: "))

        ficha.str = float(input("Defina os Atributos, Força: "))
        ficha.dex = float(input("Destreza: "))
        ficha.sap = float(input("Inteligencia: "))
        ficha.sab = float(input("Sabedoria: "))
        ficha.car = float(input("Carisma: "))

        print(f"\n{ficha.view_ficha()}")
        resposta = input("Essa ficha está correta? Digite 1 para Sim: ")

        if resposta == "1":
            print("Salvo")
            break
        else:
            print("Preencha Novamente, seu bosta")

    # Segundo loop — menu de operações
    while True:
        print("\nEscolha uma opção:")
        print("1 - Aumentar HP")
        print("2 - Diminuir HP")
        print("3 - Aumentar MP")
        print("4 - Diminuir MP")
        print("5 - Aumentar XP")
        print("6 - Diminuir XP")
        print("7 - Mostrar ficha")
        print("8 - Sair")

        opcao = input("Opção: ")

        # Para operações, só perguntamos modificador se necessário
        if opcao in {"1", "2", "3", "4", "5", "6"}:
            modificador = float(input("Valor: "))

        match opcao:
            case "1":
                ficha.increase_hp(modificador)
                print(ficha.view_ficha())

            case "2":
                ficha.decrease_hp(modificador)
                print(ficha.view_ficha())

            case "3":
                ficha.increase_mp(modificador)
                print(ficha.view_ficha())

            case "4":
                ficha.decrease_mp(modificador)
                print(ficha.view_ficha())

            case "5":
                ficha.increase_xp(modificador)
                print(ficha.view_ficha())

            case "6":
                ficha.decrease_xp(modificador)
                print(ficha.view_ficha())

            case "7":
                print(ficha.view_ficha())

            case "8":
                print("Saindo...")
                break

            case _:
                print("Out of Range")


if __name__ == "__main__":
    main()
