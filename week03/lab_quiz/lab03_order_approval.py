def main():
    # 1. Kullanıcıdan girdileri al
    amount = float(input("Enter order amount (TRY): "))
    available_stock = int(input("Enter available stock: "))
    requested_qty = int(input("Enter requested quantity: "))
    member_input = input("Is customer a member? (yes/no): ").strip().lower()

    # Üyelik kontrolü
    is_member = member_input in ["yes", "y"]

    # 2. Hata & Stok Kontrolleri 
    if requested_qty <= 0 or amount <= 0:
        print("\nOrder Status: REJECTED")
        print("Reason: Quantity and amount must be greater than zero.")
    elif requested_qty > available_stock:
        print("\nOrder Status: REJECTED")
        print(
            f"Reason: Insufficient stock (requested: {requested_qty}, available: {available_stock})."
        )
    else:
        # 3. Onay ve İndirim Kontrolleri
        discount = 0.0

        # En az 500 TRY ve üye olma şartı
        if is_member and amount >= 500.0:
            discount = 0.10
            approval_reason = "10% member discount applied (order >= 500 TRY)."
        elif is_member and amount < 500.0:
            approval_reason = (
                "Approved without discount (member threshold not reached)."
            )
        else:
            approval_reason = "Approved without discount (non-member customer)."

        final_price = amount * (1.0 - discount)

        # Çıktıları yazdır
        print("\nOrder Status: APPROVED")
        print(f"Reason: {approval_reason}")
        print(f"Final Price: {final_price:.2f} TRY")


if __name__ == "__main__":
    main()
