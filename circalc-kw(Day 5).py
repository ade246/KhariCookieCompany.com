""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Day 5 Challenge for Tprg 2131 intro week 3


### KHARI WALLACE, 100807131, TPRG 2131 ###

TPRG 2131 Fall 2022 Week 2 Day 4 Challenge
September 19, 2023
Khari Wallace <khari.wallace@dcmail.ca>

Day 5 challenge:

In the previous challenge, you modified the program to offer the added option to
calculate the resonant frequency of a series RLC circuit. Today's task is to expand
the program a bit more to give the user the Q (quality factor) of the series RLC
circuit. No additional inputs are required, the bandwidth and Q are just additional
results to be calculated and printed. Depending on the user's choices, ask for the
necessary input values, then calculate and print the expected result. The program
quits gracefully when the user enters "q" or "Q".
;"""



import math

def calculate_series_resonance(l, c, r):
    """Calculate the resonant frequency, bandwidth, and Q factor for a series resonant circuit."""
    resonant_frequency = 1 / (2 * math.pi * math.sqrt(l * c) * 1e-6)
    bandwidth = 1 / (r * c * 1e-6)
    q_factor = resonant_frequency / bandwidth
    return resonant_frequency, bandwidth, q_factor

def main():
    print("Electrical Circuit Calculator\n(Enter 'q' to quit)")

    while True:
        choice = input("Choose an option:\n"
                       "1. Calculate Series Resonance\n"
                       "2. Calculate Parallel Resistance\n"
                       "3. Calculate RC Time Constant\n"
                       "4. Calculate Series RLC Resonance (including Q factor)\n"
                       "Enter the number of your choice: ")

        if choice == 'q' or choice == 'Q':
            break

        if choice == '1':
            l = float(input("What is the inductance in mH? "))
            while l <= 0.0:
                l = float(input("The value must be greater than zero.\n"
                                "What is the inductance in mH? "))

            c = float(input("What is the capacitance in uF? "))
            while c <= 0.0:
                c = float(input("The value must be greater than zero.\n"
                                "What is the capacitance in uF? "))

            r = float(input("What is the resistance in ohms? "))
            while r <= 0.0:
                r = float(input("The value must be greater than zero.\n"
                                "What is the resistance in ohms? "))

            resonant_frequency, bandwidth, q_factor = calculate_series_resonance(l, c, r)

            print("Series Resonance Results:")
            print(f"Resonant Frequency: {resonant_frequency} Hz")
            print(f"Bandwidth: {bandwidth} Hz")
            print(f"Q Factor: {q_factor}\n")

        # Add other options here for parallel resistance and RC time constant calculations

        elif choice == '4':
            l = float(input("What is the inductance in mH? "))
            while l <= 0.0:
                l = float(input("The value must be greater than zero.\n"
                                "What is the inductance in mH? "))

            c = float(input("What is the capacitance in uF? "))
            while c <= 0.0:
                c = float(input("The value must be greater than zero.\n"
                                "What is the capacitance in uF? "))

            r = float(input("What is the resistance in ohms? "))
            while r <= 0.0:
                r = float(input("The value must be greater than zero.\n"
                                "What is the resistance in ohms? "))

            resonant_frequency, bandwidth, q_factor = calculate_series_resonance(l, c, r)

            print("Series RLC Resonance Results:")
            print(f"Resonant Frequency: {resonant_frequency} Hz")
            print(f"Bandwidth: {bandwidth} Hz")
            print(f"Q Factor: {q_factor}\n")

if __name__ == "__main__":
    main()
