##WEEK01
Student Name: Erdinç Kılıç
Student ID: 2404109060
Department: Management Information Systems
Course: Basic Programming
AI Tool Used: Chat GPT
Prompt Used: "Python ile kullanıcıdan isim, bölüm, yaş ve kariyer hedefi alıp ekrana düzenli bir öğrenci profili bastıran basit bir kod yazar mısın?"
What did you change? Girdi alırken değişken isimlerini kendi projemin akışına göre uyarladım ve çıktının ödev formatına tam uyması için print kısımlarını düzenledim.


##WEEK02
AI Tool Used: Chat GPT
Prompt Used: "Python'da sonsuz döngüyle çalışan bir öğrenci not hesaplama programı yazıyorum. Kullanıcı yanlışlıkla sayı yerine harf girerse programın çökmemesini nasıl yapabilirim
ve genel ortalamayı virgülden sonra 2 basamak olacak şekilde nasıl yuvarlayabilirim?"
What did you change? Kullanıcının sayı yerine harf girmesi durumunda kodun hata verip durmasını engellemek için try-except bloğu ekledim 
ve ortalama puanı :.2f ile virgülden sonra iki basamağa yuvarlayacak şekilde düzenledim.


## Week 03
AI Tool Used: Gemini
Prompt Used: This week you will combine everything you have learned so far: input, type conversion, f-strings, loops, and this week's new topic: conditions (if / elif / else, and / or, boundaries and input validation)
What did you change? I used the `.strip()` method on user inputs to prevent accidental spaces from failing validation and formatted the final outputs to two decimal places.
Tests
 1. Input: Name: Erdinc, Age: 5, Day: weekend, Student: no -> Result: Can: 0.00 TRY (Free) [Boundary: Age < 6]
 2. Input: Name: Lütfü, Age: 12, Day: weekday, Student: yes -> Result: Deniz: 120.00 TRY (Child) [Boundary: Child upper limit]
  3. Input: Name: Hilmi, Age: 21, Day: weekday, Student: yes -> Result: Mert: 140.00 TRY (Student) [Boundary: Student upper age limit]
Why does the order of the rules matter?
If the Student rule comes first, a 10-year-old student gets only a 30% discount instead of the 40% child discount. The order matters because Python stops at the first true condition, so we must check bigger discounts first.
