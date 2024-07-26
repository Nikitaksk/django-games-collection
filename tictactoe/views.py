from django.shortcuts import render, redirect


def index(request):
    if 'board' not in request.session:
        start_game(request)

    if request.method == "POST":
        if request.session['winner'] != None:
            start_game(request)
            return redirect("index")

        index = int(request.POST["index"])
        board = list(request.session['board'])

        if board[index] == " " and not request.session['winner']:
            board[index] = request.session['current_turn']
            request.session['board'] = ''.join(board)
            request.session['current_turn'] = 'O' if request.session['current_turn'] == 'X' else 'X'
            winner = check_winner(request.session['board'])
            request.session['winner'] = winner
        return redirect("index")

    context = {
        'board': request.session['board'],
        'winner': request.session['winner'],
        'current_turn': request.session['current_turn'],
    }
    return render(request, 'tictactoe/index.html', context)


def start_game(request):
    request.session['board'] = ' ' * 9
    request.session['current_turn'] = 'X'
    request.session['winner'] = None


def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a] + ' wins!'
    if " " not in board:
        return "Draw"
    return None
