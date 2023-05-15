def student_info(first_name, last_name, **kwargs):
    student = {"first_name": first_name, "last_name": last_name}
    for key, value in kwargs.items():
        student[key] = value
    return student
# y = {'age':23}
x = student_info('abdumannop', 'ibragimov', age=23)
# print(x)


def list_tugashi(royxat):
    natija = [royxat[0], royxat[-1]]
    return natija
    

a = [5, 10, 15, 20, 25]
# print(list_tugashi(a))


import random

def sontop():
    a = random.randint(0, 11)
    taxmin = 0
    
    while taxmin != a:
        taxmin = int(input("Raqam kiriting: "))
        if taxmin == a:
            print("topdiz")
        else:
            if taxmin > a:
                print("Komputer o'ylagan son kichiqroq")
            else:
                print("Komputer o'ylagan son kattaroq")
        
# sontop()
    

# def sontopkomp():
#     komp_oylagan_son = random.randint(0, 11)
#     kiritish = int(input("Raqam kiriting: "))
    
    
#     while komp_oylagan_son != kiritish:
        
#         if komp_oylagan_son == kiritish:
#             print("Kompyuter soningizni topdi")
#         else:
#             if kiritish > komp_oylagan_son:
#                 komp_oylagan_son = random.randint(kiritish, 11)
#                 continue
                
#             else:
#                 komp_oylagan_son = random.randint(0, kiritish)
#                 continue
        
# sontopkomp()
    

def game():
    

    # Set up initial range of possible numbers
    low = 1
    high = 100

    # Initialize number of attempts to 0
    attempts = 0

    # Computer makes first guess
    guess = (low + high) // 2

    # Loop until computer guesses correctly
    while True:
        print(f"Is your number {guess}?")
        response = input("Enter 'h' if your number is higher, 'l' if it's lower, or 'c' if it's correct: ")
        
        # If the guess is correct, break out of the loop
        if response == 'c':
            attempts += 1
            print(f"The computer guessed your number in {attempts} attempts!")
            break
        
        # If the guess is too high, set the new upper bound of the range
        elif response == 'h':
            high = guess - 1
            attempts += 1
        
        # If the guess is too low, set the new lower bound of the range
        elif response == 'l':
            low = guess + 1
            attempts += 1
        
        # Make a new guess based on the updated range
        guess = (low + high) // 2

# game()

# print("heelo")

# x = 10
# print(type(x))


# matn = "salom"
# print(type(matn))


# def salom_ber():
#     print("Assalom alaykum")

# print(type(salom_ber))

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def tanishtir(self):
        return (f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")

talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.tanishtir())