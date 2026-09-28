# girdileri alma
name = input("Adınızı girin: ")
while not name:
  print("Hata: İsim alanı boş bırakılamaz!")
  name = input("Lütfen geçerli bir isim girin: ")
student_id = input("Öğrenci numanızı girin: ")
department = input("Bölmünüzü girin: ")
github_username = input("GitHub kullanıcı adını giriniz: ")
goal = input("Programlama hedefinizi girin: ")

# kartını ekrana bastırma
print("\n" + "=" * 30)
print("STUDENT CARD")
print("=" * 30)
print(f"Name : {name}")
print(f"Student ID : {student_id}")
print(f"Department : {department}")
print(f"GitHub : {github_username}")
print(f"Goal : {goal}")
print("=" * 30)

# I added check for a name to warn the user if the name field is left empty.
