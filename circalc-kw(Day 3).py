""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Day 3 Challenge for Tprg 2131 intro week 1-2


### KHARI WALLACE, 100807131, TPRG 2131 ###

TPRG 2131 Fall 2022 Week 2 Day 3 Challenge
September 15, 2023
Khari Wallace <khari.wallace@dcmail.ca>

Day 3 challenge:
In the previous challenge, you modified the program to calculate series or parallel
resistance of two resistors, depending on the user's choice. Today's task is to
expand the program to ask the user if they want to calculate series or parallel
resistance with two resistors (as before), or the RC time constant of a
resistor-capacitor combination. Depending on the answer, ask for two resistor
values, or a resistor and capacitor, then calculate and print the expected result.
The program continues looping until the user is done (CTRL-C).
;"""




import math

def calculate_series_resistance(resistor1, resistor2):
    return resistor1 + resistor2

def calculate_parallel_resistance(resistor1, resistor2):
    return 1 / ((1 / resistor1) + (1 / resistor2))

def calculate_rc_time_constant(resistor, capacitance):
    return resistor * capacitance * 1e-6

print("Electrical Calculator (CTRL-C to quit)")

while True:
    calculation_type = input("What do you want to calculate (S for series Resistance, P for parallel Resistance, T for RC Time Constant)? ").upper()
    
    if calculation_type == 'S':
        resistor1 = float(input("Enter the resistance of the first resistor in ohms: "))
        resistor2 = float(input("Enter the resistance of the second resistor in ohms: "))
        total_resistance = calculate_series_resistance(resistor1, resistor2)
        print(f"Total resistance in series: {total_resistance} ohms")
    
    elif calculation_type == 'P':
        resistor1 = float(input("Enter the resistance of the first resistor in ohms: "))
        resistor2 = float(input("Enter the resistance of the second resistor in ohms: "))
        total_resistance = calculate_parallel_resistance(resistor1, resistor2)
        print(f"Total resistance in parallel: {total_resistance} ohms")
    
    elif calculation_type == 'T':
        resistor = float(input("Enter the resistance in ohms: "))
        capacitance = float(input("Enter the capacitance in uF: "))
        rc_time_constant = calculate_rc_time_constant(resistor, capacitance)
        print(f"RC Time Constant: {rc_time_constant} seconds")
    
    else:
        print("Invalid input. Enter 'S' for series Resistance, 'P' for parallel Resistance, or 'T' for RC Time Constant.")
    
    cont = input("Do you want to calculate another value (Y/N)? ").upper()
    if cont != 'Y':
        break
