# Created by Cassandra Chow

# Purpose: This program helps individuals participating in the SAG-AFTRA strike of 2023
# to input their expected work hours and constant hourly rate to estimate a
# projected loss of income while protesting unfair labor laws.

"""
To-Do:
- [] insert last month's tax -> get actual pay and %loss
- [] remove all unnecessary "self."
- [] make moving table entries easier when adding new features/boxes instead of recalculating all object placement
- [] table to insert estimated pay for which dates, taxes, actual pay, % loss, payday
- [] calculate average tax -> use to tune actual pay and % loss
"""

import tkinter as tk
from tkinter import messagebox

class Window():
    def __init__(self) -> None:
        """
        Initialize the tkinter window, all of the string variables, label objects, entry objects, and buttons.
        """
        # Setup tkinter window
        self.window = tk.Tk()
        self.window.title("SAG-AFTRA Strike Estimated Cost Calculator")
        self.window.geometry("500x300")

        # Setup text
        self.message = "Projected Impact on Income: "

        # Declare string variables for storage
        self.reg_hrs = tk.StringVar()
        self.reg_hr_rate = tk.StringVar()
        self.over_hrs = tk.StringVar()
        self.over_hr_rate = tk.StringVar()
        self.monthly_deductions = tk.StringVar()

        """
        For:
        - Expected Regular Work Hour(s)
        - Hourly Rate
        - Expected Overtime Work Hour(s)
        - Overtime Rate
        - Last month's deductions
        - Answer
        """

        # Show labels and entry boxes
        self.reg_hr_label = tk.Label(self.window, text="Expected Regular Work Hour(s): ") # Show following "Expected Work Hours" entry box
        self.reg_hr_entry = tk.Entry(self.window, textvariable=self.reg_hrs) # Input expected work hours

        self.reg_hr_rate_label = tk.Label(self.window, text="Hourly Rate: ") # Show following "Hourly Rate" entry box
        self.reg_hr_rate_entry = tk.Entry(self.window, textvariable=self.reg_hr_rate) # Input hourly work rate

        self.over_hr_label = tk.Label(self.window, text="Expected Overtime Work Hour(s): ") # Show following "Expected Overtime Work Hour(s)" entry box
        self.over_hr_entry = tk.Entry(self.window, textvariable=self.over_hrs) # Input expected overtime work hours

        self.over_hr_rate_label = tk.Label(self.window, text="Overtime Rate: ") # Show following "Overtime Rate" entry box
        self.over_hr_rate_entry = tk.Entry(self.window, textvariable=self.over_hr_rate) # Input hourly overtime work rate

        self.monthly_deduction_label = tk.Label(self.window, text="Monthly Deduction: ") # Show following "Monthly Deduction" entry box
        self.monthly_deduction_entry = tk.Entry(self.window, textvariable=self.monthly_deductions) # Input last month's deduction (from tax, 401k contribution, etc)

        self.answer = tk.Label(self.window, text="{0}: $0.0".format(self.message)) # Show following total expected losses

        # Place all objects in appropriate locations in window
        self.reg_hr_label.place(x=10, y=25)
        self.reg_hr_entry.place(x=200, y=25)
        self.reg_hr_rate_label.place(x=10, y=50)
        self.reg_hr_rate_entry.place(x=200, y=50)
        self.over_hr_label.place(x=10, y=75)
        self.over_hr_entry.place(x=200, y=75)
        self.over_hr_rate_label.place(x=10, y=100)
        self.over_hr_rate_entry.place(x=200, y=100)
        self.monthly_deduction_label.place(x=10, y=125)
        self.monthly_deduction_entry.place(x=200, y=125)
        self.answer.place(x=175, y=150)

        # Initialize and place calculate and quit buttons
        calc_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        calc_button.place(x=175, y=190)
        quit_button = tk.Button(self.window, text="Quit", command=self.program_exit)
        quit_button.place(x=175, y=250)

    def calculate(self) -> None:
        """
        Calculate the estimated loss of money for the user based on the following formula.

        Formula = reg_work_hrs * reg_hrly_rate + overtime_hrs * overtime_hrly_rate
        """
        money_total = round(float(self.reg_hrs.get()) * float(self.reg_hr_rate.get()) + float(self.over_hrs.get()) * float(self.over_hr_rate.get()), 2)
        self.answer.config(text="{0}: ${1}".format(self.message, money_total))
        messagebox.showinfo("Projected Impact", "{0}${1}".format(self.message, money_total))

    def program_exit(self) -> None:
        """
        Exits the program.
        """
        exit()

    def run(self) -> None:
        """
        Runs the program continuously
        """
        self.window.mainloop()

if __name__ == "__main__":
    w = Window()
    w.run()
