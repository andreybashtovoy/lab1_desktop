import tkinter as tk
import requests
import json


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
        self._frame.grid(row=0, column=0)


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)


class CarGet(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is Cars list page").pack(side="top", fill="x", pady=10)


class CarCreate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is Cars create page").pack(side="top", fill="x", pady=10)


class OrderGet(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is Orders get page").pack(side="top", fill="x", pady=10)


class OrderCreate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is Orders create page").pack(side="top", fill="x", pady=10)


class InvoiceGet(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Button(
            self,
            text='List invoices',
            command=self.send_get_request
        ).grid(
            row=0,
            column=0,
            sticky=tk.W,
            pady=4
        )

    def send_get_request(self):
        r = requests.get('http://127.0.0.1:8000/api/')
        data = json.dumps(r.json(), indent=4)

        tk.Label(
            self,
            text=data
        ).grid(
            row=4,
            column=0,
            sticky=tk.W,
            pady=4
        )


class InvoiceCreate(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(
            self,
            text='Car id: '
        ).grid(
            row=0, column=0
        )
        self.card_id_entry = tk.Entry(self)
        self.card_id_entry.grid(
            row=0, column=1
        )

        tk.Label(
            self,
            text='Order id: '
        ).grid(
            row=1, column=0
        )
        self.order_id_entry = tk.Entry(self)
        self.order_id_entry.grid(
            row=1, column=1
        )

        tk.Label(
            self,
            text='Price: '
        ).grid(
            row=2, column=0
        )
        self.price_entry = tk.Entry(self)
        self.price_entry.grid(
            row=2, column=1
        )

        tk.Button(
            self,
            text='Create invoice',
            command=self.send_post_request
        ).grid(
            row=3,
            column=0,
            sticky=tk.W,
            pady=4
        )

    def send_post_request(self):
        car_id = int(self.card_id_entry.get())
        order_id = int(self.order_id_entry.get())
        price = int(self.price_entry.get())

        data = {
            'car_id': car_id,
            'order_id': order_id,
            'price': price
        }

        r = requests.post('http://127.0.0.1:8000/api/', data=data)
        result = r.json()

        tk.Label(
            self,
            text=result
        ).grid(
            row=4,
            column=0,
            sticky=tk.W,
            pady=4,
            columnspan=2
        )


if __name__ == "__main__":
    app = SampleApp()
    main_menu = tk.Menu(app)

    car_menu = tk.Menu(app)
    car_menu.add_command(label="Get", command=lambda: app.switch_frame(CarGet))
    car_menu.add_command(label="Create", command=lambda: app.switch_frame(CarCreate))

    order_menu = tk.Menu(app)
    order_menu.add_command(label="Get", command=lambda: app.switch_frame(OrderGet))
    order_menu.add_command(label="Create", command=lambda: app.switch_frame(OrderCreate))

    invoice_menu = tk.Menu(app)
    invoice_menu.add_command(label="Get", command=lambda: app.switch_frame(InvoiceGet))
    invoice_menu.add_command(label="Create", command=lambda: app.switch_frame(InvoiceCreate))

    crud_menu = tk.Menu(main_menu, tearoff=0)
    crud_menu.add_cascade(label="Car", menu=car_menu)
    crud_menu.add_cascade(label="Order", menu=order_menu)
    crud_menu.add_cascade(label="Invoice", menu=invoice_menu)

    main_menu.add_command(label="Main", command=lambda: app.switch_frame(StartPage))
    main_menu.add_cascade(label="Menu", menu=crud_menu)

    app.configure(menu=main_menu, padx=5, pady=5)

    app.title("Cars")
    app.geometry("800x600")
    app.mainloop()
