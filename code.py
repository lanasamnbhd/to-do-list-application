todo_listesi=[]
def secenekler():
    print("to-do list uygulaması")
    print("1. görev ekle")
    print("2. görev sil")
    print("3. görevleri görüntüle")
    print("4.çıkış yap")
def gorev_ekle():
    yeniGorev=input("eklemek istediğiniz görevi yazınız:")
    todo_listesi.append(yeniGorev)
    print(f"'{yeniGorev}' görev olarak başarılı bir şekilde eklendi")

def gorev_sil():
    gorevNo=int(input("silmek istediğiniz görevin numarasını giriniz:"))
    if 1<=gorevNo<len(todo_listesi)+1:
        silinenGorev=todo_listesi.pop(gorevNo-1)
        print("görev başarıyla silindi")
    else:
        print("girdiğiniz sayıya uygun görev bulunamadı")

def gorev_goster():
    if not todo_listesi:
        print("yapılacak görev bulunamadı. yeni görev ekleme zamanııı!!!")
    else:
        print("görevler:\n")
        for i, gorev in enumerate(todo_listesi,1):
            print(f"{i}. {gorev}")

while True:
    secenekler()
    secim=int(input("yapmak istediğiniz işlemi seçin(1/2/3/4):"))
    if secim==1:
        gorev_ekle()
    elif secim==2:
        gorev_sil()
    elif secim==3:
        gorev_goster()
    elif secim==4:
        print("çıkış yapıldı...")
        break
    else:
        print("bir hata oluştu. lütfen tekrar1 deneyin.")
