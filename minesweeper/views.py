import random

from django.shortcuts import render, redirect

from .models import minesweeper_active, minesweeper_cells


def create_game(request):
    if request.method == 'POST':
        height = int(request.POST['height'])
        width = int(request.POST['width'])
        difficulty = int(request.POST['difficulty'])
        amount_of_mines = (height * width * difficulty) // 100
        game = minesweeper_active.objects.create(height=height, width=width, mines=amount_of_mines,
                                                 started_by_user=request.user)
        game.save()
        cells = []
        for x in range(game.width):
            for y in range(game.height):
                cells.append(minesweeper_cells.objects.create(game_id=game, x=x, y=y))

        mines = random.sample(cells, amount_of_mines)
        # print(f'{amount_of_mines} mines created')
        print(mines)
        for mine in mines:
            mine.is_mine = True
            mine.save()

        for cell in cells:
            cell.adjacent_mines = count_adjacent_mines(cell)
            cell.save()
        # print(cells)
        return redirect('index')
    else:
        return render(request, 'minesweeper/game_creation.html')


def count_adjacent_mines(cell):
    game = cell.game_id
    adjacent_cells = minesweeper_cells.objects.filter(
        game_id=game,
        x__range=(cell.x - 1, cell.x + 1),
        y__range=(cell.y - 1, cell.y + 1)
    ).exclude(id=cell.id)

    return adjacent_cells.filter(is_mine=True).count()


def clear(request):
    minesweeper_active.objects.all().delete()
    minesweeper_cells.objects.all().delete()
    print("CLEARED ?")
    return redirect('index')


def index(request):
    try:
        game = minesweeper_active.objects.get(started_by_user=request.user)
        cells = [[]]
        for i in range(game.width):
            for j in range(game.height):
                cells[-1].append(minesweeper_cells.objects.get(game_id=game, x=i, y=j))
            cells.append([])
    except minesweeper_active.DoesNotExist:
        return redirect('create_game')

    if request.method == 'GET':
        return render(request, 'minesweeper/index.html', {'game': game, 'cells': cells})
    else:
        to_toggle = (request.POST['index']).split(',')
        x = int(to_toggle[0])
        y = int(to_toggle[1])

        # cell = minesweeper_cells.objects.get(game_id=game, x=x, y=y)
        reveal(game, cells, x, y)
        game.amount_of_moves += 1
        print(game.amount_of_moves)
        game.save()
        return render(request, 'minesweeper/index.html', {'game': game, 'cells': cells})


def reveal(game, cells, x, y):
    if x >= 0 and x < game.width and y >= 0 and y < game.height:
        cell = cells[x][y]
        if cell.is_mine == False and cell.is_revealed == False:
            cell.is_revealed = True
            if cell.adjacent_mines == 0 :
                reveal(game, cells, x, y - 1)
                reveal(game, cells, x, y + 1)
                reveal(game, cells, x + 1, y)
                reveal(game, cells, x - 1, y)

                reveal(game, cells, x - 1, y - 1)
                reveal(game, cells, x - 1, y + 1)
                reveal(game, cells, x + 1, y - 1)
                reveal(game, cells, x + 1, y + 1)
            cell.save()
