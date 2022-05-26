"""
    игроки по очереди заполняют массив игрового поля Garr
    выигрывает тот, кто после своего хода заполнил строку, столбец или диагональ
"""


N = 3  # размерность поля, константа, но можно легко допилить ручной ввод

capture = [i for i in range(N)]  # формирует "заголовок" игрового поля (первая строка =  0 1 2 .. N)

Garr = [['-'] * N for i in range(N)]  # GameArray массив игрового поля, в начале игры заполняется '-', 
                                      # по ходу игры заполняется 'O', 'X'


def game_print(arr, cap):
    # выводит на печать текущее игровое поле arr c "заголовком" cap

    def line_print(line, num):
        # вывод на печать строки из элементов одноуровнего списка line == [.., .., ...] с добавлением разделителя ' '
        # добавляет номер строки num
        print(f'{num} {" ".join(map(str, line))}')
        return None

    line_print(cap, ' ')
    for i in range(N): line_print(arr[i], i)
    print()
    return


def step(val, arr):
    # запрашивает две координаты x, y
    # валлидирует введённое значение
    # добавляет их в массив ходов arr и возвращает его
    # val - текущее значение игрока "X" или "O" 

    while True:
        line = input(f'Player {val} step. Input colum and row data -->').split()
        try:
            x, y = int(line[0]), int(line[1])
            if arr[y][x] == '-':
                arr[y][x] = val
                return arr
            else:
                print('Input error. Should select free position')
        except:
            print('Input error. Number in N-range expected')


def is_gameover(val, arr):
    # проверяет выйгрыш, сообщает результат, возращает True если выйгрыш 
    # val - текущее значение игрока "X" или "O" 


    # массив с переставленными строками и столбцами для удобства проверки выйгрыша
    mirror_arr = [['-'] * N for i in range(N)]

    d1, d2 = [], []  # диагонали игровой матрицы для удобства проверки выйгрыша
    wincode = [val] * N  # выйгрышная комбинация

    # заполнение вспомогательных mirror_arr, d1, d2 из текущего игрового массива
    for i in range(N):
        d1.append(arr[i][i])
        d2.append(arr[i][N - i - 1])
        for j in range(N):
            mirror_arr[j][i] = arr[i][j]

    flag = False
    # построковая проверка текущего игрового массива, вспомогательного "зеркального" массива и диагоналей
    # на соответствие выйгрышной комбинации
    for i in range(N):
        if arr[i] == wincode or mirror_arr[i] == wincode or d1 == wincode or d2 == wincode:
            flag = True
            print(f'Game Over! \n {val} win!')
            break

    return flag


# начало игры

game_print(Garr, capture)  # вывод начального пустого поля

while True:
    step('X', Garr)
    game_print(Garr, capture)
    if is_gameover('X', Garr):
        break

    step('O', Garr)
    game_print(Garr, capture)
    if is_gameover('O', Garr):
        break
