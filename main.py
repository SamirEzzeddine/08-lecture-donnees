"""
Data reading and basic list operations.

This module reads numerical data from a CSV file (semicolon separated)
and provides simple functions to manipulate lists of integers.
"""

#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires


def read_data(filename):
    """Retourne le contenu du fichier <filename>.

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    data = []

    with open(filename, mode="r", encoding="utf8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            data.append([int(x) for x in line.split(";")])

    return data


def get_list_k(data, k):
    """Retourne la k-ième liste."""
    return data[k]


def get_first(l):
    """Retourne le premier élément de la liste."""
    return l[0]


def get_last(l):
    """Retourne le dernier élément de la liste."""
    return l[-1]


def get_max(l):
    """Retourne le maximum de la liste."""
    return max(l)


def get_min(l):
    """Retourne le minimum de la liste."""
    return min(l)


def get_sum(l):
    """Retourne la somme des éléments de la liste."""
    return sum(l)


#### Fonction principale


def main():
    """Teste les fonctions secondaires."""
    data = read_data(FILENAME)

    for i, lst in enumerate(data[:5]):
        print(i, lst)

    k = 37
    lk = get_list_k(data, k)
    print("k =", k)
    print("list:", lk)
    print("first:", get_first(lk))
    print("last:", get_last(lk))
    print("max:", get_max(lk))
    print("min:", get_min(lk))
    print("sum:", get_sum(lk))


if __name__ == "__main__":
    main()
