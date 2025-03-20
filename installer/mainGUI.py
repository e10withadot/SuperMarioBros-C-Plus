from functools import partial
import tkinter as tk
import baseGUI as gui
import fileexp as ex
import build


def rom_exists():
    '''
    Check if ROM exists.
    '''
    try:
        f = open('Super Mario Bros. (JU) (PRG0) [!].nes')
        f.close()
        win.switchToPage("build")
    except EnvironmentError:
        win.switchToPage("file")


class Start(gui.Page):
    def __init__(self, root):
        desc = '''Welcome to the setup wizard for the Super Mario Bros. recompilation, "Super Mario Bros. C Plus".
Please press "Next" to proceed with the setup.'''
        elements = [
            gui.Element(tk.Label(root,
                                 text='Super Mario Bros C Plus Setup Wizard',
                                 pady=15,
                                 font=("TkDefaultFont", 15)),
                        {"row": 0, "column": 0}
                        ),
            gui.Element(tk.Label(root,
                                 text=desc),
                        {"row": 1, "column": 0}),
            gui.Element(tk.Button(root,
                                  text="Next",
                                  command=partial(rom_exists)),
                        {"row": 2, "column": 0, "sticky": "se"})
        ]
        super().__init__(elements)


root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
root.title('Super Mario Bros. C Plus Builder')
win = gui.MainWindow(root)
win.initPages({
    "start": Start(root),
    "file": ex.FilePage(root, win),
    "build": build.BuildPage(root, win)
})
win.switchToPage("start")
