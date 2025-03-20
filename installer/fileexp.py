from functools import partial
import tkinter as tk
from tkinter import filedialog
import baseGUI as gui
import build

'''
Selected file.
'''
filepath: tk.StringVar


def browse(entry: tk.StringVar):
    '''
    Browse files and return path.
    '''
    entry.set(
        filedialog.askopenfilename(initialdir="..",
                                   title="Select a File",
                                   filetypes=(
                                       ("NES ROMs", "*.nes"),
                                       ("All Files", "*.*"))
                                   )
    )


class FilePage(gui.Page):
    def __init__(self, root, win):
        filepath = tk.StringVar(root)
        desc = '''Select the file path for your Super Mario Bros. ROM.'''
        elements = [
            gui.Element(tk.Label(root,
                        text='Select Super Mario Bros. ROM',
                        pady=15,
                        font=("TkDefaultFont", 15)),
                        {"row": 0, "column": 0, "columnspan": 2}
                        ),
            gui.Element(tk.Label(root,
                        text=desc),
                        {"row": 1, "column": 0, "columnspan": 2}
                        ),
            gui.Element(tk.Entry(root,
                        justify='right',
                        textvariable=filepath),
                        {"row": 2, "column": 0, "sticky": "e"}
                        ),
            gui.Element(tk.Button(root,
                        text='Browse...',
                        command=partial(browse, filepath),
                        anchor='w',
                        justify='left'),
                        {"row": 2, "column": 1, "sticky": "w"}
                        ),
            gui.Element(tk.Button(root,
                        text="Next",
                        command=partial(win.switchToPage, 'build')),
                        {"row": 3, "column": 1, "sticky": "se"}
                        )
        ]
        super().__init__(elements)
