""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Day 4 Challenge for Tprg 2131 intro week 3


### KHARI WALLACE, 100807131, TPRG 2131 ###

TPRG 2131 Fall 2022 Week 2 Day 4 Challenge
September 18, 2023
Khari Wallace <khari.wallace@dcmail.ca>

Day 4 challenge:

In the previous challenge, you modified the program to calculate resistance of two
resistors or the time constant of a resistor-capacitor combination, depending on
the user's choice. Today's task is to expand the program to give the user an
additional choice of calculating the resonant frequency of a series RLC circuit.
The previous choices are still available -- the RLC is an added feature. Depending
on the user's choices, ask for the necessary input values, then calculate and print
the expected result.
Instead of crashing out with CTRL-C, the program quits gracefully when the user
enters "q" or "Q".
;"""




import math

def calculate_series_resistance(resistor1, resistor2): 
    return resistor1 + resistor2

def calculate_parallel_resistance(resistor1, resistor2):
    return 1 / ((1 / resistor1) + (1 / resistor2))

def calculate_rc_time_constant(resistor, capacitance_uF):
    time_constant = resistor * capacitance_uF * 1e-6
    return time_constant

def calculate_resonant_frequency(inductance_mH, capacitance_uF):
    inductance_H = inductance_mH * 1e-3
    capacitance_F = capacitance_uF * 1e-6
    return 1 / (2 * math.pi * math.sqrt(inductance_H * capacitance_F))

print("Electrical Calculator (Type 'q' or 'Q' to quit)")

while True:
    choice = input("What would you like to calculate?\n"
                   "1. Series Resistance\n"
                   "2. Parallel Resistance\n"
                   "3. RC Time Constant\n"
                   "4. Resonant Frequency of Series RLC Circuit\n"
                   "Enter your choice (1/2/3/4/q/Q): ").lower()

    if choice == 'q':
        break

    if choice == '1':
        resistor1 = float(input("Enter the resistance of the first resistor in ohms: "))
        resistor2 = float(input("Enter the resistance of the second resistor in ohms: "))
        total_resistance = calculate_series_resistance(resistor1, resistor2)
        print(f"Total resistance in series: {total_resistance} ohms")

    elif choice == '2':
        resistor1 = float(input("Enter the resistance of the first resistor in ohms: "))
        resistor2 = float(input("Enter the resistance of the second resistor in ohms: "))
        total_resistance = calculate_parallel_resistance(resistor1, resistor2)
        print(f"Total resistance in parallel: {total_resistance} ohms")

    elif choice == '3':
        resistor = float(input("Enter the resistance in ohms: "))
        capacitance_uF = float(input("Enter the capacitance in uF: "))
        time_constant = calculate_rc_time_constant(resistor, capacitance_uF)
        print(f"RC Time Constant: {time_constant} seconds")

    elif choice == '4':
        inductance_mH = float(input("Enter the inductance in mH: "))
        capacitance_uF = float(input("Enter the capacitance in uF: "))
        resonant_frequency = calculate_resonant_frequency(inductance_mH, capacitance_uF)
        print(f"Resonant Frequency: {resonant_frequency:.2f} Hz")

    else:
        print("Invalid choice. Please select 1, 2, 3, 4, q, or Q.")
