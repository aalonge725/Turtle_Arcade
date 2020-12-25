"""Implementation of Tic-tac-toe using Python's turtle library.""" # TODO: update docstrings

import turtle
from typing import List, Tuple, Optional
from random import choice

Point = Tuple[float, float]

WIDTH = 600
HEIGHT = 600
WINS: List[List[int]] = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
R1: range = range(-300, -104)
R2: range = range(-95, 96)
R3: range = range(105, 301)


class Section:

    def __init__(self, xs: range, ys: range, draw_start_x: float):
        self.xs = xs
        self.ys = ys
        self.draw_start_pos: Point = (draw_start_x, ys[0] + 25)
        self.val: str = ""


class TicTacToe:
    """Informal abstract class for PvP and PvC classes."""

    def __init__(self):
        self.grid: List[Section] = [
            Section(R1, R3, -200),
            Section(R2, R3, 0),
            Section(R3, R3, 200),
            Section(R1, R2, -200),
            Section(R2, R2, 0),
            Section(R3, R2, 200),
            Section(R1, R1, -200),
            Section(R2, R1, 0),
            Section(R3, R1, 200)
        ]
        self.p1: List[int] = []
        self.p2: List[int] = []
        self.winner: str = ""
        self.x = turtle.Turtle()
        self.o = turtle.Turtle()
        self.board_setup()
    
    def board_setup(self) -> None:
        turtle.speed(10)
        self.x.ht()
        self.o.ht()
        turtle.pu()
        turtle.width(10)
        turtle.goto(-WIDTH/6, HEIGHT/2)
        turtle.pd()
        turtle.goto(-WIDTH/6, -HEIGHT/2)
        turtle.pu()
        turtle.goto(WIDTH/6, HEIGHT/2)
        turtle.pd()
        turtle.goto(WIDTH/6, -HEIGHT/2)
        turtle.pu()
        turtle.goto(-WIDTH/2, HEIGHT/6)
        turtle.pd()
        turtle.goto(WIDTH/2, HEIGHT/6)
        turtle.pu()
        turtle.goto(-WIDTH/2, -HEIGHT/6)
        turtle.pd()
        turtle.goto(WIDTH/2, -HEIGHT/6)
        turtle.pu()
        turtle.speed(0)

    def get_sec_ind(self, x: float, y: float) -> Optional[int]:
        row: int = -1
        col: int = -1
        if x >= -300 and x <= 300 and y >= -300 and y <= 300:
            if y in R3:
                row = 0
            elif y in R2:
                row = 1
            elif y in R1:
                row = 2
            if x in R1:
                col = 0
            elif x in R2:
                col = 1
            elif x in R3:
                col = 2
            if row == -1 or col == -1:
                return None
            return row * 3 + col
        return None

    def draw_X(self, p: Point) -> None:
        x_len: float = (2 * (140 ** 2)) ** .5
        p = (p[0] - 70, p[1] + 140)
        self.x.pu()
        self.x.goto(p)
        self.x.color("red")
        self.x.width(10)
        self.x.speed(0)
        self.x.pd()
        self.x.setheading(315)
        self.x.forward(x_len)
        self.x.pu()
        self.x.setheading(90)
        self.x.forward(140)
        self.x.setheading(225)
        self.x.pd()
        self.x.forward(x_len)
        self.x.pu()

    def draw_O(self, p: Point) -> None:
        self.o.pu()
        self.o.goto(p)
        self.o.color("blue")
        self.o.width(10)
        self.o.speed(0)
        self.o.pd()
        self.o.circle(70)
        self.o.pu()

    def won(self, player: List[int], wins: List[List[int]]) -> bool:
        for i in wins:
            if sub(i, player):
                return True
        return False

    def check_wins(self):
        if self.won(self.p1, WINS):
            self.winner = "Player 1 wins"
        elif self.won(self.p2, WINS):
            self.winner = "Player 2 wins"
        elif len([i for i in self.grid if i.val == ""]) == 0:
            self.winner = "Draw"
        if self.winner != "":
            print("Board:", [i.val for i in self.grid], "\nPlayer 1 Choices:", self.p1, "\nPlayer 2 Choices:", self.p2)
            self.end_game()

    def end_game(self):
        response = turtle.textinput("Game Over!", f"{self.winner}!\n"
        "Enter 1 to play against a friend\n"
        "Enter 2 to play against the computer on easy mode\n"
        "Enter 3 to play against the computer on hard mode\n"
        "Press Enter or click Cancel to quit")
        turtle.clear()
        self.x.clear()
        self.o.clear()
        if response == "1":
            PvP()
        elif response == "2":
            PvC("easy")
        elif response == "3":
            PvC("hard")
        else:
            turtle.Screen().bye()

    def click(self):
        pass


class PvC(TicTacToe):

    def __init__(self, mode: str):
        print("new PvC")
        self.available: List[int] = [i for i in range(0, 9)]
        super().__init__()
        self.mode = mode
        turtle.onscreenclick(self.click)

    def click(self, x: float, y: float) -> None:
        user_ind = super().get_sec_ind(x, y)
        if user_ind is None:
            return
        user_sec: Section = self.grid[user_ind]
        if user_sec.val == "":
            self.p1.append(user_ind)
            user_sec.val = "X"
            super().draw_X(user_sec.draw_start_pos)
            super().check_wins()
        if self.winner != "":
            return
        elif self.mode == "easy":
            self.easy_mode()
        else:
            self.hard_mode()

    def easy_mode(self) -> None:
        comp_ind: int = choice([i for i in range(len(self.grid)) if self.grid[i].val == ""])
        comp_sec: Section = self.grid[comp_ind]
        self.p2.append(comp_ind)
        comp_sec.val = "O"
        super().draw_O(comp_sec.draw_start_pos)
        super().check_wins()


class PvP(TicTacToe):

    def __init__(self):
        self.turn: str = "X"
        super().__init__()
        turtle.onscreenclick(self.click)

    def click(self, x: float, y: float) -> None:
        sec_ind = super().get_sec_ind(x, y)
        if sec_ind is None:
            return
        sec: Section = self.grid[sec_ind]
        if sec.val == "":
            if self.turn == "X":
                self.p1.append(sec_ind)
                sec.val = self.turn
                super().draw_X(sec.draw_start_pos)
                self.turn = "O"
            elif self.turn == "O":
                self.p2.append(sec_ind)
                sec.val = self.turn
                super().draw_O(sec.draw_start_pos)
                self.turn = "X"
            super().check_wins()


def main() -> None:
    turtle.screensize(WIDTH, HEIGHT)
    turtle.speed(10)
    turtle.ht()
    user_input = turtle.textinput("Welcome to Tic Tac Toe!", "Enter 1 to play against a friend\n"
    "Enter 2 to play against the computer on easy mode\n"
    "Enter 3 to play against the computer on hard mode\n"
    "Enter anything else or click Cancel to quit")
    if user_input == "1":
        PvP()
    elif user_input == "2":
        PvC("easy")
    elif user_input == "3":
        PvC("hard")
    else:
        turtle.Screen().bye()

    turtle.done()


def sub(a: List[int], b: List[int]) -> bool:
    for i in a:
        if i not in b:
            return False
    return True


if __name__ == "__main__":
    main()