import calendar
import datetime
from tkinter import Button, DISABLED, Frame, Label, NORMAL, Tk

def get_date():
    """Displays a date picker window and returns [year, month, day]"""
    root = Tk()
    date = []
    dp = DatePicker(root, date)
    dp.pack()
    root.mainloop()
    return date

class DatePicker(Frame):
    def __init__(self, root, output_list):
        super().__init__(root)
        self.root = root
        self.output_list = output_list
        self.month = datetime.date.today().month
        self.year = datetime.date.today().year
        self.buttons = {}
        for row in range(6):
            for col in range(7):
                b = Button(self)
                self.buttons[(row, col)] = b
                b.grid(row=row+1, column=col, sticky="EW")
        Button(self, text="<",
               command=lambda: self.change_month(-1)).grid(row=0, column=0)
        Button(self, text=">",
               command=lambda: self.change_month(1)).grid(row=0, column=6)
        self.label = Label(self)
        self.label.grid(row=0, column=1, columnspan=5)
        self.change_month(0)

    def change_month(self, delta):
        m = self.month + delta - 1
        self.month, self.year = m % 12 + 1, self.year + m // 12
        self.label.config(text="{} {}".format(calendar.month_name[self.month],
                                              self.year))
        self.update_buttons()

    def choose(self, day):
        self.output_list[:] = [self.year, self.month, day]
        self.root.destroy()

    def set_day(self, button, day):
        if day:
            button.config(text=str(day), command=lambda: self.choose(day),
                          state=NORMAL)
        else:
            button.config(text="", command=None, state=DISABLED)

    def update_buttons(self):
        c = calendar.Calendar(firstweekday=6)
        days = c.monthdayscalendar(self.year, self.month)
        for row in range(6):
            for col in range(7):
                try:
                    day = days[row][col]
                except IndexError:
                    day = 0
                self.set_day(self.buttons[(row, col)], day)

if __name__ == '__main__':
    print(get_date())
