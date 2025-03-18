from functools import partial
import tkinter as tk
from tkinter import filedialog
import baseGUI as gui

filepath: str

def browse(entry: tk.StringVar):
    '''
    Browse files and return path.
    '''
    entry.set(filedialog.askopenfilename(initialdir = "..",
                                title = "Select a File",
                                filetypes = (("NES ROMs", "*.nes"), ("All Files", "*.*"))
                                ))

class FilePage(gui.Page):
    def __init__(self, root):
        filepath = tk.StringVar(root)
        elements= [
            gui.Element(tk.Entry(root,
                        justify='right',
                        textvariable= filepath),
                        {"row": 2, "column": 0, "sticky": "e"}
                        ),
            gui.Element(tk.Button(root,
                        text='Browse...',
                        command= partial(browse, filepath),
                        anchor='w',
                        justify='left'),
                        {"row": 2, "column": 1, "sticky": "w"}
                        )]
        super().__init__(elements)