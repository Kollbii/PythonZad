# Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym
# wymiarze n x n wypełnioną liczbami naturalnymi. Dla danej tablicy należy napisać
# funkcję, która zwraca liczbę par elementów, o określonym iloczynie, takich że
# elementy są odległe o jeden ruch skoczka szachowego.
# Wymiar tablicy powinien być definiowany przez użytkownika.

import random

n = int(input("Podaj rozmiar tablicy [n x n]:  "))
l = int(input("Podaj iloczyn do szukania: "))

# Randomowa tablica o rozmiarze nxn wypełniona losowymi liczbami z zakresu

def gener_tab(n):
    tab = [[0 for x in range(n)] for y in range(n)]     #dwuwymiarowa tablica wypełniona zerami
    for i in range (0, n):
        for j in range (0, n):
            tab[i][j] = random.randint(1,9)             #potencjalne zwiększenie zakresu liczb w tablicy
    return tab

# Ładnie wypisze w formie "szachownicy"

def draw_tab(tab):
    draw = ''    
    for i in range (0, len(tab)):
        for j in range (0, len(tab[i])):
            if(j == len(tab[i]) - 1):
                draw += ''.join(str(tab[i][j]))
                draw += ''.join("\n")
            else:
                draw += ''.join(str(tab[i][j]))
                draw += ''.join(" | ")
    return draw

# Sprawdza czy iloczyn tych par jest równy zadanemu iloczynowi

def check_multiplication(tab, i, j, x, y, l):
    if(tab[i][j] * tab[i+x][j+y] == l):
        return True
    return False

# Wyszukuje WSZYSTKIE możliwe przeskoki, podaje na wejście 'check_multiplication(...)'
# Zwraca tablicę WSZYSTKICH możliwych przeskoków o zadanym iloczynie ale z POWTÓRZENIAMI

def find_possible_pairs(tab, l):
    possible_pairs = []
    for i in range (0, len(tab)):
        for j in range(0, len(tab[i])):
            for x, y in _moves:

                if(i + x >= 0 and i + x < len(tab) and j + y >= 0 and j + y < len(tab)):
                    if(check_multiplication(tab, i, j, x, y, l)):
                        possible_pairs.append([tab[i][j],tab[i+x][j+y]])

    return possible_pairs

# No to tutaj wywalam te duplikaty bo zwykły set() na 2D array'u nie chciał działać :c

def remove_duplicates(tab):
    seen = set()
    new_tab = []
    for x in tab:
        a = tuple(x)
        if a not in seen:
            new_tab.append(x)
            seen.add(a)
    return new_tab


work_array = [
    [2,3,6,3,6],
    [7,2,9,4,7],
    [1,4,3,2,6],
    [7,6,8,5,7],
    [2,3,6,3,2]
]

_moves = [
    [1,2],  
    [2,1],  
    [-1,2],
    [-2,1],
    [-1,-2],
    [-2,-1],
    [1,-2],
    [2,-1]
]


print(draw_tab(gener_tab(n)))
print(remove_duplicates(find_possible_pairs(gener_tab(n), l)))

# print(draw_tab(work_array))
# print(find_possible_pairs(work_array, 12))
# print(remove_duplicates(find_possible_pairs(work_array, 12)))