def get_input(prompt, zero_ok):
    while True:
        try:
            val = float(input(prompt))
            if val >= 0 if zero_ok else val > 0:
                return val
        except ValueError:
            pass
        print("Invalid input, please try again.")

start = get_input("Starting balance: ", True)
deposit = get_input("Monthly deposit: ", False)
rate = get_input("Monthly interest rate (%): ", True)
goal = get_input("Savings goal: ", False)

balance, total_int, months = start, 0.0, 0

if balance >= goal:
    print("\nStarting balance already meets the goal!")
    print("Goal reached in 0 months.")
else:
    print("\nMonth | Interest | Balance\n" + "-" * 27)
    for m in range(1, 61):
        interest = balance * (rate / 100)
        total_int += interest
        balance += interest + deposit
        print(f"{m:5d} | {interest:8.2f} | {balance:9.2f}")
        months = m
        if balance >= goal:
            break
    print("-" * 27)
    print(f"Goal {'reached in ' + str(months) + ' months' if balance >= goal else 'not reached after 60 months'}.")

print(f"Final Balance: {balance:.2f}\nTotal Interest Ea
