"""
Generators and Iterators Exercises - Day 2.

Practice creating generators with yield, using yield from, and processing data streams.
The functions below need to be implemented using generators.

Your task:
1. Implement each function as a generator using yield
2. Add proper type hints to all functions
3. Complete the docstrings with :param, :type, :yield, :rtype annotations
4. Ensure your code passes Ruff linting

Run the tests with: pytest tests/test_02_generators_iterators.py
"""


from typing import Generator, Iterator, Iterable, List, Any, Dict


# Exercise 1: Basic Generators with yield
def fibonacci() -> Generator[int, None, None]:
    """
    Generate Fibonacci sequence indefinitely.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def countdown(n: int) -> Generator[int, None, None]:
    """
    Generate countdown from n to 1.

    :param n: The starting number.
    :type n: int
    :yield: The next number in the countdown sequence.
    :rtype: Generator[int, None, None]

    Example:
        >>> list(countdown(5))
        [1-5]
    """
    while n > 0:
        yield n    # Entrega el número actual
        n -= 1     # Resta 1 y "pausa" hasta la siguiente llamada


def infinite_sequence(start: int) -> Generator[int, None, None]:
    """
    Generate infinite sequence starting from start.

    :param start: The starting integer.
    :type start: int
    :yield: The next integer in the sequence.
    :rtype: Generator[int, None, None]

    Example:
        >>> gen = infinite_sequence(10)
        >>> [next(gen) for _ in range(5)]
    """
    current = start
    while True:
        yield current
        current += 1


# Exercise 2: Generators for Data Processing
def chunk_data(data: Iterable[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """
    Split data into chunks of specified size.

    :param data: The input sequence or iterable.
    :type data: Iterable[Any]
    :param chunk_size: The size of each chunk.
    :type chunk_size: int
    :yield: A list representing a chunk of data.
    :rtype: Generator[List[Any], None, None]

    Example:
        >>> list(chunk_data([1-5], 2))
        [[1, 2], [3, 4], [5]]
    """
    chunk = []
    for item in data:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk      # Entregamos el paquete completo
            chunk = []       # Vaciamos para el siguiente
    
    # Si sobraron datos al final (ej: el [5] del ejemplo), los entregamos también
    if chunk:
        yield chunk


def filter_even(numbers: Iterable[int]) -> Generator[int, None, None]:
    """
    Filter only even numbers from an iterable.

    :param numbers: Input iterable of integers.
    :type numbers: Iterable[int]
    :yield: The next even number found.
    :rtype: Generator[int, None, None]

    Example:
        >>> list(filter_even([1-6]))
        [2, 4, 6]
    """
    for num in numbers:
        if num % 2 == 0:
            yield num


def square_numbers(numbers: Iterable[int]) -> Generator[int, None, None]:
    """
    Square each number from an iterable.

    :param numbers: Input iterable of integers.
    :type numbers: Iterable[int]
    :yield: The square of the next number.
    :rtype: Generator[int, None, None]

    Example:
        >>> list(square_numbers([1-4]))
        [1, 4, 7, 8]
    """
    for num in numbers:
        yield num ** 2



# Exercise 3: yield from
def chain_iterables(*iterables: Iterable[Any]) -> Generator[Any, None, None]:
    """
    Chain multiple iterables into a single generator.

    :param iterables: Variable number of iterable objects.
    :type iterables: Iterable[Any]
    :yield: The next element from the current iterable.
    :rtype: Generator[Any, None, None]

    Example:
        >>> list(chain_iterables([1, 2], [3, 4], [5, 6]))
        [1-6]
    """
    # *iterables recoge todos los argumentos en una tupla.
    # Recorremos cada iterable y delegamos la entrega con 'yield from'.
    for it in iterables:
        yield from it


def flatten_nested_list(nested_list: Iterable[Iterable[Any]]) -> Generator[Any, None, None]:
    """
    Flatten a nested list (one level deep).

    :param nested_list: A list (or iterable) of lists.
    :type nested_list: Iterable[Iterable[Any]]
    :yield: The next element from the sublists.
    :rtype: Generator[Any, None, None]

    Example:
        >>> list(flatten_nested_list([[1, 2], [3, 4], [5]]))
        [1-5]
    """
    # Iteramos sobre la lista principal
    for sublist in nested_list:
        # Delegamos la iteración de la sublista a Python
        yield from sublist


def read_multiple_sources(sources: Iterable[Iterable[Any]]) -> Generator[Any, None, None]:
    """
    Read data from multiple sources (lists) sequentially.

    :param sources: An iterable containing multiple data sources (lists).
    :type sources: Iterable[Iterable[Any]]
    :yield: The next item from the current source.
    :rtype: Generator[Any, None, None]

    Example:
        >>> sources = [['a', 'b'], ['c', 'd'], ['e']]
        >>> list(read_multiple_sources(sources))
        ['a', 'b', 'c', 'd', 'e']
    """
    # Funciona igual que flatten, pero conceptualmente es para orquestar fuentes de datos
    for source in sources:
        yield from source


# Exercise 4: Streaming Data Processing
def read_lines_stream(lines: Iterable[str]) -> Generator[str, None, None]:
    """
    Stream lines one at a time (simulates file reading).

    :param lines: Input iterable of strings (lines).
    :type lines: Iterable[str]
    :yield: The next line.
    :rtype: Generator[str, None, None]

    Example:
        >>> lines = ['line1', 'line2', 'line3']
        >>> list(read_lines_stream(lines))
        ['line1', 'line2', 'line3']
    """
    for line in lines:
        yield line


# TODO: Add type hints and implement using yield
def process_csv_stream(csv_data: Iterable[List[str]]) -> Generator[Dict[str, str], None, None]:
    """
    Process CSV data stream and yield dictionaries.

    :param csv_data: Iterable of rows (lists of strings).
    :type csv_data: Iterable[List[str]]
    :yield: Dictionary mapping headers to values for each row.
    :rtype: Generator[Dict[str, str], None, None]

    Example:
        >>> csv_data = [['name', 'age'], ['Alice', '30']]
        >>> list(process_csv_stream(csv_data))
        [{'name': 'Alice', 'age': '30'}]
    """
    # 1. Convertimos a iterador para poder extraer la cabecera
    # sin cargar todo en memoria (si fuera un archivo real).
    iterator = iter(csv_data)
    
    try:
        # 2. Consumimos solo la primera fila (headers)
        headers = next(iterator)
    except StopIteration:
        return  # Si está vacío, terminamos
        
    # 3. Iteramos sobre el RESTO de filas
    for row in iterator:
        # zip combina headers y row: ('name', 'Alice'), ('age', '30')
        yield dict(zip(headers, row))


# TODO: Add type hints and implement using yield
def running_average(numbers: Iterable[float]) -> Generator[float, None, None]:
    """
    Calculate running average of numbers stream.

    :param numbers: Iterable of numbers.
    :type numbers: Iterable[float]
    :yield: The current average after processing each number.
    :rtype: Generator[float, None, None]

    Example:
        >>> list(running_average([1-4]))
        [10.0, 15.0, 20.0, 25.0]
    """
    total = 0.0
    count = 0
    for num in numbers:
        total += num
        count += 1
        yield total / count


# Exercise 5: Advanced Generator Patterns
def take(iterable: Iterable[Any], n: int) -> Generator[Any, None, None]:
    """
    Take first n items from an iterable.

    :param iterable: The input sequence.
    :type iterable: Iterable[Any]
    :param n: Number of items to take.
    :type n: int
    :yield: The next item up to n items.
    :rtype: Generator[Any, None, None]

    Example:
        >>> list(take(range(100), 5))
        [1-4]
    """
    count = 0
    for item in iterable:
        if count >= n:
            break  # Cortamos el grifo cuando llegamos a n
        yield item
        count += 1


def drop(iterable: Iterable[Any], n: int) -> Generator[Any, None, None]:
    """
    Drop first n items from an iterable, yield the rest.

    :param iterable: The input sequence.
    :type iterable: Iterable[Any]
    :param n: Number of items to skip.
    :type n: int
    :yield: The remaining items after skipping n.
    :rtype: Generator[Any, None, None]

    Example:
        >>> list(drop(range(10), 5))
        [5-9]
    """
    # enumerate nos da (índice, valor) automáticamente
    for i, item in enumerate(iterable):
        if i >= n:
            yield item


def sliding_window(iterable: Iterable[Any], window_size: int) -> Generator[List[Any], None, None]:
    """
    Generate sliding windows of specified size.

    :param iterable: The input sequence.
    :type iterable: Iterable[Any]
    :param window_size: The size of the window.
    :type window_size: int
    :yield: A list representing the current window.
    :rtype: Generator[List[Any], None, None]

    Example:
        >>> list(sliding_window([1-5], 3))
        [[1-3], [2-4], [3-5]]
    """
    buffer = []
    for item in iterable:
        buffer.append(item)
        # Si el buffer excede el tamaño, quitamos el más viejo (el primero)
        if len(buffer) > window_size:
            buffer.pop(0)
        
        # Si el buffer está lleno, entregamos una copia
        if len(buffer) == window_size:
            yield list(buffer)
