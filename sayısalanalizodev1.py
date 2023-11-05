import math
x=math.pi/5
n=int(input("bir sayi giriniz:"))
toplam=0
sign=1
for i in range(n):
   toplam =toplam+sign*(x**(2*i))/math.factorial(2*i)
   sign=(-1)*sign
   orijinaldeger=math.cos(x)
   print("yaklasık degeri",toplam)
   print("cos(x) ifadenin gercek degeri ",orijinaldeger)
   kesmehatasi=(orijinaldeger-toplam)
   print("kesme hatasi",kesmehatasi)
