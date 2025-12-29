import tkinter as tk
from ficha import Ficha
from Gui import App
import json

def main():
    ficha = Ficha() # Estado Único
    root = tk.Tk()
    app = App(root, ficha)
    root.mainloop()

if __name__ == "__main__":
    main()