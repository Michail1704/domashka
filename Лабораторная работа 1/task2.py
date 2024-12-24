# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
size_of_symbol = 4
size_of_book = pages * lines * symbols * size_of_symbol

size_in_Mb = 1.44
size_in_b = size_in_Mb * 1024 * 1024

books = size_in_b // size_of_book # Выводит 3.0
result = round(books) # Выводит 3
print("Количество книг, помещающихся на дискету:", result)
