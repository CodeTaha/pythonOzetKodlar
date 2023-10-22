from functools import reduce
import os


def veriTurleri():
    # Veritipi Çıktısı: String
    x = "Hello World"
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Tam Sayı
    x = 50
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Ondalıklı Sayı
    x = 60.5
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Karmaşık
    x = 3j
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Liste
    x = ["geeks", "for", "geeks"]
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Demet
    x = ("geeks", "for", "geeks")
    print(x)
    print(type(x))

    # belirli aralıkta bulunan sayıları göstermek için kullanılır.
    x = range(10)
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Sözlük
    x = {"name": "Suraj", "age": 24}
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Dize
    x = {"geeks", "for", "geeks"}
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Değiştirilemez-Kıstlanmış Dize
    x = frozenset({"geeks", "for", "geeks"})
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Mantıksal Değişken
    x = True
    print(x)
    print(type(x))

    # 8 adet bit'ten oluşan bir birimdir.
    x = b"Geeks"
    print(x)
    print(type(x))

    # bytes veri tipinin aksine, üzerinde değişiklik yapılabilen bir veri tipidir
    x = bytearray(4)
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Bellek Görünümü
    x = memoryview(bytes(6))
    print(x)
    print(type(x))

    # Veritipi Çıktısı: Tipsiz
    x = None
    print(x)
    print(type(x))


def printFonksiyonu():
    # python'da Hello World Yazdırma
    print("Hello World")

    # ends the output with a space
    print("Welcome to", end=' ')
    print("GeeksforGeeks", end=' ')

    # code for disabling the softspace feature
    print('09', '12', '2016', sep='-')

    # another example
    print('Example', 'geeksforgeeks', sep='@')


def kullaniciVerisiAlma():
    # Python program showing
    # a use of input()

    val = input("Enter your value: ")
    print(val)


def yorumSatirinaAlma():
    # Single Line comment

    # Python program to demonstrate
    # multiline comments

    """ Python program to demonstrate
    multiline comments"""

    name = "geeksforgeeks"
    print(name)


def operatorler():
    # Examples of Arithmetic Operator
    a = 9
    b = 4

    # Toplamı
    ekle = a + b

    # Farkı
    sub = a - b

    # Çarpımı
    mul = a * b

    # Modu
    mod = a % b

    # Karesi
    p = a ** b

    # print results
    print(ekle)
    print(sub)
    print(mul)
    print(mod)
    print(p)

    # Karşılaştırma Operatörleri
    a = 13
    b = 33

    # a > b is False
    print(a > b)

    # a < b is True
    print(a < b)

    # a == b is False
    print(a == b)

    # a != b is True
    print(a != b)

    # a >= b is False
    print(a >= b)

    # a <= b is True
    print(a <= b)

    # Mantıksal Operatörler
    a = True
    b = False

    # Print a and b is False
    print(a and b)

    # Print a or b is True
    print(a or b)

    # Print not an is False
    print(not a)

    # Bitsel Operatörler
    a = 10
    b = 4

    # Print bitwise AND operation
    print(a & b)

    # Print bitwise OR operation
    print(a | b)

    # Print bitwise NOT operation
    print(~a)

    # print bitwise XOR operation
    print(a ^ b)

    # print bitwise right shift operation
    print(a >> 2)

    # print bitwise left shift operation
    print(a << 2)


def dizeDilimleme():
    # Creating a String
    String1 = "GeeksForGeeks"
    print("Initial String: ")
    print(String1)

    # Printing 3rd character
    print("\nSlicing characters from 3-12: ")
    print(String1[3])

    # Printing characters between
    # 3rd and 2nd last character
    print("\nSlicing characters between " +
          "3rd and 2nd last character: ")
    print(String1[3:-2])


def kosulluIfadeler():
    # python program to illustrate If else statement

    i = 20
    if i < 15:
        print("i is smaller than 15")
    else:
        print("i is greater than 15")
    print("i'm not in if and not in else Block")


def donguler():
    # Python program to illustrate
    # Iterating over a list
    list = ["geeks", "for", "geeks"]

    for i in list:
        print(i)

    # Python program to illustrate
    # while loop
    count = 0
    while count < 3:
        count = count + 1
        print("Hello Geek")


def listeleme():
    Var = ["Geeks", "for", "Geeks"]
    print(Var)

    # Using list comprehension to iterate through loop
    List = [character for character in [1, 2, 3]]

    # Displaying list
    print(List)


def sozluk():
    Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    print(Dict)

    # Lists to represent keys and values
    keys = ['a', 'b', 'c', 'd', 'e']
    values = [1, 2, 3, 4, 5]

    # but this line shows dict comprehension here
    myDict = {k: v for (k, v) in zip(keys, values)}

    # We can use below too
    # myDict = dict(zip(keys, values))

    print(myDict)


def tupleLar():
    var = ("Geeks", "for", "Geeks")
    print(var)


def kume():
    var = {"Geeks", "for", "Geeks"}
    print(var)


# A simple Python function
def fonksiyon():
    print("Welcome to GFG")


# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


# Python program to
# demonstrate return statement
def add(a, b):
    # returning sum of a and b
    return a + b


def is_true(a):
    # returning boolean of a
    return bool(a)


def rangeFonksiyonu():
    # print first 5 integers
    # using python range() function
    for i in range(5):
        print(i, end=" ")
    print()


# Return double of n
def addition(n):
    return n + n


# function that filters vowels
def birFonksiyon(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False


def azaltma():
    nums = [1, 2, 3, 4]
    ans = reduce(lambda x, y: x + y, nums)
    print(ans)


def pyLambda():
    calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

    print(calc(20))


def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


def tryExcept():
    a = [1, 2, 3]
    try:
        print("Second element = %d" % (a[1]))

        # Throws error since there are only 3 elements in array
        print("Fourth element = %d" % (a[3]))

    except:
        print("An error occurred")


def dosyaIslemleri():
    def create_file(filenamesss):
        try:
            with open(filenamesss, 'w') as f:
                f.write('Hello, world!\n')
            print("File " + filenamesss + " created successfully.")
        except IOError:
            print("Error: could not create file " + filenamesss)

    def read_file(filenameson):
        try:
            with open(filenameson, 'r') as f:
                contents = f.read()
                print(contents)
        except IOError:
            print("Error: could not read file " + filenameson)

    def append_file(filenameing, text):
        try:
            with open(filenameing, 'a') as f:
                f.write(text)
            print("Text appended to file " + filenameing + " successfully.")
        except IOError:
            print("Error: could not append to file " + filenameing)

    def rename_file(filenamer, renew_filename):
        try:
            os.rename(filenamer, renew_filename)
            print("File " + filenamer + " renamed to " +
                  renew_filename + " successfully.")
        except IOError:
            print("Error: could not rename file " + filenamer)

    def delete_file(filenameses):
        try:
            os.remove(filenameses)
            print("File " + filenameses + " deleted successfully.")
        except IOError:
            print("Error: could not delete file " + filenameses)

    if __name__ == '__main__':
        filename = "example.txt"
        new_filename = "new_example.txt"

        create_file(filename)
        read_file(filename)
        append_file(filename, "This is some additional text.\n")
        read_file(filename)
        rename_file(filename, new_filename)
        read_file(new_filename)
        delete_file(new_filename)


def OOP():
    class Car:
        def __init__(self, make, model, year):
            self._make = make  # protected attribute
            self.__model = model  # private attribute
            self.year = year  # public attribute

        def get_make(self):
            return self._make

        def set_model(self, model):
            self.__model = model

        def get_model(self):
            return self.__model

    my_car = Car("Toyota", "Corolla", 2022)

    print(my_car.get_make())  # Accessing protected attribute
    my_car.set_model("Camry")  # Modifying private attribute
    print(my_car.get_model())  # Accessing modified private attribute
    print(my_car.year)  # Accessing public attribute


veriTurleri()
print("-----------------------------------------------------------------------------------")
printFonksiyonu()
print("-----------------------------------------------------------------------------------")
kullaniciVerisiAlma()
print("-----------------------------------------------------------------------------------")
yorumSatirinaAlma()
print("-----------------------------------------------------------------------------------")
operatorler()
print("-----------------------------------------------------------------------------------")
dizeDilimleme()
print("-----------------------------------------------------------------------------------")
kosulluIfadeler()
print("-----------------------------------------------------------------------------------")
donguler()
print("-----------------------------------------------------------------------------------")
listeleme()
print("-----------------------------------------------------------------------------------")
sozluk()
print("-----------------------------------------------------------------------------------")
tupleLar()
print("-----------------------------------------------------------------------------------")
kume()
print("-----------------------------------------------------------------------------------")
fonksiyon()
print("-----------------------------------------------------------------------------------")
evenOdd(2)
evenOdd(3)
print("-----------------------------------------------------------------------------------")
# calling function
res = add(2, 3)
print("Result of add function is {}".format(res))

res = is_true(2 < 5)
print("\nResult of is_true function is {}".format(res))
print("-----------------------------------------------------------------------------------")
rangeFonksiyonu()
print("-----------------------------------------------------------------------------------")
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
print("-----------------------------------------------------------------------------------")
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(birFonksiyon, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)
print("-----------------------------------------------------------------------------------")
azaltma()
print("-----------------------------------------------------------------------------------")
pyLambda()
print("-----------------------------------------------------------------------------------")
# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
print("-----------------------------------------------------------------------------------")
tryExcept()
