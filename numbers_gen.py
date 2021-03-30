from string import ascii_lowercase
from random import choice


def vertical_line_right(border_size, table, size):
    for i in range(size):
        for j in range(size):
            if size - border_size <= j:
                table[i][j] = str(choice(ascii_lowercase))
    return table


def half_vertical_up_line_right(border_size, table, size):
    for i in range(size):
        for j in range(size):
            if (i <= size // 2) and (size - border_size <= j):
                table[i][j] = str(choice(ascii_lowercase))
    return table


def half_vertical_bottom_line_right(border_size, table, size):
    for i in range(size):
        for j in range(size):
            if (size // 2 < i) and (size - border_size <= j):
                table[i][j] = str(choice(ascii_lowercase))
    return table


def vertical_line_left(border_size, table, size):
    for i in range(size):
        for j in range(size):
            if j < border_size:
                table[i][j] = str(choice(ascii_lowercase))
    return table


def half_vertical_up_line_left(border_size, table, size):
    for i in range(size):
        for j in range(size):
            if (i <= size // 2) and (j < border_size):
                table[i][j] = str(choice(ascii_lowercase))
    return table


def half_vertical_bottom_line_left(border_size, table, size):
    for i in range(size):
        for j in range(size):
            if (size // 2 < i) and (j < border_size):
                table[i][j] = str(choice(ascii_lowercase))
    return table


def horizontal_up_line(border_size, table, size):
    for i in range(size):
        for j in range(size):
            if i < border_size:
                table[i][j] = str(choice(ascii_lowercase))
    return table


def horizontal_middle_line(border_size, table, size):
    for i in range(size):
        for j in range(size):
            if size // 2 <= i < size // 2 + border_size:
                table[i][j] = str(choice(ascii_lowercase))
    return table


def horizontal_bottom_line(border_size, table, size):
    for i in range(size):
        for j in range(size):
            if size - border_size <= i:
                table[i][j] = str(choice(ascii_lowercase))
    return table


def numb_choice(number, border_size, lines, rows, size):
    tab = [[" "] * size for i in range(size)]
    if number == 0:
        vertical_line_right(border_size, tab, size)
        vertical_line_left(border_size, tab, size)
        horizontal_bottom_line(border_size, tab, size)
        horizontal_up_line(border_size, tab, size)

    elif number == 1:
        vertical_line_right(border_size, tab, size)

    elif number == 2:
        horizontal_up_line(border_size, tab, size)
        half_vertical_up_line_right(border_size, tab, size)
        horizontal_middle_line(border_size, tab, size)
        half_vertical_bottom_line_left(border_size, tab, size)
        horizontal_bottom_line(border_size, tab, size)

    elif number == 3:
        horizontal_up_line(border_size, tab, size)
        horizontal_middle_line(border_size, tab, size)
        vertical_line_right(border_size, tab, size)
        horizontal_bottom_line(border_size, tab, size)

    elif number == 4:
        vertical_line_right(border_size, tab, size)
        horizontal_middle_line(border_size, tab, size)
        half_vertical_up_line_left(border_size, tab, size)

    elif number == 5:
        horizontal_up_line(border_size, tab, size)
        half_vertical_up_line_left(border_size, tab, size)
        horizontal_middle_line(border_size, tab, size)
        horizontal_bottom_line(border_size, tab, size)
        half_vertical_bottom_line_right(border_size, tab, size)

    elif number == 6:
        horizontal_up_line(border_size, tab, size)
        horizontal_middle_line(border_size, tab, size)
        horizontal_bottom_line(border_size, tab, size)
        vertical_line_left(border_size, tab, size)
        half_vertical_bottom_line_right(border_size, tab, size)

    elif number == 7:
        horizontal_up_line(border_size, tab, size)
        vertical_line_right(border_size, tab, size)

    elif number == 8:
        vertical_line_right(border_size, tab, size)
        vertical_line_left(border_size, tab, size)
        horizontal_bottom_line(border_size, tab, size)
        horizontal_up_line(border_size, tab, size)
        horizontal_middle_line(border_size, tab, size)

    elif number == 9:
        vertical_line_right(border_size, tab, size)
        horizontal_middle_line(border_size, tab, size)
        horizontal_bottom_line(border_size, tab, size)
        horizontal_up_line(border_size, tab, size)
        half_vertical_up_line_left(border_size, tab, size)

    return tab[lines][rows]


def main_func(user_choice):
    user_choice = str(user_choice)
    size = 10
    border_size = size // 5
    result_num_list = []
    for i in range(size):
        for m in range(len(user_choice)):
            for j in range(size):
                if m == 0:
                    a = str(numb_choice(int(user_choice[0]), border_size, i, j, size))
                elif m == 1:
                    a = str(numb_choice(int(user_choice[1]), border_size, i, j, size))
                elif m == 2:
                    a = str(numb_choice(int(user_choice[2]), border_size, i, j, size))
                else:
                    a = str(numb_choice(int(user_choice[3]), border_size, i, j, size))
                result_num_list.append(a)
            result_num_list.append("   ")
        result_num_list.append("\n")
    result_str = "".join(result_num_list)
    return result_str


if __name__ == "__main__":  # если функция запускается в корневом файле
    check = main_func(4545)
    print(check)
