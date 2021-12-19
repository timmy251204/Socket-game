def rook(place,prohibit):
    bukvar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    letter = list(place)[0]
    number = list(place)[1]
    for i in range(1,9):
        if i == int(number):
            continue
        else:
            prohibit.append(str(letter) + str(i))
    for i in range(8):
        prohibit.append(bukvar[i] + number)
def letter(letter): # превращение буквы в цмфру
    if letter == 'a':
        return 0
    if letter == 'b':
        return 1
    if letter == 'c':
        return 2
    if letter == 'd':
        return 3
    if letter == 'e':
        return 4
    if letter == 'f':
        return 5
    if letter == 'g':
        return 6
    if letter == 'h':
        return 7
def doska(board):
    s = ''
    for i in range(8):
        for j in range(8):
            s += board[i][j]
        s += '\n'
    return s
def letter_id(a):
    if a == 'a':
        return 1
    elif a == 'b':
        return 1
    elif a == 'c':
        return 1
    elif a == 'd':
        return 1
    elif a == 'e':
        return 1
    elif a == 'f':
        return 1
    elif a == 'g':
        return 1
    elif a == 'h':
        return 1
    else:
        return 0
def number_id(a):
    if a == 1:
        return 1
    elif a == 2:
        return 1
    elif a == 3:
        return 1
    elif a == 4:
        return 1
    elif a == 5:
        return 1
    elif a == 6:
        return 1
    elif a == 7:
        return 1
    elif a == 8:
        return 1
    else:
        return 0
def symbol(a):
    if a == '$':
        return 0
    elif a == '&':
        return 1
    else:
        return 2
def found(board):
    bukvar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    kol=[]
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] == 'L':
                kol.append(bukvar[j] + str(i+1))
    prohibit=[]
    rook(kol[0],prohibit)
    rook(kol[1],prohibit)
    return prohibit
def ladia(board):
    bukvar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    kol = []
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == 'L':
                kol.append(bukvar[i] + str(j + 1))
    return kol
def king_a(board):
    bukvar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    kol = []
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] == 'K':
                kol.append(i)
                kol.append(j)
    number = list(kol)[0]
    letter = list(kol)[1]
    prohibit = []
    print(kol)
    for i in range(0, 8):
        for j in range(0, 8):
            if abs(letter - i) == 0 and abs(number - j) == 0:
                continue
            elif abs(letter - i) <= 1 and abs(number - j) <= 1:
                prohibit.append(bukvar[i] + str(j + 1))
    return prohibit
def same(a,b):
    count = 0
    for i in range(len(a)):
        if b.count(a[i]) > 0:
            count += 1
        else:
            continue
    return len(a) - count
turn_move = 0
unit = 0
#   abcdefgh
# 1 ////////
# 2 ///L////
# 3 ////////
# 4 ////////
# 5 ///////
# 6 /////6//
# 7 ////////
# 8 ////////
# если не кратно 2, то ход короля
# если кратно 2, то ход ладьи
# L - ладья
# / - Пустое место
# K - король

def move(a, board):
    a = list(str(a))
    global turn_move
    start_letter = a[0]
    start_number = int(a[1])
    end_letter = a[3]
    end_number = int(a[4])
    if len(a) != 6:
        return 'Ход надо ввести в правильном формате сначала координата поля, откуда делается ход, потом тире, а потом координта поля, куда делают ход'
    elif a[2] != '-':
        return 'Ход надо ввести в правильном формате сначала координата поля, откуда делается ход, потом тире, а потом координта поля, куда делают ход'
    elif letter_id(start_letter) == 0:
        return 'Такой координаты нет на доске'
    elif number_id(start_number) == 0:
        return 'Такой координаты нет на доске'
    elif letter_id(end_letter) == 0:
        return 'Такой координаты нет на доске'
    elif number_id(end_number) == 0:
        return 'Такой координаты нет на доске'
    else:
        if symbol(a[5]) == 2:
            return 'Специальный символ неправильный'
        elif symbol(a[5]) != turn_move % 2:
            return 'Соперник пытается сделать ход в твое время, думай быстрее'
        elif turn_move % 2 == 0:
            if board[start_number - 1][letter(start_letter)] != 'L':
                return 'Ладьи нет на месте, где вы хотит сделать ход'
            elif start_letter == end_letter and start_number == end_number: # ход в тоже место
                return 'Ход в тоже место где вы стоите делать нельзя'
            elif start_letter == end_letter and board[end_number - 1][letter(end_letter)] == '/': # ход
                board[start_number - 1][letter(start_letter)] = '/'
                board[end_number - 1][letter(end_letter)] = 'L'
                turn_move+=1

                if same(king_a(board), found(board)) == 0:
                    return 'Ахахаххахахахах лаьди выиграли'
                else:
                    return doska(board)
            elif start_number == end_number and board[end_number - 1][letter(end_letter)] == '/': # ход
                board[start_number - 1][letter(start_letter)] = '/'
                board[end_number - 1][letter(end_letter)] = 'L'
                turn_move+=1

                if same(king_a(board), found(board)) == 0:
                    return 'Ахахаххахахахах лаьди выиграли'
                else:
                    return doska(board)
            else:
                return 'Я не знаю, что за ошибка, но ход неправильный' # неизвестно что, но ошибка
        else:
            if same(king_a(board),found(board)) == 0:
                return 'Ахахаххахахахах лаьди выиграли'
            elif ladia(board).count(a[3]+a[4]) > 0:
                return'Ахахаххахахахах лаьди програли'
            elif found(board).count(a[3]+a[4]) > 0:
                return 'Под шах нельзя делать ход'
            elif board[start_number - 1][letter(start_letter)] != 'K':
                return 'Короля нет на месте, где вы хотит сделать ход'
            elif abs(letter(end_letter) - letter(start_letter)) == 1 and abs(start_number - end_number) == 1:
                board[start_number - 1][letter(start_letter)] = '/'
                board[end_number - 1][letter(end_letter)] = 'K'
                turn_move += 1
                return doska(board)
            elif abs(letter(end_letter) - letter(start_letter)) == 1 and abs(start_number - end_number) == 0:
                board[start_number - 1][letter(start_letter)] = '/'
                board[end_number - 1][letter(end_letter)] = 'K'
                turn_move += 1
                return doska(board)
            elif abs(letter(end_letter) - letter(start_letter)) == 0 and abs(start_number - end_number) == 1:
                board[start_number - 1][letter(start_letter)] = '/'
                board[end_number - 1][letter(end_letter)] = 'K'
                turn_move += 1
                return doska(board)
            else:
                return 'Я не знаю, что за ошибка, но ход неправильный'  # неизвестно что, но ошибка













