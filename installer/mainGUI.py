import tkinter as tk
import baseGUI as gui

class Page1(gui.Page):
    def __init__(self, root):
        elements = [
            gui.Element(tk.Label(root, text='Super Mario Bros C Plus Builder'), {"row": 0, "column": 0})
        ] 
        super().__init__(elements)

root = tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
root.title('Super Mario Bros. C Plus Builder')
win = gui.MainWindow(root)
win.initPages({
    "p1": Page1(root)
})
win.switchToPage("p1")