# class Foydalanuvchi:
#     def __init__(self):
#         ism = input("Ismizi kiriting: ")
#         familiya = input("Familiyangizni kiriting: ")
#         email = input("Email kiriting: ")
#         self.ism = ism
#         self.familiya = familiya
#         self.email = email

#     def get_info(self):
#         return f"{self.ism}, {self.familiya}. email:{self.email}."

#     # def yosh_qosh(self, yosh):
#     #     self.yosh = yosh


# sariqdev = Foydalanuvchi()
# # sariqdev.yosh_qosh('15')
# print(sariqdev.get_info())


class YoshKategoriyasi:
    def __init__(self, yosh):
        self.yosh = yosh

    def yoshni_ajratish(self):
        if self.yosh > 0:
            if self.yosh <= 10:
                print("Siz bolasiz")
            elif self.yosh <= 16:
                print("Siz o'smirsiz")
            elif self.yosh > 16 and self.yosh <= 30:
                print("Siz eng zo'r yoshdasiz")
            elif self.yosh > 30 and self.yosh <= 45:
                print("Siz o'rta yoshsiz")
            else:
                print("Siz qariyapsiz")


while True:
    yosh = int(input("Yosh kiriting: "))
    obyekt = YoshKategoriyasi(yosh)
    obyekt.yoshni_ajratish()
    if yosh >= 0:
        davom_etaymi = input("Yana bilishni xohlaysizmi? 'ha' yoki 'yoq' ")
        if davom_etaymi == 'yoq':
            break
    else:
        print("To'g'ri yosh kiriting")









# class Foydalanuvchi:
#     def __init__(self,ism,familiya,email,yosh):
#         self.ism = ism
#         self.familiya = familiya
#         self.email = email
#         self.yosh = yosh

#     def yosh_aniqla(self):
#         if self.yosh < 7 :
#             return f"Hurmatli {self.ism} {self.familiya} Siz endi o'quvchi bo'lasiz :)"
#         if self.yosh < 18:
#             return f"Hurmatli {self.ism} {self.familiya} Siz o'quvchisiz."
#         else:
#             return f"Hurmatli {self.ism} {self.familiya} Siz o'quvchi emasiz."

# ism = input("Ismingizni kiriting: ")
# familiya = input("Familiyangizni kiriting: ")
# email = input("Emailingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))

# karimov = Foydalanuvchi(ism,familiya,email,yosh)
# print(karimov.yosh_aniqla())