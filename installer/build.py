import baseGUI as gui
import tkinter as tk
import tkinter.ttk as ttk


class BuildPage(gui.Page):
    def __init__(self, root, win):
        desc = '''Please wait while the program builds.'''
        elements = [
            gui.Element(tk.Label(root,
                        text='Building...',
                        pady=15,
                        font=("TkDefaultFont", 15)),
                        {"row": 0, "column": 0}
                        ),
            gui.Element(tk.Label(root,
                        text=desc),
                        {"row": 1, "column": 0}
                        ),
            gui.Element(ttk.Progressbar(root,
                        orient='horizontal',
                        length=100,
                        mode='determinate'),
                        {"row": 2, "column": 0}
                        ),
        ]
        super().__init__(elements)
