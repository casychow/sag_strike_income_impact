# Created by Cassandra Chow

# Purpose: This program helps individuals participating in the SAG-AFTRA strike of 2023
# to input their expected work hours and constant hourly rate to estimate a
# projected loss of income while protesting unfair labor laws.

import tkinter as tk

class Window():
    def __init__(self) -> None:
        """
        Initialize the tkinter window, all of the string variables, label objects, entry objects, and buttons.
        """
        # Setup tkinter window
        self.window = tk.Tk()
        self.window.title("SAG-AFTRA Strike Estimated Cost Calculator")
        self.window.geometry("600x450")

        # Setup text
        self.loss_income_message = "Projected Impact on Income: "

        # Declare string variables for storage
        self.reg_hrs_string = tk.StringVar()
        self.reg_hr_rate_string = tk.StringVar()
        self.over_hrs_string = tk.StringVar()
        self.over_hr_rate_string = tk.StringVar()
        self.pay_deductions_string = tk.StringVar()
        self.paid_amount_string = tk.StringVar()

        """
        For:
        - Expected Regular Work Hour(s)
        - Hourly Rate
        - Expected Overtime Work Hour(s)
        - Overtime Rate
        - Pay deductions
        - Answer
        """

        # Show labels and entry boxes
        reg_hr_label = tk.Label(self.window, text="Expected Regular Work Hour(s): ") # Show following "Expected Work Hours" entry box
        reg_hr_entry = tk.Entry(self.window, textvariable=self.reg_hrs_string) # Input expected work hours

        reg_hr_rate_label = tk.Label(self.window, text="Hourly Rate: ") # Show following "Hourly Rate" entry box
        reg_hr_rate_entry = tk.Entry(self.window, textvariable=self.reg_hr_rate_string) # Input hourly work rate

        over_hr_label = tk.Label(self.window, text="Expected Overtime Work Hour(s): ") # Show following "Expected Overtime Work Hour(s)" entry box
        over_hr_entry = tk.Entry(self.window, textvariable=self.over_hrs_string) # Input expected overtime work hours

        over_hr_rate_label = tk.Label(self.window, text="Overtime Rate: ") # Show following "Overtime Rate" entry box
        over_hr_rate_entry = tk.Entry(self.window, textvariable=self.over_hr_rate_string) # Input hourly overtime work rate

        pay_deduction_label = tk.Label(self.window, text="Pay Deduction: ") # Show following "Pay Deduction" entry box
        pay_deduction_entry = tk.Entry(self.window, textvariable=self.pay_deductions_string) # Input last pay stub's deductions (from tax, 401k contribution, etc)

        paid_amount_label = tk.Label(self.window, text="Actual Pay: ")
        paid_amount_entry = tk.Entry(self.window, textvariable=self.paid_amount_string) # Input last pay stub's final paid amount

        self.answer = tk.Label(self.window, text="{0} $0.0".format(self.loss_income_message)) # Show following total expected losses

        # Place all objects in appropriate locations in window
        reg_hr_label.place(x=10, y=25)
        reg_hr_entry.place(x=200, y=25)
        reg_hr_rate_label.place(x=10, y=50)
        reg_hr_rate_entry.place(x=200, y=50)
        over_hr_label.place(x=10, y=75)
        over_hr_entry.place(x=200, y=75)
        over_hr_rate_label.place(x=10, y=100)
        over_hr_rate_entry.place(x=200, y=100)
        pay_deduction_label.place(x=10, y=125)
        pay_deduction_entry.place(x=200, y=125)
        paid_amount_label.place(x=10, y=150)
        paid_amount_entry.place(x=200, y=150)
        self.answer.place(x=100, y=250)

        # Initialize and place calculate and quit buttons
        calc_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        calc_button.place(x=350, y=25)
        quit_button = tk.Button(self.window, text="Quit", command=self.program_exit)
        quit_button.place(x=350, y=50)

    def read_string_var(self, input_string: 'tk.StringVar') -> float:
        return float(input_string.get()) if input_string.get() != "" else 0

    def calculate(self) -> None:
        """
        Calculate the estimated loss of money for the user based on the following formula.

        Formulas:
        - Estimated Pay = (Regular Work Hours * Regular Hourly Rate) + (Overtime Hours * Overtime Hourly Rate)
        - % loss = (Estimated Pay - Actual Pay) / Estimated Pay
        """
        estimated_pay = round(self.read_string_var(self.reg_hrs_string) * self.read_string_var(self.reg_hr_rate_string) + \
                              self.read_string_var(self.over_hrs_string) * self.read_string_var(self.over_hr_rate_string)
                              , 2)
        deducted_pay = self.read_string_var(self.pay_deductions_string)
        actual_pay = self.read_string_var(self.paid_amount_string)
        percent_loss = round(((estimated_pay - actual_pay) / estimated_pay * 100), 2)
        self.answer.config(text="{} {}".format(self.loss_income_message, actual_pay))
        calculated_info = "Estimated Pay: ${0}\nPay Stub Deductions: ${1}\nActual Pay: ${2}\nPercent Loss: {3}%".format(estimated_pay, deducted_pay, actual_pay, percent_loss)
        
        final_text = tk.Text(self.window, height=5, width=40)
        final_text.place(x=100, y=300)
        final_text.insert(tk.END, calculated_info)

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
