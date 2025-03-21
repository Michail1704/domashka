import doctest

class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.
        Примеры:
        >>> b = Book("Test Book", "Test Author")
        >>> str(b)
        'Книга Test Book. Автор Test Author'
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        """
        Возвращает валидное строковое представление экземпляра книги.
        Примеры:
        >>> b = Book("Test Book", "Test Author")
        >>> repr(b)
        "Book(name='Test Book', author='Test Author')"
        """
        return f"{self.__class__.__name__}(name={repr(self.name)}, author={repr(self.author)})"


class PaperBook(Book):
    """ Класс бумажной книги, наследуется от Book. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """
        Устанавливает количество страниц в бумажной книге.
        Проверка на допустимые значения.
        :param value: Количество страниц в книге
        :raise ValueError: Если количество страниц меньше или равно 0
        Примеры:
        >>> p = PaperBook("Test Paper Book", "Test Author", 200)
        >>> p.pages
        200
        >>> p.pages = -50
        Traceback (most recent call last):
        ...
        ValueError: Количество страниц должно быть положительным числом
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление бумажной книги.
        Примеры:
        >>> p = PaperBook("Test Paper Book", "Test Author", 200)
        >>> str(p)
        'Книга Test Paper Book. Автор Test Author, Страниц: 200'
        """
        return f"Книга {self.name}. Автор {self.author}, Страниц: {self.pages}"

    def __repr__(self) -> str:
        """
        Возвращает валидную строку для инициализации такого же экземпляра PaperBook.
        Примеры:
        >>> p = PaperBook("Test Paper Book", "Test Author", 200)
        >>> repr(p)
        "PaperBook(name='Test Paper Book', author='Test Author', pages=200)"
        """
        return f"PaperBook(name={repr(self.name)}, author={repr(self.author)}, pages={self.pages})"


class AudioBook(Book):
    """ Класс аудиокниги, наследуется от Book. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """
        Устанавливает продолжительность аудиокниги.
        Проверка на допустимые значения.
        :param value: Продолжительность аудиокниги в часах
        :raise ValueError: Если продолжительность меньше или равна 0
        Примеры:
        >>> a = AudioBook("Test Audio Book", "Test Author", 5.5)
        >>> a.duration
        5.5
        >>> a.duration = -1
        Traceback (most recent call last):
        ...
        ValueError: Продолжительность аудиокниги должна быть положительным числом
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом")
        self._duration = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление аудиокниги.
        Примеры:
        >>> a = AudioBook("Test Audio Book", "Test Author", 5.5)
        >>> str(a)
        'Книга Test Audio Book. Автор Test Author, Продолжительность: 5.5 часов'
        """
        return f"Книга {self.name}. Автор {self.author}, Продолжительность: {self.duration} часов"

    def __repr__(self) -> str:
        """
        Возвращает валидную строку для инициализации такого же экземпляра AudioBook.
        Примеры:
        >>> a = AudioBook("Test Audio Book", "Test Author", 5.5)
        >>> repr(a)
        "AudioBook(name='Test Audio Book', author='Test Author', duration=5.5)"
        """
        return f"AudioBook(name={repr(self.name)}, author={repr(self.author)}, duration={self.duration})"


if __name__ == "__main__":
    doctest.testmod()