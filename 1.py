liczba = int(input("Podaj liczbę całkowitą: "))
if liczba < 2:
   print("Podaj liczbę większą lub równą 2.")
else:
   print("Liczby pierwsze do", liczba, "to:", end=" ")
   for num in range(2, liczba + 1):
       czy_pierwsza = True
       for i in range(2, num):
           if num % i == 0:
               czy_pierwsza = False
               break
       if czy_pierwsza:
           print(num, end=" ")

           
