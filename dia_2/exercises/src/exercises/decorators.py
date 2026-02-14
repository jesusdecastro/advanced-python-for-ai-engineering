"""
Decorators Exercises - Day 2.

This module contains exercises to practice working with Python decorators,
including @property, @staticmethod, @classmethod, and custom decorators.

Your tasks:
1. Complete the BankAccount class with @property
2. Implement the Date class with @classmethod factory methods
3. Create a custom @validate_types decorator

Run the tests with: pytest tests/test_decorators.py
"""

import functools
import time
from datetime import datetime
from typing import Any, Callable, Type, Union


# Exercise 1: BankAccount with @property
class BankAccount:
    """
    Bank account with balance management.

    :param initial_balance: Starting balance.
    :type initial_balance: float
    :ivar _balance: Private balance attribute.
    :vartype _balance: float
    """

    def __init__(self, initial_balance: float):
        # Validamos que el balance inicial no sea negativo
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        """
        Get current balance (read-only property).

        :return: The current balance.
        :rtype: float
        """
        return self._balance

    def deposit(self, amount: float) -> None:
        """
        Deposit money into account.

        :param amount: Amount to deposit.
        :type amount: float
        :raises ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from account.

        :param amount: Amount to withdraw.
        :type amount: float
        :raises ValueError: If amount is not positive or sufficient funds.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

# Exercise 2: Date class with @classmethod
class Date:
    """
    Date representation with factory methods.

    :param day: Day of month.
    :type day: int
    :param month: Month number (1-12).
    :type month: int
    :param year: Year.
    :type year: int
    """

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string: str) -> "Date":
        """
        Create Date instance from string in DD-MM-YYYY format.

        :param date_string: Date string in "DD-MM-YYYY" format.
        :type date_string: str
        :return: A new Date instance.
        :rtype: Date
        """
        # Parseamos el string "DD-MM-YYYY"
        # map(int, ...) convierte cada trozo en un entero
        day, month, year = map(int, date_string.split('-'))
        
        # Usamos cls(...) en lugar de Date(...) para que funcione 
        # incluso si alguien hereda de esta clase.
        return cls(day, month, year)

    @classmethod
    def today(cls) -> "Date":
        """
        Create Date instance with today's date.

        :return: A new Date instance representing today.
        :rtype: Date
        """
        # Usamos la librería datetime que importamos arriba
        now = datetime.now()
        return cls(now.day, now.month, now.year)

    def display(self) -> str:
        """
        Display date in readable format.

        :return: Date formatted as "DD de [Month] de YYYY".
        :rtype: str
        """
        month_names = {
            1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
            5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
            9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
        }
        # Obtenemos el nombre del mes (o "desconocido" si no es 1-12)
        month_name = month_names.get(self.month, "desconocido")
        return f"{self.day} de {month_name} de {self.year}"


# Exercise 3: Custom decorator with type validation
def validate_types(func: Callable) -> Callable:
    """
    Validate function arguments match their type hints.

    :param func: Function to decorate.
    :type func: callable
    :return: Wrapped function with type validation.
    :rtype: callable
    :raises TypeError: When argument types don't match hints.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Obtenemos las anotaciones (type hints) de la función
        annotations = func.__annotations__
        
        # 2. Obtenemos los nombres de los argumentos
        # co_varnames nos da todos los nombres locales, cogemos solo los argumentos
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        
        # 3. Mapeamos los argumentos posicionales (*args) a sus nombres
        args_dict = dict(zip(arg_names, args))
        
        # 4. Fusionamos con los argumentos nombrados (**kwargs)
        args_dict.update(kwargs)
        
        # 5. Validamos cada argumento
        for name, value in args_dict.items():
            # Solo validamos si el argumento tiene type hint definido
            if name in annotations:
                expected_type = annotations[name]
                
                # Ignoramos la anotación de retorno ('return') si está presente
                if name == 'return':
                    continue
                
                # Verificamos el tipo
                # Nota: Esto funciona bien con tipos nativos (int, str). 
                # Para tipos complejos como List[int] se requeriría lógica extra.
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Argument '{name}' expected {expected_type.__name__}, "
                        f"but got {type(value).__name__}"
                    )
                    
        return func(*args, **kwargs)

    return wrapper


# Bonus Exercise: Create a timing decorator
def timing_decorator(func: Callable) -> Callable:
    """
    Measure and print function execution time.

    :param func: The function to measure.
    :return: The wrapped function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Inicio del cronómetro
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            end_time = time.perf_counter()  # Fin del cronómetro
            execution_time = end_time - start_time
            print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute")
            
    return wrapper


# Bonus Exercise: Create a retry decorator with parameters
def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
    """
    Retry a function on failure.

    Executes the decorated function and, if it raises an exception,
    retries it up to 'max_attempts' times, waiting 'delay' seconds
    between attempts.

    :param max_attempts: Maximum number of execution attempts (default: 3).
    :type max_attempts: int
    :param delay: Seconds to wait between retries (default: 1.0).
    :type delay: float
    :return: The wrapped function with retry logic.
    :rtype: Callable
    """
    # NIVEL 1: La "Fábrica" de decoradores (recibe los argumentos)
    def decorator(func: Callable) -> Callable:
        
        # NIVEL 2: El Decorador real (recibe la función)
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            
            # NIVEL 3: El Wrapper (la lógica de ejecución)
            last_exception = None
            
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    # Si aún nos quedan intentos, esperamos
                    if attempt < max_attempts:
                        print(f"Attempt {attempt}/{max_attempts} failed. Retrying in {delay}s...")
                        time.sleep(delay)
            
            # Si salimos del bucle, es que fallaron todos los intentos
            print(f"Function failed after {max_attempts} attempts.")
            raise last_exception
            
        return wrapper
    return decorator
