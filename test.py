# Syntax Error
# return "Dönüş Cümlesi"

#Girinti Hatası
# def fun():
# return "DataCamp" 

#Sıfıra Bölme Hatası
#test = 1/0

#Try Except
# try:
#    print(x)
# except :
#    print("Hata Yakalandı")

#Çoklu Try Except
# try:
#    print(1/0)
# except ZeroDivisionError:
#    print("Sıfıra Bölemezsin")
# except:
#    print("Başka Bir Hata Var")

#Dosya Yükleme
# try:
#    with open('data.csv') as file:
#        read_data = file.read()
# except FileNotFoundError as fnf_error:
#    print(fnf_error)
#    print("Dosya Yüklenemedi")


#Try Except Else
# try:
#    result = 1/3
# except ZeroDivisionError as err:
#    print(err)
# else:
#    print(f"Cevap: {result}")

#Finally
# def divide(x,y):
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         print("Sıfıra Bölünemez")   
#     else:
#         print(f"Cevap: {result}")
#     finally:
#         print("Kod Tamamlandı")
# divide(1,0)
# divide(3,4)

#Raise ile Hata Fırlatmak
# value = 2_000
# if value > 1_000:      
#     raise Exception("1000'den büyük değer olamaz!")
# else:
#     print("Bir sıkıntı yok")

# if value > 1_000:      
#     raise ValueError("1000'den büyük değer olamaz!")
# else:
#     print("Bir sıkıntı yok")


#Fırlatılan hataları yakalamak
# value = 2_000
# try:
#     if value > 1_000:               
#         raise ValueError("1000'den büyük değer olamaz!")
#     else:
#         print("Bir sıkıntı yok")            
# except ValueError as e:
#         print(e)    


