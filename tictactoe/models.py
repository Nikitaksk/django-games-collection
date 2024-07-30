
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class unfinished_tictactoe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.CharField(max_length=9, default=' ' * 9)
    difficulty = models.CharField(max_length=10, default='easy')
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tic tac toe {self.id =}: {self.board =}, {self.difficulty =}"


class tictactoe_archive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"Finished tic tac toe game: by {self.user = }, {self.start_time = }, {self.end_time = }"
