class Ficha:
    def __init__(self):
        # Status
        self.nome = None
        self.hp_max = 0.0
        self.mp_max = 0.0
        self.xp = 0.0

        # Atributos
        self.str = 0.0
        self.dex = 0.0
        self.sap = 0.0  # Inteligência
        self.sab = 0.0
        self.car = 0.0

        # Moedas
        self.ouro = 0.0
        self.prata = 0.0
        self.cobre = 0.0

    # -------------------------
    # Métodos utilitários gerais
    # -------------------------

    def add(self, attr, valor):
        """Aumenta o valor de qualquer atributo numérico."""
        atual = getattr(self, attr)
        setattr(self, attr, atual + valor)

    def sub(self, attr, valor):
        """Diminui o valor de qualquer atributo numérico."""
        atual = getattr(self, attr)
        setattr(self, attr, atual - valor)

    # -------------------------
    # Visualização da ficha
    # -------------------------

    def view_ficha(self):
        return (
            f"Ficha:\n"
            f"Nome: {self.nome}\n"
            f"Hp: {self.hp_max}\n"
            f"Mp: {self.mp_max}\n"
            f"Xp: {self.xp}\n"
            f"For: {self.str}\n"
            f"Dex: {self.dex}\n"
            f"Int: {self.sap}\n"
            f"Sab: {self.sab}\n"
            f"Car: {self.car}\n"
            f"Ouro: {self.ouro}\n"
            f"Prata: {self.prata}\n"
            f"Cobre: {self.cobre}\n"
        )
