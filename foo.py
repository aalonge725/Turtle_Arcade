import turtle
from turtle import Screen

WIDTH = 600
HEIGHT = 600

class Foo:
    win: str = "Foo"

    def __init__(self):
        turtle.speed(0)
        turtle.circle(100)
        self.next()

    def next(self):
        a = turtle.numinput("Foo", f"{self.win} won! Enter 1 to play against someone else, 2 to play against the computer, or anything else to quit.", minval=1, maxval=2)
        if a == 1:
            turtle.clear()
            turtle.reset()
            Foo()
        else:
            Screen().bye()

def main() -> None:

    # turtle.circle(100, steps=5)

    # t.write(turtle.textinput("FooFoo", "LOL"), True)

    turtle.screensize(WIDTH, HEIGHT)

    turtle.listen()
    turtle.onscreenclick(coor)
    
    turtle.done()


def coor(x: float, y: float) -> None:
    if y > 200:
        turtle.clear()
        turtle.reset()
    else:
        turtle.goto(x, y)


# def click(x, y):
#     turtle.onscreenclick(click)
#     turtle.goto(x, y)
#     turtle.onscreenclick(None)

def f(x, y):
    print(x, y)
    turtle.goto(x, y)


if __name__ == "__main__":
    main()