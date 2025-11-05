class InvalidQuantityError(Exception):
    """Miktar sıfır veya negatif girildiğinde fırlatılır."""
    pass

class ProductNotFoundError(Exception):
    """Ürün bulunamadığında fırlatılır."""
    pass


class Inventory:
    def __init__(self):
        self.items = {}

    def add_product(self, name, quantity):
        try:
            if not isinstance(name, str):
                raise TypeError("Ürün adı metin olmalı.")
            if quantity <= 0:
                raise InvalidQuantityError("Miktar pozitif olmalı!")
            
            self.items[name] = self.items.get(name, 0) + quantity
            print(f"{name} başarıyla eklendi. Yeni miktar: {self.items[name]}")
        
        except InvalidQuantityError as e:
            print("Geçersiz miktar hatası:", e)
        except TypeError as e:
            print("Tip hatası:", e)
        except Exception as e:
            print("Başka bir hata:", e)
        else:
            print("Hata olmadı, işlem başarıyla tamamlandı.")
        finally:
            print("İşlem tamamlandı.")
    

    def remove_product(self, name, quantity):
        pass

    def show_stock(self):
        print("=== Mevcut Stok ===")
        if not self.items:
            print("Stokta ürün yok.")
        else:
            for k, v in self.items.items():
                print(f"{k}: {v}")


def main():
    inv = Inventory()

    while True:
        print("\nMenü: 1-Ekle 2-Sil  3-Listele  0-Çıkış")
        choice = input("Seçiminiz: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Hata: Menü seçimi sayı olmalı.")
            continue

        if choice == 0:
            print("Program sonlandırıldı.")
            break

        elif choice == 1:
            name = input("Ürün adı: ")
            try:
                qty = int(input("Miktar: "))
            except ValueError:
                print("Hata: Miktar sayısal olmalı.")
                continue
            inv.add_product(name, qty)
        
        elif choice == 2:
            print('İşlem sizin tarafınızdan yapılacak')

        elif choice == 3:
            inv.show_stock()

        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    try:
        main()    
    except Exception as e:
        print("Ana program hatası:", e)
    finally:
        print("Program sonlandı.")

# Silme işlemi için 
# ilk olarak kullanıcıdan bir ürün ismi alınacak ve listede bu isim yoksa hata verilecek(ProductNotFoundError)
# ikinci olarak kullancıdan kaç adet sileceğine dair bilgi alınacak ve alınan değer sayısal değil ise hata verilecek
# üçüncü olarak silinen miktar var olan miktardan fazla ise veya eksi bir değer silinmeye çalışılıyorsa hata verilecek(InvalidQuantityError)
# son olarak ürünün miktarı silindikten sonra güncellenecek

