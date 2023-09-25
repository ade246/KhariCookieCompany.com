""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Day 1 Challenge for Tprg 2131 intro week 1-2


### KHARI WALLACE, 100707131, TPRG 2131 ###

TPRG 2131 Fall 2022 Week 2 Day 1 Challenge
September 13, 2023
Khari Wallace <khari.wallace@dcmail.ca>

This LCR calculator is ugly and incomplete. The code runs but doesn't actually
calculate anything. For full marks, you must complete the computation. You must
also "clean up" the code according to the course style guide and coding
standard. Specifically, you must:
  
  1) Take code that is duplicated and encapsulate it into a function that is
     called from the main program; the function must not "reach into" the
     main program for its working values;
  2) Rename variables so that they are not single letters, using descriptive
     names;"""



import math

def calculate_series_resistance(resistor1, resistor2):
    return resistor1 + resistor2

def calculate_parallel_resistance(resistor1, resistor2):
    return 1 / ((1 / resistor1) + (1 / resistor2))

print("Resistor Calculator (CTRL-C to quit)")

while True:
    circuit_type = input("Enter circuit type (S for Series, P for Parallel): ").upper()
    
    if circuit_type == 'S':
        resistor1 = float(input("Enter the resistance of the first resistor in ohms: "))
        resistor2 = float(input("Enter the resistance of the second resistor in ohms: "))
        total_resistance = calculate_series_resistance(resistor1, resistor2)
        print(f"Total resistance in series: {total_resistance} ohms")
    
    elif circuit_type == 'P':
        resistor1 = float(input("Enter the resistance of the first resistor in ohms: "))
        resistor2 = float(input("Enter the resistance of the second resistor in ohms: "))
        total_resistance = calculate_parallel_resistance(resistor1, resistor2)
        print(f"Total resistance in parallel: {total_resistance} ohms")
    
    else:
        print("Invalid input. Enter 'S' for Series or 'P' for Parallel.")
    
    cont = input("Do you want to calculate another circuit (Y/N)? ").upper()
    if cont != 'Y':
        break
