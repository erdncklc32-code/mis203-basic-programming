def ticket_office():
    tickets_sold = 0
    total_revenue = 0.0
    free_tickets = 0

    while True:
        name = input("Customer name (or q to quit): ").strip()
        if name.lower() == 'q':
            break

        # Validate age
        age_input = input("Age: ").strip()
        try:
            age = int(age_input)
        except ValueError:
            print("Invalid age.")
            continue

        if age < 0 or age > 120:
            print("Invalid age.")
            continue

        # Validate day
        day_input = input("Day (weekday/weekend): ").strip().lower()
        if day_input not in ["weekday", "weekend"]:
            print("Invalid day.")
            continue

        # Validate student status
        student_input = input("Student (yes/no): ").strip().lower()
        if student_input not in ["yes", "no"]:
            print("Please answer yes or no.")
            continue

        # Determine base price
        if day_input == "weekday":
            base_price = 200.0
        else:
            base_price = 250.0

        # Apply discounts in order of precedence
        if age < 6:
            discount = 1.0  # 100% free
            category = "Free"
        elif age >= 65:
            discount = 0.5  # 50% senior discount
            category = "Senior"
        elif age <= 12:
            discount = 0.4  # 40% child discount
            category = "Child"
        elif student_input == "yes" and age <= 25:
            discount = 0.3  # 30% student discount
            category = "Student"
        else:
            discount = 0.0  # 0% standard
            category = "Standard"

        price = base_price * (1 - discount)

        # Print ticket result
        print(f"{name}: {price:.2f} TRY ({category})")

        # Update statistics
        tickets_sold += 1
        total_revenue += price
        if category == "Free":
            free_tickets += 1

    print()
    # Print summary
    if tickets_sold == 0:
        print("No tickets sold.")
    else:
        average_price = total_revenue / tickets_sold
        print(f"Tickets sold: {tickets_sold}")
        print(f"Total revenue: {total_revenue:.2f} TRY")
        print(f"Average price: {average_price:.2f} TRY")
        print(f"Free tickets: {free_tickets}")

if __name__ == "__main__":
    ticket_office()
