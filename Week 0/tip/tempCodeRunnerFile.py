def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the leading $
    d = d.replace("$", "")

    # Return the amount as a float
    return float(d)

def percent_to_float(p):
    # Remove the trailing %
    p = p.replace("$", "")

    p = float(p) / 100

    # Return the percentage as a float
    return float(p)

main()