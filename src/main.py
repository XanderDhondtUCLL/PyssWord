from Pasgenerator import *

def main():
    print("it works!")
    pasgenerator = Pasgenerator()
    pas_length = input("Length of password? ")
    if pas_length != "":
        pasgenerator.length = pas_length
    
    print(pasgenerator.length)




if __name__ == "__main__":
    main()