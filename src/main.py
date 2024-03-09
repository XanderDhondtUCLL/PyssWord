from Pasgenerator import *

def main():
    print("it works!")
    pasgenerator = Pasgenerator()
    pas_len = input("Length of password? ")

    if pas_len != "":
        pasgenerator.length = int(pas_len)



    print(pasgenerator.length)

    pasgenerator.generate()
    print(pasgenerator.password)


if __name__ == "__main__":
    main()