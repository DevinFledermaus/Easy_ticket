# Devin Fledermaus
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Easy Tickets")
root.geometry("700x500")
root.resizable(False, False)
root.config(bg="gray")


class TicketSales:
    tcktprice = StringVar

    def __init__(self, window):
        # Labels
        self.lbl1 = Label(window, text="Please enter cell number: ", bg="gray")
        self.lbl1.place(x=100, y=50)
        self.lbl2 = Label(window, text="Select the ticket type you'd like: ", bg="gray")
        self.lbl2.place(x=100, y=100)
        self.lbl3 = Label(window, text="How many tickets would you like?: ", bg="gray")
        self.lbl3.place(x=100, y=150)
        # Entries
        self.ent = Entry(window)
        self.ent.place(x=300, y=50)
        # OptionMenu
        self.options = ["Soccer", "Movie", "Theatre"]
        self.default_txt = StringVar(window)
        self.default_txt.set("Select Ticket")
        self.optmenu = OptionMenu(window, self.default_txt, *self.options)
        self.optmenu.place(x=330, y=95)
        # SpinBox
        self.spnbox = Spinbox(window, from_=1, to=100, width=3)
        self.spnbox.place(x=350, y=150)
        # Buttons
        self.btncalc = Button(window, text="Calculate Price", borderwidth="5", command=self.calculate, bg="green", fg="black")
        self.btncalc.place(x=100, y=250)
        self.btnclr = Button(window, text="Clear", borderwidth="5", command=self.clear, bg="yellow", fg="black")
        self.btnclr.place(x=400, y=250)
        # Results
        self.rescalc = Label(root, text="", bg="gray")
        self.ticket_res = Label(root, text="", bg="gray")
        self.cell_txt = Label(root, text="", bg="gray")
        self.rescalc.place(x=100, y=320)
        self.ticket_res.place(x=100, y=380)
        self.cell_txt.place(x=100, y=440)

    def calculate(self):
        # Constant variables
        tcktno = int(self.spnbox.get())
        vat = float(0.14)
        try:
            # Error Parameters
            int(self.ent.get())
            if len(self.ent.get()) > 10 or len(self.ent.get()) < 10:
                raise ValueError

            elif self.default_txt.get() == "Select Ticket":
                raise ValueError

            elif int(self.spnbox.get()) == 0:
                raise ValueError

            # Soccer
            elif self.default_txt.get() == "Soccer":
                price = 40
                amount = tcktno * (price + vat)
                result = ("Total Amount: R{}".format(amount))
                self.rescalc.config(text=result)

            # Movie
            elif self.default_txt.get() == "Movie":
                price = 75
                amount = tcktno * (price + vat)
                result = ("Total Amount: R{}".format(amount))
                self.rescalc.config(text=result)

            # Theatre
            elif self.default_txt.get() == "Theatre":
                price = 100
                amount = tcktno * (price + vat)
                result = ("Total Amount: R{}".format(amount))
                self.rescalc.config(text=result)
            # Results
            tickets = "{} ticket(s) reserved : {} ".format(self.default_txt.get(), tcktno)
            cell = "Reservations made by: {}".format(self.ent.get())
            self.ticket_res.config(text=tickets)
            self.cell_txt.config(text=cell)

        except ValueError:
            messagebox.showerror("ERROR", "Please enter all relevant information")

    # Defining clear button
    def clear(self):
        self.ent.delete(0, END)


# Run Program
TicketSales(root)
root.mainloop()
