def topla(int1, int2):
    try:
        summary = int1 + int2
        print("İşlem Sonucu:", summary)
    except:
        print("Lütfen sadece sayı giriniz!")

def cikart(int1, int2):
    try:
        summary = int1 - int2
        print("İşlem Sonucu:", summary)
    except:
        print("Lütfen sadece sayı giriniz!")

def carp(int1, int2):
    try:
        summary = int1 * int2
        print("İşlem Sonucu:", summary)
    except:
        print("Lütfen sadece sayı giriniz!")

def bol(int1, int2):
    try:
        summary = int1 // int2
        print("İşlem Sonucu:", summary)
    except:
        print("Lütfen sadece sayı giriniz!")

try:
    while True:
        print("""
1) Toplama
2) Çıkarma
3) Çarpma
4) Bölme
5) Çıkış
        """)
        try:
            secenek = int(input("Seçenek: "))
            if not secenek:
                print("Lütfen bir işlem girin.")
            elif (secenek == 1):
                int1 = int(input("Değer 1: "))
                int2 = int(input("Değer 2: "))
                topla(int1=int1, int2=int2)
            elif (secenek == 2):
                int1 = int(input("Değer 1: "))
                int2 = int(input("Değer 2: "))
                cikart(int1=int1, int2=int2)
            elif (secenek == 3):
                int1 = int(input("Değer 1: "))
                int2 = int(input("Değer 2: "))
                carp(int1=int1, int2=int2)
            elif (secenek == 4):
                int1 = int(input("Değer 1: "))
                int2 = int(input("Değer 2: "))
                bol(int1=int1, int2=int2)
            elif (secenek == 5):
                print("Görüşmek Üzere!")
                break
            else:
                print("İşlem Tanınamadı!")
        except:
            print("Lütfen sadece sayı girin!")
except:
    print("Bir hata tespit edildi! İletişim için Instagram: @cyrstudios")
