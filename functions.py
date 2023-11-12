import random
import sys
import os

def draw_board(board) :
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---+---+---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---+---+---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def get_player_move(board, symbol) :
    try :
        move = int(input(f'Ход игрока {symbol}: '))
        if move > 9 :
            print('Нверное значение, попробуйте снова!')
            return get_player_move(board, symbol)
        if board[move-1] == ' ' :
            board[move-1] = symbol
        else :
            print('Сюда ходить нельзя, попробуйте снова!')
            return get_player_move(board, symbol)
    except ValueError:
        print('Неверное значение!')
        return get_player_move(board, symbol)
    
def get_computer_move(board, symbol) :
    move = random.randint(0, 8)
    if board[move] == ' ' :
        board[move] = symbol
    else : get_computer_move(board, symbol)
    
def choose() :
    symbol_player = input('Выберете, кем играть: игрок Х или игрок О? ').upper()
    if symbol_player == 'X' :
        symbol_computer = 'O'
        return symbol_player, symbol_computer
    elif symbol_player == 'O' :
        symbol_computer = 'X'
        return symbol_player, symbol_computer
    else :
        print('Выбран неверный игрок, повторите попытку снова! ')
        return choose()

def check_win(board, symbol_player, symbol_computer) :
    wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for win in wins :
        if board[win[0]] == board[win[1]] == board[win[2]] != ' ':
            if board[win[0]] == symbol_player :
                print('Вы победили!')
                sys.exit()
            elif board[win[0]] == symbol_computer :
                print('Вы проиграли! ')
                sys.exit()

def Main() :
    os.system('CLS')
    choice = choose()
    symbol_player = choice[0]
    symbol_computer = choice[1]
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    draw_board(board)
    counter = 0
    for i in range(len(board)) :
        if board[i] != 'X' or board[i] != 'O' :
            get_player_move(board, symbol_player)
            draw_board(board)
            check_win(board, symbol_player, symbol_computer)
            counter += 1
            print()
            if counter<9 :
                get_computer_move(board, symbol_computer)
                draw_board(board)
                check_win(board, symbol_player, symbol_computer)
                counter += 1
                print()
            else :
                draw_board(board)
                print('Ничья!')
                sys.exit()  