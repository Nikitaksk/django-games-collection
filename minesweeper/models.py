from django.contrib.auth.models import User
from django.db import models



class minesweeper_active(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()
    mines = models.IntegerField()
    started_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    amount_of_moves = models.IntegerField(default=0)

    def __str__(self):
        return f' [{self.id}]Width: {self.width}, Height: {self.height}, Mines: {self.mines}, User: {self.started_by_user}'

class minesweeper_cells(models.Model):
    game_id = models.ForeignKey(minesweeper_active, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    adjacent_mines = models.IntegerField(default=0)
    is_mine = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    is_revealed = models.BooleanField(default=False)

    def __str__(self):
        return f' Cell[{self.id}]  X: {self.x}, Y: {self.y}'