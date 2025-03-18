import tkinter as tk
import baseGUI as gui

class Page1(gui.Page):
    def __init__(self, root):
        desc= '''Welcome to the builder wizard for the Super Mario Bros. C recompilation, "Super Mario Bros. C Plus".
Please enter the file path for your Super Mario Bros. ROM below.'''
        elements = [
            gui.Element(tk.Label(root,
                            text='Super Mario Bros C Plus Builder',
                            pady=15,
                            font=("TkDefaultFont", 15)),
                            {"row": 0, "column": 0, "columnspan": 2}
                        ),
            gui.Element(tk.Label(root,
                            text= desc),
                            {"row": 1, "column": 0, "columnspan": 2}),
            gui.Element(tk.Entry(root,
                                justify='right'),
                            {"row": 2, "column": 0, "sticky": "e"}
                        ),
            gui.Element(tk.Button(root,
                                text='Browse...',
                                anchor='w',
                                justify='left'),
                            {"row": 2, "column": 1, "sticky": "w"}
                        )
        ] 
        super().__init__(elements)

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
root.title('Super Mario Bros. C Plus Builder')
win = gui.MainWindow(root)
win.initPages({
    "p1": Page1(root)
})
win.switchToPage("p1")