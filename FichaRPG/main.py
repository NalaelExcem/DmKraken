from ficha import Ficha  # importa a classe Ficha
import json # importa json para futuras funcionalidades


def pedir_numero(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Por favor, digite um número válido.")


def main():
    ficha = Ficha()

    print("Ver Alpha 1.0 - Inicializada.")

    # ------------------------------
    # Primeiro Loop — preenchimento
    # ------------------------------
    print("Deseja carregar dados da ficha salva? (s/n)")
    op = input().lower()
    if op == "s":
        with open("ficha_salva.json", "r") as f:
            dados = json.load(f)
            for chave, valor in dados.items():
                setattr(ficha, chave, valor) 
    else:
        while True:
            ficha.nome = input("Digite Nome (texto): ")

            # Lista de atributos numéricos que serão perguntados automaticamente
            campos = [
                ("hp_max", "Hp (número): "),
                ("mp_max", "Mp (número): "),
                ("xp", "Xp (número): "),
                ("str", "Defina os Atributos, Força: "),
                ("dex", "Destreza: "),
                ("sap", "Inteligência: "),
                ("sab", "Sabedoria: "),
                ("car", "Carisma: "),
                ("ouro", "Moedas - Ouro: "),
                ("prata", "Prata: "),
                ("cobre", "Cobre: "),
            ]

            # Preenchimento automático
            for atributo, mensagem in campos:
                valor = pedir_numero(mensagem)
                setattr(ficha, atributo, valor)

            print(f"\n{ficha.view_ficha()}")

            resposta = input("Essa ficha está correta? Digite 1 para Sim: ")

            if resposta == "1":
                with open("ficha_salva.json", "w") as f:
                    json.dump(ficha.__dict__, f)
                print("Salvo")
                break
            else:
                print("Preencha novamente.")

    # ------------------------------
    # Segundo Loop — Menu
    # ------------------------------
    atributos_validos = {
        "hp_max", "mp_max", "xp", "str", "dex", "sap", "sab",
        "car", "ouro", "prata", "cobre"
    }

    while True:
        print("\nEscolha uma Opção:")
        print("1 - Aumentar Atributos")
        print("2 - Diminuir Atributos")
        print("3 - Mostrar a ficha")
        print("4 - Sair")

        opcao = input("Opção: ")

        # ------------------------------
        # Modificar atributos
        # ------------------------------
        if opcao in {"1", "2"}:
            print("\nAtributos disponíveis:")
            print(", ".join(atributos_validos))

            attr = input("Digite o atributo que deseja modificar: ")

            while attr not in atributos_validos:
                print("Atributo inválido. Tente novamente.")
                attr = input("Digite o atributo que deseja modificar: ")

            valor = pedir_numero("Digite o valor: ")

            if opcao == "1":
                ficha.add(attr, valor)
            else:
                ficha.sub(attr, valor)

            print("\nAtributo atualizado!")
            print(ficha.view_ficha())

        # ------------------------------
        # Mostrar ficha
        # ------------------------------
        elif opcao == "3":
            print(f"\n{ficha.view_ficha()}")

        # ------------------------------
        # Sair
        # ------------------------------
        elif opcao == "4":
            with open("ficha_salva.json", "w") as f:
                json.dump(ficha.__dict__, f)
            print("Salvo")
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()