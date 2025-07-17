import tkinter as tk
import pyjokes


class Window():
    def __init__(self, root):
        root.title('Py-Jokes')
        root.geometry('950x100')

        self.joke = tk.StringVar()

        self.label = tk.Label(root, textvariable=self.joke, font=('Arial Bold', 10), bg='lightyellow')
        self.button = tk.Button(root, text='New Joke', command=self.get_new_joke, bg='lightblue')
        self.label.pack()
        self.joke.set(pyjokes.get_joke())
        self.button.pack()
    
    def get_new_joke(self):
        self.joke.set(pyjokes.get_joke())
   

root = tk.Tk()
window = Window(root)
root.mainloop()