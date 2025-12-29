import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, root, ficha):
        # ========================
        # Referências centrais
        # ========================
        self.root = root
        self.ficha = ficha

        self.root.title("DmKraken")
        self.root.geometry("900x600")

        # ========================
        # VARIÁVEIS (STATE DA GUI)
        # ========================
        # Valores Base
        self.nome_var = tk.StringVar(value=self.ficha.nome)
        self.apelido_var = tk.StringVar(value=self.ficha.apelido)
        self.nome_jogador_var = tk.StringVar(value=self.ficha.nome_jogador)

        self.classe_var = tk.StringVar(value=self.ficha.classe)
        self.ca_var = tk.IntVar(value=self.ficha.classeArmadura)
        self.inspiracao_var = tk.IntVar(value=self.ficha.inspiracao)

        self.level_var = tk.IntVar(value=self.ficha.level)
        self.xp_var = tk.DoubleVar(value=self.ficha.xp)

        # Status
        self.hp_max_var = tk.DoubleVar(value=self.ficha.hp_max)
        self.hp_atual_var = tk.DoubleVar(value=self.ficha.hp_atual)
        self.mp_max_var = tk.DoubleVar(value=self.ficha.mp_max)
        self.mp_atual_var = tk.DoubleVar(value=self.ficha.mp_atual)

        # Atributos (vars)
        self.forca_var = tk.DoubleVar(value=self.ficha.forca)
        self.destreza_var = tk.DoubleVar(value=self.ficha.destreza)
        self.inteligencia_var = tk.DoubleVar(value=self.ficha.inteligencia)
        self.sabedoria_var = tk.DoubleVar(value=self.ficha.sabedoria)
        self.carisma_var = tk.DoubleVar(value=self.ficha.carisma)

        # Modificadores (somente leitura)
        self.mod_forca_var = tk.StringVar()
        self.mod_destreza_var = tk.StringVar()
        self.mod_inteligencia_var = tk.StringVar()
        self.mod_sabedoria_var = tk.StringVar()
        self.mod_carisma_var = tk.StringVar()

        # Moedas
        self.ouro_var = tk.DoubleVar(value=self.ficha.ouro)
        self.prata_var = tk.DoubleVar(value=self.ficha.prata)
        self.cobre_var = tk.DoubleVar(value=self.ficha.cobre)

        # Mappings to ficha attribute names (fixes previous mismatch)
        self.atributos = {
            "forca": ("Força", self.forca_var),
            "destreza": ("Destreza", self.destreza_var),
            "inteligencia": ("Inteligência", self.inteligencia_var),
            "sabedoria": ("Sabedoria", self.sabedoria_var),
            "carisma": ("Carisma", self.carisma_var),
        }

        self.mod_vars = {
            "forca": self.mod_forca_var,
            "destreza": self.mod_destreza_var,
            "inteligencia": self.mod_inteligencia_var,
            "sabedoria": self.mod_sabedoria_var,
            "carisma": self.mod_carisma_var,
        }

        # ========================
        # LAYOUT PRINCIPAL
        # ========================
        main = ttk.Frame(self.root, padding=10)
        main.pack(fill="both", expand=True)

        # ========================
        # FRAMES (seguindo seu design)
        # ========================
        self._build_valores_base(main)
        self._build_status(main)
        self._build_atributos(main)
        self._build_modificadores(main)
        self._build_moedas(main)

        # ========================
        # TRACERS (reatividade)
        # ========================
        self._bind_atributos()
        self._update_modificadores()

    # =====================================================
    # BUILDERS DE FRAME (organização visual)
    # =====================================================

    def _build_valores_base(self, parent):
        frame = ttk.LabelFrame(parent, text="Valores Base")
        frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        campos = [
            ("Nome", self.nome_var),
            ("Apelido", self.apelido_var),
            ("Jogador", self.nome_jogador_var),
            ("Classe", self.classe_var),
            ("CA", self.ca_var),
            ("Inspiração", self.inspiracao_var),
            ("Level", self.level_var),
            ("XP", self.xp_var),
        ]

        for i, (label, var) in enumerate(campos):
            ttk.Label(frame, text=label).grid(row=i, column=0, sticky="w")
            ttk.Entry(frame, textvariable=var, width=18).grid(row=i, column=1)

    def _build_status(self, parent):
        frame = ttk.LabelFrame(parent, text="Status")
        frame.grid(row=1, column=0, sticky="nw", padx=10, pady=10)

        campos = [
            ("HP Máx", self.hp_max_var),
            ("HP Atual", self.hp_atual_var),
            ("MP Máx", self.mp_max_var),
            ("MP Atual", self.mp_atual_var),
        ]

        for i, (label, var) in enumerate(campos):
            ttk.Label(frame, text=label).grid(row=i, column=0, sticky="w")
            ttk.Entry(frame, textvariable=var, width=10).grid(row=i, column=1)

    def _build_atributos(self, parent):
        frame = ttk.LabelFrame(parent, text="Atributos")
        frame.grid(row=2, column=0, sticky="nw", padx=10, pady=10)

        for i, (_, (nome, var)) in enumerate(self.atributos.items()):
            ttk.Label(frame, text=nome).grid(row=i, column=0, sticky="w")
            ttk.Entry(frame, textvariable=var, width=6).grid(row=i, column=1)

    def _build_modificadores(self, parent):
        frame = ttk.LabelFrame(parent, text="Modificadores")
        frame.grid(row=2, column=1, sticky="nw", padx=10, pady=10)

        for i, (nome, var) in enumerate(
            [
                ("Força", self.mod_forca_var),
                ("Destreza", self.mod_destreza_var),
                ("Inteligência", self.mod_inteligencia_var),
                ("Sabedoria", self.mod_sabedoria_var),
                ("Carisma", self.mod_carisma_var),
            ]
        ):
            ttk.Label(frame, text=nome).grid(row=i, column=0, sticky="w")
            ttk.Label(frame, textvariable=var).grid(row=i, column=1, sticky="e")

    def _build_moedas(self, parent):
        frame = ttk.LabelFrame(parent, text="Moedas")
        frame.grid(row=3, column=0, sticky="nw", padx=10, pady=10)

        moedas = [
            ("Ouro", self.ouro_var),
            ("Prata", self.prata_var),
            ("Cobre", self.cobre_var),
        ]

        for i, (nome, var) in enumerate(moedas):
            ttk.Label(frame, text=nome).grid(row=i, column=0, sticky="w")
            ttk.Entry(frame, textvariable=var, width=10).grid(row=i, column=1)

    # =====================================================
    # REATIVIDADE (TRACE)
    # =====================================================

    def _bind_atributos(self):
        for attr, (_, var) in self.atributos.items():
            self._bind(attr, var)

    def _bind(self, attr, var):
        def callback(*_):
            try:
                # Ensure numeric vars are written back to the ficha using the correct attribute name
                value = var.get()
                setattr(self.ficha, attr, value)
                self._update_modificadores()
            except Exception:
                pass

        var.trace_add("write", callback)

    def _update_modificadores(self):
        # Use mapping to read the ficha's computed modifier properties
        for attr, mod_var in self.mod_vars.items():
            mod_value = getattr(self.ficha, f"mod_{attr}")
            mod_var.set(f"{mod_value:.1f}")