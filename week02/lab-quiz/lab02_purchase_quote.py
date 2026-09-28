# 1. Ürün bilgilerini al
item1_name = input("1. Ürünün adını girin: ")
item1_qty = int(input("1. Ürünün adedini girin: "))
item1_price = float(input("1. Ürünün birim fiyatını girin (TL): "))

# 2. Ürün bilgilerini al
item2_name = input("2. Ürünün adını girin: ")
item2_qty = int(input("2. Ürünün adedini girin: "))
item2_price = float(input("2. Ürünün birim fiyatını girin (TL): "))

# Kargo ücreti ve vergi oranını al
delivery_fee = float(input("Kargo ücretini girin (TL): "))
tax_percent = float(input("Vergi yüzdesini girin (%10 için 10 yazın): "))

# Hesaplamaları yap
item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price
subtotal = item1_total + item2_total
tax_amount = subtotal * (tax_percent / 100.0)
final_total = subtotal + tax_amount + delivery_fee

# Biçimlendirilmiş çıktı
print("\n" + "=" * 35)
print("          FİYAT TEKLİFİ          ")
print("=" * 35)
print(f"{item1_name} ({item1_qty} x {item1_price:.2f} TL): {item1_total:.2f} TL")
print(f"{item2_name} ({item2_qty} x {item2_price:.2f} TL): {item2_total:.2f} TL")
print("-" * 35)
print(f"Ara Toplam:      {subtotal:.2f} TL")
print(f"Vergi (%{tax_percent:.1f}):     {tax_amount:.2f} TL")
print(f"Kargo Ücreti:    {delivery_fee:.2f} TL")
print("-" * 35)
print(f"Genel Toplam:    {final_total:.2f} TL")
print("=" * 35)
