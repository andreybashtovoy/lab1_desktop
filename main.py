import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)


class Car(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is Cars page").pack(side="top", fill="x", pady=10)
        # tk.Button(self, text="Return to start page", command=lambda: master.switch_frame(StartPage)).pack()


class Order(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is Orders page").pack(side="top", fill="x", pady=10)


if __name__ == "__main__":
    app = SampleApp()
    main_menu = tk.Menu(app)

    crud_menu = tk.Menu(main_menu, tearoff=0)
    crud_menu.add_command(label="Main", command=lambda : app.switch_frame(StartPage))
    crud_menu.add_command(label="Car", command=lambda : app.switch_frame(Car))
    crud_menu.add_command(label="Order", command=lambda : app.switch_frame(Order))

    main_menu.add_cascade(label="Menu", menu=crud_menu)

    app.configure(menu=main_menu, padx=5, pady=5)

    app.title("Cars")
    app.geometry("800x600")
    app.mainloop()
