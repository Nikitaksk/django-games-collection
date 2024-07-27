from django.db import models
from django.contrib.auth.models import User


class unfinished_tictactoe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.CharField(max_length=9, default=' ' * 9)
    current_turn = models.CharField(max_length=1, default='X')
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Game {self.id}: {self.board}"


class tictactoe_archive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # start_time = models.DateTimeField(auto_now_add=True)
    # end_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"finished tictactoe: {self.user}"
