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

    # Retorno
    def view_ficha(self):
        show_all = (
            f"Ficha:\n"
            f"Nome: {self.nome}\n"
            f"Hp: {self.hp_max}\n"
            f"Mp: {self.mp_max}\n"
            f"Xp: {self.xp}\n"
            f"For: {self.str}\n"
            f"Dex: {self.dex}\n"
            f"Int: {self.sap}\n"
            f"Sab: {self.sab}\n"
            f"Car: {self.car}"
        )
        return show_all

    # Increase and Decrease (HP, MP, XP)
    def increase_hp(self, hp):
        self.hp_max += hp

    def decrease_hp(self, valor):
        self.hp_max -= valor

    def increase_mp(self, valor):
        self.mp_max += valor

    def decrease_mp(self, valor):
        self.mp_max -= valor

    def increase_xp(self, valor):
        self.xp += valor

    def decrease_xp(self, valor):
        self.xp -= valor

    # Getters and Setters

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_hp(self):
        return self.hp_max

    def set_hp(self, hp):
        self.hp_max = hp

    def get_mp(self):
        return self.mp_max

    def set_mp(self, mp):
        self.mp_max = mp

    def get_xp(self):
        return self.xp

    def set_xp(self, xp):
        self.xp = xp

    def get_str(self):
        return self.str

    def set_str(self, valor):
        self.str = valor

    def get_dex(self):
        return self.dex

    def set_dex(self, valor):
        self.dex = valor

    def get_sap(self):
        return self.sap

    def set_sap(self, valor):
        self.sap = valor

    def get_sab(self):
        return self.sab

    def set_sab(self, valor):
        self.sab = valor

    def get_car(self):
        return self.car

    def set_car(self, valor):
        self.car = valor
