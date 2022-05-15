import sys

#definiujemy liczbe prob = 5
no_of_tries=5

#definujemy wyraz, ktory uzytkownik ma zgadnac w grze
word="kamila"

#stworzymy liste, do ktorej bedziemy dodawac litery podane przez uzytkownika
used_letters=[]

#stworzymy liste, ktora bedzie przestawiac zgadywany wyraz
user_word=[]

def find_indexes(word, letter):
    indexes = []
#petla for zawsze przeszukuje np. dany wyraz/liste itd, funkcja enumerate() podaje numer indeksu oraz litere, ktora jest przypisana do tego indeksu 
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game():
    print()
    print(user_word)
    print("Pozostało prób: ", no_of_tries)
    print("Uzyte litery: ", used_letters)
    print()

###

for _ in word:
    user_word.append("_")

#stworzymy petle while True, ktora bedzie wykonywac sie w nieskonczonosc. Nastepnie, bedziemy prosic uzytkownika o litere
#litery, ktore poda uzytkownik bedziemy dodawac do listy z uzytymi literami 
while True:
    letter=input("Podaj litere: ")
    used_letters.append(letter)
#sprawdzamy, czy litera podana przez uzytkownika znajduje sie w word - korzystamy z funkcji index, ktora zwraca nam indeks litery w wyrazie word, jezeli sie tam znajduje
#niemniej jednak, funkcja ta nie bedzie przydatna jezeli w word znajda sie wiecej niz jedna taka sama litera - funkcja bedzie podawac indeks jedynie pierwszej napotkanej litery w wyrazie
#wtedy najlepszym rozwiazaniem bedzie stworzenie wlasnej funkcji zatytulowanej find_indexes, ktora bedzie przyjmowac dwa argumenty - nasze slowo i nasze litery
    # print(word.index(letter))

    found_indexes=find_indexes(word, letter)

    if len(found_indexes) == 0:
        print(f"Nie ma takiej litery jak {letter}")
        no_of_tries-=1
         

        if no_of_tries== 0:
            print("Koniec gry :(")
            sys.exit(0)
    
    else:
        for index in found_indexes:
            user_word[index]=letter
    
    show_state_of_game()
       

#chcemy, aby lista stała się słowem to definiujemy sobie pusty string za pomocą cudzysłowa i następnie korzystamy z funkcji join.
#zeby porownac slowo z listy z naszym word uzywamy IF
    if "".join(user_word) == word:
        print("Brawo, to jest to słowo!")
        sys.exit(0)     


    