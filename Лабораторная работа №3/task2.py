# TODO Напишите функцию find_common_participants

def find_common_participants(a, b, d=","):
    ar_a = a.split(d)
    ar_b = b.split(d)
    c=[]
    for i in ar_a:
        for g in ar_b:
            if i == g and i not in c:
                c.append(i)
    return c

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

array = find_common_participants(participants_first_group, participants_second_group, "|")
array = sorted(array)


# TODO Провеьте работу функции с разделителем отличным от запятой
