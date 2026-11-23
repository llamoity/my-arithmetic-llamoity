"""Fonctions arithmétiques."""


def gcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur de deux entiers.

    Utilise l'algorithme d'Euclide. Le résultat est toujours positif ou nul.

    Parameters
    ----------
    a : int
        Premier entier.
    b : int
        Second entier.

    Returns
    -------
    int
        Le PGCD de `a` et `b` ; ``gcd(0, 0)`` vaut ``0``.

    Examples
    --------
    >>> gcd(12, 18)
    6
    >>> gcd(-4, 6)
    2
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
