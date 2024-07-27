import random

from django.shortcuts import render, redirect, get_object_or_404
from .models import unfinished_tictactoe, tictactoe_archive


def index(request):
    game = unfinished_tictactoe.objects.get_or_create(user=request.user)[0]
    if request.method == "POST":
        if check_winner(game.board):
            return redirect('clear')
        index_to_place = int(request.POST["index"])
        if game.board[index_to_place] == " ":
            game.board = update_board(game.board, index_to_place, 'X')
            game.save()

            ai_move = get_best_move(game.board)
            if ai_move is not None:
                print(f'{ai_move =}')
                game.board = update_board(game.board, ai_move, 'O')
                game.current_turn = 'X'
                game.save()
        return redirect("index")

    context = {
        'board': game.board,
        'winner': check_winner(game.board),
        'current_turn': game.current_turn,
    }
    return render(request, 'tictactoe/index.html', context)


def update_board(board, to_place, player):
    return board[:to_place] + player + board[to_place + 1:]


def clear(request):
    unfinished_tictactoe.objects.get_or_create(user=request.user)[0].delete()
    return redirect("index")


def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        empty_spots = [i for i, spot in enumerate(board) if spot == ' ']
        for spot in empty_spots:
            board = update_board(board, spot, 'O')
            score = minimax(board, False)
            board = update_board(board, spot, ' ')
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        empty_spots = [i for i, spot in enumerate(board) if spot == ' ']
        for spot in empty_spots:
            board = update_board(board, spot, 'X')
            score = minimax(board, True)
            board = update_board(board, spot, ' ')
            best_score = min(score, best_score)
        return best_score


def get_best_move(board):
    empty_spots = [i for i, spot in enumerate(board) if spot == ' ']
    if not empty_spots:
        return None
    best_score = -float('inf')
    best_move = None
    for spot in empty_spots:
        board = update_board(board, spot, 'O')
        score = minimax(board, False)
        board = update_board(board, spot, ' ')
        if score > best_score:
            best_score = score
            best_move = spot

    if best_move is None:
        print('RNDM')
        return random.choice(empty_spots)
    return best_move


def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    if " " not in board:
        return "Draw"
    return None
