from game import Game
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Big Snake's Brain")
        self.geometry("300x100")
        self.label = tk.Label(self, text="Welcome to Big Snake's Game")
        self.label.pack()
        self.btn_play = tk.Button(self, text="Play", command=self.play)
        self.btn_play.pack()
        self.btn_data = tk.Button(self, text='Statistics', command=self.data)
        self.btn_data.pack()
        self.btn_quit = tk.Button(self, text="Quit", command=self.destroy)
        self.btn_quit.pack()

    def play(self):
        Game().run()

    def data(self):
        pass

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
