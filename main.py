from tkinter import *
from cell import Cell
import settings
import utils


def create_app():
    root = Tk()
    root.configure(background="black")
    root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
    root.title("Minesweeper Game")
    root.resizable(False, False)

    top_frame = Frame(
        root,
        bg="black",
        width=settings.WIDTH,
        height=utils.height_prct(percentage=25),
    )
    top_frame.place(x=0, y=0)

    game_title = Label(
        top_frame,
        bg="black",
        fg='white',
        text='Minesweeper Game',
        font=('', 30)
    )

    game_title.place(
        x=utils.width_prct(25),
        y=0
    )

    left_frame = Frame(
        root,
        bg='black',
        width=utils.width_prct(percentage=25),
        height=utils.height_prct(percentage=75)
    )
    left_frame.place(x=0, y=utils.height_prct(percentage=25))

    center_frame = Frame(
        root,
        bg="black",
        width=utils.width_prct(percentage=75),
        height=utils.height_prct(percentage=75),
    )
    center_frame.place(
        x=utils.width_prct(percentage=25),
        y=utils.height_prct(percentage=25),
    )

    for row in range(settings.GRID_SIZE):
        for column in range(settings.GRID_SIZE):
            c = Cell(
                location=center_frame,
                column=column,
                row=row,
            )

    Cell.randomize_mines()
    Cell.create_cell_count_label(left_frame)
    root.mainloop()


if __name__ == '__main__':
    create_app()
