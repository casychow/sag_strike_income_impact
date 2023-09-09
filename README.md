# SAG-AFTRA Strike Potential Impact on Income Calculator
The members of SAG-AFTRA (Screen Actors Guild and American Federation of Television and Radio Artists) and their allies are on strike about unfair labor situations in Hollywood. Some actors have cited the lack of residuals as reasons for going on strike; despite appearing on popular TV shows as series regulars or guests, they are being paid pennies.

This project shows how much an actor's finances could be impacted based on their expected work hours, their hourly wage[1], their expected overtime work hours, and their overtime hourly wage[2].

[1] Note: the hourly wage is assumed to be constant for this project

[2] Note: the overtime hourly wage is also assumed to be constant

# Requirements
- Python 3
- Tkinter library

# Instructions
1. Download the `tkinter_sag_strike_calculator.py` file
2. Open a command prompt and change the working directory to the location of the downloaded file
3. Run `python tkinter_sag_strike_calculator.py`
   - Press `Quit` to quit the program or click on the `X`at the top right of the window

# Calculator
![sag_strike_cost_calculator](https://github.com/casychow/sag_strike_income_impact/blob/main/pictures/sag_strike_cost_calculator_v0_1.png)

## Inputting information
![sag_strike_cost_calculator_input_v0_1](https://github.com/casychow/sag_strike_income_impact/blob/main/pictures/sag_strike_cost_calculator_input_v0_1.png)

## Outputting information
![sag_strike_cost_calculator_output_v0_1](https://github.com/casychow/sag_strike_income_impact/blob/main/pictures/sag_strike_cost_calculator_output_v0_1.png)

# To-Do:
- [ ] make moving table entries easier when adding new features/boxes instead of recalculating all object placement, OR use .grid
- [ ] table to insert estimated pay for which dates, taxes, actual pay, % loss, payday
- [ ] calculate average tax -> use to tune actual pay and % loss
