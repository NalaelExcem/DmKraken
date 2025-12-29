class Ficha:
    def __init__(self):
        # Valores Base
        self.nome = ""
        self.apelido = ""
        self.nome_jogador = ""

        self.classeArmadura = 0
        self.inspiracao = 0
        self.classe = ""

        self.level = 0
        self.xp = 0.0

        # Status
        self.hp_max = 0.0
        self.mp_max = 0.0

        self.hp_atual = 0.0
        self.mp_atual = 0.0
        
        # Atributos Base
        self.forca = 0.0
        self.destreza = 0.0
        self.inteligencia = 0.0
        self.sabedoria = 0.0
        self.carisma = 0.0

        # Moedas
        self.ouro = 0.0
        self.prata = 0.0
        self.cobre = 0.0

    @property
    def mod_forca(self):
        return self.forca / 2

    @property
    def mod_destreza(self):
        return self.destreza / 2

    @property
    def mod_inteligencia(self):
        return self.inteligencia / 2

    @property
    def mod_sabedoria(self):
        return self.sabedoria / 2

    @property
    def mod_carisma(self):
        return self.carisma / 2

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
    # Visualização da ficha (Para BackEnd Somente)
    # -------------------------

    def view_ficha(self):
        return (
            f"Ficha:\n"
            f"Nome: {self.nome}\n"
            f"Hp: {self.hp_max}\n"
            f"Mp: {self.mp_max}\n"
            f"Xp: {self.xp}\n"
            f"For: {self.forca}\n"
            f"Dex: {self.destreza}\n"
            f"Int: {self.inteligencia}\n"
            f"Sab: {self.sabedoria}\n"
            f"Car: {self.carisma}\n"
            f"Ouro: {self.ouro}\n"
            f"Prata: {self.prata}\n"
            f"Cobre: {self.cobre}\n"
        )
