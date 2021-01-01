"""Implementation of Tic Tac Toe using Python's turtle library."""

import turtle
from typing import List, Tuple, Optional
from random import choice

Point = Tuple[float, float]
Potental_Win = Tuple[Tuple[int, int], int]

WIDTH = 600
HEIGHT = 600
X: str = "X"
O: str = "O"
EMPTY: str = ""
EASY: str = "easy"
MED: str = "medium"
HARD: str = "hard"
ONE: str = "1"
TWO: str = "2"
THREE: str = "3"
FOUR: str = "4"
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
POTENTIAL_WINS: List[Potental_Win] = [
    ((0, 1), 2),
    ((0, 2), 1),
    ((1, 2), 0),
    ((3, 4), 5),
    ((3, 5), 4),
    ((4, 5), 3),
    ((6, 7), 8),
    ((6, 8), 7),
    ((7, 8), 6),
    ((0, 3), 6),
    ((0, 6), 3),
    ((3, 6), 0),
    ((1, 4), 7),
    ((1, 7), 4),
    ((4, 7), 1),
    ((2, 5), 8),
    ((2, 8), 5),
    ((5, 8), 2),
    ((0, 4), 8),
    ((0, 8), 4),
    ((4, 8), 0),
    ((2, 4), 6),
    ((2, 6), 4),
    ((4, 6), 2)
]
R1: range = range(-300, -104)
R2: range = range(-95, 96)
R3: range = range(105, 301)


class Section:

    def __init__(self, xs: range, ys: range, draw_start_x: float):
        self.xs = xs
        self.ys = ys
        self.draw_start_pos: Point = (draw_start_x, ys[0] + 25)
        self.val: str = EMPTY


class TicTacToe:
    """Informal "abstract" class for the PvP and PvC classes. Sets up most of the attributes and methods of a Tic Tac Toe game"""
    x = turtle.Turtle()
    o = turtle.Turtle()
    x.ht()
    o.ht()

    def __init__(self):
        """General consturctor for a game of Tic Tac Toe."""
        self.board: List[Section] = [
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
        self.winner: str = EMPTY

    def get_sec_ind(self, x: float, y: float) -> Optional[int]:
        """Returns the index of a section on the board depending on the coordinates of a click."""
        row: int = -1
        col: int = -1
        if x >= -WIDTH / 2 and x <= WIDTH / 2 and y >= -HEIGHT / 2 and y <= HEIGHT / 2:
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
        """Draws an "X" on the board."""
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
        """Draws an "O" on the board."""
        self.o.pu()
        self.o.goto(p)
        self.o.color("blue")
        self.o.width(10)
        self.o.speed(0)
        self.o.pd()
        self.o.circle(70)
        self.o.pu()

    def draw(self, player: List[int], index: int, mark: str) -> None:
        """Draws an "X" or "O" on the board at a given index for a given player."""
        if not (mark == X or mark == O):
            raise ValueError("Mark must be an \"X\" or an \"O\"")
        section: Section = self.board[index]
        player.append(index)
        section.val = mark
        if mark == X:
            self.draw_X(section.draw_start_pos)
        else:
            self.draw_O(section.draw_start_pos)

    def won(self, player: List[int], wins: List[List[int]]) -> bool:
        """Checks if a player has a win."""
        for i in wins:
            if sub(i, player):
                return True
        return False

    def check_wins(self) -> None:
        """Checks if either player in a game has won."""
        if self.won(self.p1, WINS):
            self.winner = "Player 1 wins"
        elif self.won(self.p2, WINS):
            self.winner = "Player 2 wins"
        elif len([i for i in self.board if i.val == EMPTY]) == 0:
            self.winner = "Draw"
        if self.winner != EMPTY:
            print("Board:", [i.val for i in self.board], "\nPlayer 1 Choices:", self.p1, "\nPlayer 2 Choices:", self.p2)
            self.end_game()

    def end_game(self) -> None:
        """Ends the game and allows the user to create a new game of any game mode."""
        turtle.Screen().title("Game Over!")
        response = turtle.textinput("Game Over!", f"{self.winner}!\n"
        "Enter 1 to play against a friend\n"
        "Enter 2 to play against the computer on easy mode\n"
        "Enter 3 to play against the computer on medium mode\n"
        "Enter 4 to play against the computer on hard mode\n"
        "Press Enter or click Cancel to quit")
        self.x.clear()
        self.o.clear()
        if response == ONE:
            PvP()
        elif response == TWO:
            PvC(EASY)
        elif response == THREE:
            PvC(MED)
        elif response == FOUR:
            PvC(HARD)
        else:
            turtle.Screen().bye()

    def click(self) -> None:
        """"An "abstract" method for processing clicks on the screen (intended to be implemented in the PvC and PvP classes)."""
        pass


class PvC(TicTacToe):
    """Player vs. Computer Tic Tic Toe game: a player plays against the computer until someone wins or there is a draw (includes an easy, medium, and hard mode)."""

    def __init__(self, mode: str):
        """Constructor for a player vs. computer Tic Tac Toe game."""
        self.mode = mode
        turtle.Screen().title(f"Player vs. Computer ({self.mode} mode)")
        super().__init__()
        turtle.onscreenclick(self.click)

    def click(self, x: float, y: float) -> None:
        """Processes a click on the screen."""
        user_ind = super().get_sec_ind(x, y)
        if user_ind is None:
            return
        user_sec: Section = self.board[user_ind]
        if user_sec.val == EMPTY:
            self.draw(self.p1, user_ind, X)
            super().check_wins()
        else:
            return
        if self.winner != EMPTY:
            return
        elif self.mode == "easy":
            self.easy_mode()
        elif self.mode == "medium":
            self.med_mode()
        else:
            self.hard_mode()
        super().check_wins()

    def easy_mode(self) -> None:
        """Computer selects an available section at random."""
        comp_ind: int = choice([i for i in range(len(self.board)) if self.board[i].val == EMPTY])
        self.draw(self.p2, comp_ind, O)

    def med_mode(self) -> None:
        """Computer tries to win if it has 2/3 sections in a row or blocks the user from winning and chooses a random section otherwise."""
        comp_ind: int
        if len(self.potential_wins(self.p2)) >= 1:
            comp_ind = choice(self.potential_wins(self.p2))[1]
        elif len(self.potential_wins(self.p1)) >= 1:
            comp_ind = choice(self.potential_wins(self.p1))[1]
        else:
            comp_ind = choice([i for i in range(len(self.board)) if self.board[i].val == EMPTY])
        self.draw(self.p2, comp_ind, O)

    def hard_mode(self) -> None:
        """Computer always forces a draw or tries to win if possible."""
        comp_ind: int
        if len(self.p1) == 1:
            if self.p1[0] != 4:
                comp_ind = 4
            else:
                comp_ind = choice([i for i in range(len(self.board)) if i % 2 == 0 and i != 4])
        elif len(self.potential_wins(self.p2)) >= 1:
            comp_ind = choice(self.potential_wins(self.p2))[1]
        elif len(self.potential_wins(self.p1)) >= 1:
            comp_ind = choice(self.potential_wins(self.p1))[1]
        else:
            good_moves: List[int] = self.good_moves()
            chances_to_win: List[int] = []
            for i in good_moves:
                self.p2.append(i)
                self.board[i].val = O
                if len(self.potential_wins(self.p2)) >= 1:
                    chances_to_win.append(i)
                self.p2.pop()
                self.board[i].val = EMPTY
            if len(chances_to_win) > 0:
                comp_ind = choice(chances_to_win)
            else:
                comp_ind = choice(good_moves)
        self.draw(self.p2, comp_ind, O)

    def potential_wins(self, player: List[int]) -> List[Potental_Win]:
        """Returns a list of all instances where a player has a potential win (owns 2/3 sections in a row and the third section isn't taken."""
        wins: List[Potental_Win] = []
        nearly_won: List[Tuple[int, int]] = [i[0] for i in POTENTIAL_WINS]
        missing: List[int] = [i[1] for i in POTENTIAL_WINS]
        for i in sublists(player):
            if i in nearly_won and self.board[missing[nearly_won.index(i)]].val == EMPTY:
                wins.append(POTENTIAL_WINS[nearly_won.index(i)])
        return wins

    def good_moves(self) -> List[int]:
        """Returns a list of the sections the computer can pick that will prevent the user from having a guaranteed win."""
        available = [i for i in range(len(self.board)) if self.board[i].val == EMPTY]
        indicies: List[int] = []
        for i in available:
            bad_comp_move: bool = False
            self.p2.append(i)
            self.board[i].val = O
            for j in [k for k in available if k != i]:
                self.p1.append(j)
                self.board[j].val = X
                if len(self.potential_wins(self.p1)) >= 2 and len(self.potential_wins(self.p2)) == 0:
                    bad_comp_move = True
                    self.p1.pop()
                    self.board[j].val = EMPTY
                    break
                else:
                    self.p1.pop()
                    self.board[j].val = EMPTY
            if not bad_comp_move:
                indicies.append(i)
            self.p2.pop()
            self.board[i].val = EMPTY
        return indicies


class PvP(TicTacToe):
    """Player vs. Player Tic Tic Toe game: 2 players take turns selecting sections on the board until either player wins or there is a draw."""

    def __init__(self):
        """Constructor for a player vs. player Tic Tac Toe game."""
        turtle.Screen().title("Player vs. Player mode")
        self.turn: str = X
        super().__init__()
        turtle.onscreenclick(self.click)

    def click(self, x: float, y: float) -> None:
        """Processes a click on the screen."""
        section_ind = super().get_sec_ind(x, y)
        if section_ind is None:
            return
        if self.board[section_ind].val == EMPTY:
            if self.turn == X:
                self.draw(self.p1, section_ind, X)
                self.turn = O
            elif self.turn == O:
                self.draw(self.p2, section_ind, O)
                self.turn = X
            super().check_wins()


def main() -> None:
    turtle.screensize(WIDTH, HEIGHT)
    turtle.Screen().title("Tic Tac Toe")
    turtle.speed(10)
    turtle.ht()
    user_input = turtle.textinput("Welcome to Tic Tac Toe!", "Enter 1 to play against a friend\n"
    "Enter 2 to play against the computer on easy mode\n"
    "Enter 3 to play against the computer on medium mode\n"
    "Enter 4 to play against the computer on hard mode\n"
    "Enter anything else or click Cancel to quit")
    board_setup()
    if user_input == ONE:
        PvP()
    elif user_input == TWO:
        PvC(EASY)
    elif user_input == THREE:
        PvC(MED)
    elif user_input == FOUR:
        PvC(HARD)
    else:
        turtle.Screen().bye()

    turtle.done()


def board_setup() -> None:
    """Sets up Tic Tac Toe board."""
    turtle.speed(10)
    turtle.pu()
    turtle.width(10)
    turtle.goto(-WIDTH / 6, HEIGHT / 2)
    turtle.pd()
    turtle.goto(-WIDTH / 6, -HEIGHT / 2)
    turtle.pu()
    turtle.goto(WIDTH / 6, HEIGHT / 2)
    turtle.pd()
    turtle.goto(WIDTH / 6, -HEIGHT / 2)
    turtle.pu()
    turtle.goto(-WIDTH / 2, HEIGHT / 6)
    turtle.pd()
    turtle.goto(WIDTH / 2, HEIGHT / 6)
    turtle.pu()
    turtle.goto(-WIDTH / 2, -HEIGHT / 6)
    turtle.pd()
    turtle.goto(WIDTH / 2, -HEIGHT / 6)
    turtle.pu()
    turtle.speed(0)


def sub(a: List[int], b: List[int]) -> bool:
    """Determines if every element in one list can be found in another list."""
    for i in a:
        if i not in b:
            return False
    return True


def sublists(input: List[int]) -> List[Tuple[int, int]]:
    """Finds all combinations of length 2 pairs in a list."""
    input_sorted: List[int] = sorted(input)
    result: List[Tuple[int, int]] = []
    for i in range(len(input) - 1):
        for j in range(i + 1, len(input)):
            result.append((input_sorted[i], input_sorted[j]))
    return result


if __name__ == "__main__":
    main()