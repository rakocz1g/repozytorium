miesiac = int(input("Podaj numer miesiąca (od 1 do 12): "))
dzien = int(input("Podaj numer dnia: "))
dni_w_miesiacu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if miesiac < 1 or miesiac > 12:
   print("Podaj poprawny numer miesiąca (od 1 do 12).")
else:
   if dzien < 1 or dzien > dni_w_miesiacu[miesiac - 1]:
       print("Podaj poprawny numer dnia dla wybranego miesiąca.")
   else:
       print("Daty danego miesiąca:")
       for d in range(1, dni_w_miesiacu[miesiac - 1] + 1):
           if d == dzien:
               print("WYBRANA PRZEZ CIEBIE")
               break
           else:
               print(f"2024/{miesiac:02}/{d:02}")
       else:
           print("DATA SPOZA ZAKRESU")
