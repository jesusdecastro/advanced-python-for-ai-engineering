"""
Comprehensions Exercises - Day 2.

Practice list, dict, and set comprehensions.
The functions below need to be implemented using comprehensions.

Your task:
1. Implement each function using the appropriate comprehension type
2. Add proper type hints to all functions
3. Complete the docstrings with :param, :type, :return, :rtype annotations
4. Ensure your code passes Ruff linting

Run the tests with: pytest tests/test_01_comprehensions.py
"""

# TODO: Import necessary types from typing module
# Hint: You'll need List, Dict, Set


# Exercise 1: Basic List Comprehensions
from typing import List, Dict, Set, Any  # Añadimos Dict y Any

def get_squares(n: int) -> List[int]:  # 2. Tipamos la entrada (int) y la salida (Lista de enteros)
    """Generate a list of squares from 1 to n.

    :param n: The maximum number to square.
    :type n: int
    :return: A list of squared numbers from 1 to n.
    :rtype: List[int]

    Example:
        >>> get_squares(5)
        [1-5]
    """
    # 3. CORRECCIÓN LÓGICA:
    # No puedes iterar sobre un número ("in n"). 
    # Usamos range(1, n + 1) para ir desde el 1 hasta n incluido.
    return [number ** 2 for number in range(1, n + 1)]


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filter only even numbers from a list.

    :param numbers: The input list of integers.
    :type numbers: List[int]
    :return: A list containing only the even numbers.
    :rtype: List[int]

    Example:
        >>> filter_even_numbers([1-6])
        [2, 4, 6]
    """
    # Usamos comprensión de lista con un 'if' al final para filtrar
    return [num for num in numbers if num % 2 == 0]


def uppercase_strings(strings: List[str]) -> List[str]:
    """
    Convert all strings in a list to uppercase.

    :param strings: The list of strings to convert.
    :type strings: List[str]
    :return: A new list with all strings in uppercase.
    :rtype: List[str]

    Example:
        >>> uppercase_strings(['hello', 'world'])
        ['HELLO', 'WORLD']
    """
    # Aplicamos .upper() a cada elemento 's' de la lista
    return [s.upper() for s in strings]


# Exercise 2: Dict Comprehensions

def create_number_to_cube_dict(n: int) -> Dict[int, int]:
    """
    Create a dictionary mapping numbers 1 to n to their cubes.

    :param n: The maximum number.
    :type n: int
    :return: A dictionary with numbers as keys and their cubes as values.
    :rtype: Dict[int, int]

    Example:
        >>> create_number_to_cube_dict(3)
        {1: 1, 2: 8, 3: 27}
    """
    # Sintaxis: {clave: valor for variable in rango}
    return {x: x**3 for x in range(1, n + 1)}


def invert_dictionary(original: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Invert a dictionary (swap keys and values).

    :param original: The dictionary to invert.
    :type original: Dict[Any, Any]
    :return: A new dictionary with keys and values swapped.
    :rtype: Dict[Any, Any]

    Example:
        >>> invert_dictionary({'a': 1, 'b': 2})
        {1: 'a', 2: 'b'}
    """
    # Usamos .items() para obtener clave (k) y valor (v), y los invertimos
    return {v: k for k, v in original.items()}


def filter_dict_by_value(data: Dict[str, int], threshold: int) -> Dict[str, int]:
    """
    Filter dictionary to only include items where value > threshold.

    :param data: The input dictionary.
    :type data: Dict[str, int]
    :param threshold: The minimum value to keep.
    :type threshold: int
    :return: A filtered dictionary.
    :rtype: Dict[str, int]

    Example:
        >>> filter_dict_by_value({'a': 10, 'b': 5, 'c': 15}, 7)
        {'a': 10, 'c': 15}
    """
    # Añadimos el 'if' al final para filtrar
    return {k: v for k, v in data.items() if v > threshold}


# Exercise 3: Set Comprehensions
def get_unique_characters(text: str) -> Set[str]:
    """
    Extract unique characters from a string (excluding spaces).

    :param text: The input string.
    :type text: str
    :return: A set of unique characters.
    :rtype: Set[str]

    Example:
        >>> get_unique_characters('hello world')
        {'h', 'e', 'l', 'o', 'w', 'r', 'd'}
    """
    # Usamos { } para crear un conjunto.
    # Filtramos los espacios con el 'if'.
    return {char for char in text if char != ' '}


def get_unique_numbers(numbers: List[int]) -> Set[int]:
    """
    Get unique numbers from a list with duplicates.

    :param numbers: List of integers that may contain duplicates.
    :type numbers: List[int]
    :return: A set containing only unique integers.
    :rtype: Set[int]

    Example:
        >>> get_unique_numbers([1-4])
        {1, 2, 3, 4}
    """
    # Al convertir a set, los duplicados desaparecen automáticamente.
    return {num for num in numbers}


def get_word_lengths(words: List[str]) -> Set[int]:
    """
    Create a set of unique word lengths.

    :param words: List of words.
    :type words: List[str]
    :return: A set of unique lengths found.
    :rtype: Set[int]

    Example:
        >>> get_word_lengths(['cat', 'dog', 'bird', 'fish'])
        {3, 4}
    """
    # Calculamos la longitud len() de cada palabra.
    # Si dos palabras miden lo mismo (ej: cat, dog -> 3), el set solo guarda un 3.
    return {len(word) for word in words}


# Exercise 4: Advanced Comprehensions
def flatten_matrix(matrix: List[List[int]]) -> List[int]:
    """
    Flatten a 2D matrix into a 1D list.

    :param matrix: A list of lists of integers.
    :type matrix: List[List[int]]
    :return: A single flattened list of integers.
    :rtype: List[int]

    Example:
        >>> flatten_matrix([[1, 2], [3, 4], [5, 6]])
        [1-6]
    """
    # Doble bucle en una línea: "para cada fila en la matriz, para cada número en esa fila"
    return [num for row in matrix for num in row]


def word_frequency(words: List[str]) -> Dict[str, int]:
    """
    Create a dictionary with word frequencies.

    :param words: List of words to count.
    :type words: List[str]
    :return: Dictionary where keys are words and values are their counts.
    :rtype: Dict[str, int]

    Example:
        >>> word_frequency(['apple', 'banana', 'apple'])
        {'apple': 2, 'banana': 1}
    """
    # Usamos set(words) para no contar la misma palabra varias veces.
    # words.count(w) cuenta cuántas veces aparece 'w'.
    return {word: words.count(word) for word in set(words)}


def extract_names_from_users(users: List[Dict[str, Any]]) -> List[str]:
    """
    Extract names from a list of user dictionaries (only active users).

    :param users: List of user dictionaries containing 'name' and 'active' keys.
    :type users: List[Dict[str, Any]]
    :return: List of names of active users.
    :rtype: List[str]

    Example:
        >>> extract_names_from_users([{'name': 'Alice', 'active': True}])
        ['Alice']
    """
    # 1. Iteramos sobre 'user' en 'users'
    # 2. Filtramos: if user.get('active') es True
    # 3. Extraemos: user['name']
    return [user['name'] for user in users if user.get('active') is True]
