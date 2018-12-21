liste = []
for i in range (5):
    x = input("Bir sayı giriniz:")
    liste.append(x)
liste.sort(reverse=True)
print(liste)

dosya=open ("221120181047_sonuc.txt","w")
for m in range (5):
    dosya.write(liste[m]+" ")