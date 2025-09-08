# finance_calculators.py
import math

# ---------------- FUNCTIONS ----------------
def simple_interest(principal, rate, years):
    return principal * (1 + rate * years)

def compound_interest(principal, rate, years):
    return principal * math.pow((1 + rate), years)

def bond_repayment(present_value, rate, months):
    i = (rate / 100) / 12
    return (i * present_value) / (1 - (1 + i) ** (-months))

# ---------------- MAIN LOOP ----------------
while True:
    print("\n Choose an option:")
    print(" - investment → Calculate investment interest")
    print(" - bond       → Calculate monthly home loan repayments")
    print(" - exit       → Quit program")

    choice = input("\nEnter your choice: ").strip().lower()

    # ---------------- INVESTMENT ----------------
    if choice == "investment":
        try:
            deposit = float(input("💰 Enter the amount you are depositing: "))
            interest_rate = float(input("📊 Enter the interest rate (e.g. 8 for 8%): "))
            years = int(input("⏳ Enter the number of years you plan on investing: "))
            interest = input("Type of interest ('simple' or 'compound'): ").strip().lower()
        except ValueError:
            print(" Error: Please enter valid numbers.")
            continue

        r = interest_rate / 100

        if interest == "simple":
            A = simple_interest(deposit, r, years)
        elif interest == "compound":
            A = compound_interest(deposit, r, years)
        else:
            print(" Error: Please enter either 'simple' or 'compound'.")
            continue

        print(f"\n After {years} years at {interest_rate}% interest, "
              f"your investment will be worth: R{A:,.2f}")

    # ---------------- BOND ----------------
    elif choice == "bond":
        try:
            present_value = float(input(" Enter the present value of the house: "))
            interest_rate = float(input(" Enter the annual interest rate (e.g. 7 for 7%): "))
            months = int(input(" Enter the number of months to repay the bond: "))
        except ValueError:
            print(" Error: Please enter valid numbers.")
            continue

        repayment = bond_repayment(present_value, interest_rate, months)
        print(f"\n You will have to repay: R{repayment:,.2f} per month over {months} months.")

    # ---------------- EXIT ----------------
    elif choice == "exit":
        print(" Program closed. Goodbye!")
        break

    # ---------------- INVALID INPUT ----------------
    else:
        print(" Error: Invalid choice. Please enter 'investment', 'bond', or 'exit'.")
