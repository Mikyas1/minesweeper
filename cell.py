import random
import sys
from tkinter import Button, Label, messagebox

import settings


def NULL_FUNCTION(_):
    pass


class Cell:
    all = []
    cell_count_label_object = None
    cell_count = settings.CELL_COUNT

    def __init__(self,
                 column,
                 row,
                 location,
                 is_mined=False):
        self.is_mined = is_mined
        self.location = location
        self.hidden = True
        self.marked = False
        self.x = column
        self.y = row
        self._cell_btn_object = self.create_btn_object()
        self.grid(column=column, row=row)
        self.orig_color = self._cell_btn_object.cget("background")
        Cell.all.append(self)

    def create_btn_object(self):
        btn = Button(
            self.location,
            width=9,
            height=3,
        )
        btn.bind('<Button-1>', self.left_clicked)
        btn.bind('<Button-3>', self.right_clicked)
        return btn

    def grid(self, column, row):
        self._cell_btn_object.grid(column=column, row=row)

    def place(self, x, y):
        self._cell_btn_object.place(x=x, y=y)

    def left_clicked(self, event=None):
        if not self.hidden:
            return
        if self.is_mined:
            self._cell_btn_object.configure(background="red", text="*")
            self.hidden = False
            messagebox.showerror(title="Game over!!!", message="You clicked on a mine")
            sys.exit()
        else:
            mined_neighbors, neighbors = self.show_mined_neighbors()
            if mined_neighbors == 0:
                for cell in neighbors:
                    cell.show_mined_neighbors()
            if Cell.cell_count == settings.MINES_COUNT:
                messagebox.showinfo(title="You Won!!!", message="Good Job.")
                sys.exit()

    def right_clicked(self, event=None):
        if self.hidden:
            self.marked = not self.marked
            self._cell_btn_object.configure(
                bg='orange' if self.marked else self.orig_color,
            )

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT,
        )
        for picked_cell in picked_cells:
            picked_cell.is_mined = True

    @staticmethod
    def print_cells():
        print("===========")
        print("===========>  All Cells")
        print(f"===========> length is {len(Cell.all)}")
        for cell in Cell.all:
            print(f"===========> {cell}")

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    def show_mined_neighbors(self):
        mined_neighbors = 0
        neighbors = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                cell = Cell.get_cell_by_coordinate(x + self.x, y + self.y)
                if cell is not None and self is not cell:
                    neighbors.append(cell)
                    if cell.is_mined:
                        mined_neighbors += 1
        self._cell_btn_object.configure(
            text=f"{mined_neighbors}",
            bg=self.orig_color,
        )
        self.hidden = False
        Cell.refresh_cell_count_label()
        return mined_neighbors, neighbors

    @staticmethod
    def refresh_cell_count_label():
        if Cell.cell_count_label_object:
            Cell.cell_count -= 1
            Cell.cell_count_label_object.configure(
                text=f"Cells Left: {Cell.cell_count}"
            )

    @staticmethod
    def get_cell_by_coordinate(column, row):
        for cell in Cell.all:
            if cell.x == column and cell.y == row:
                return cell

    @staticmethod
    def create_cell_count_label(location, x=0, y=0):
        lbl = Label(
            location,
            text=f"Cells Left: {Cell.cell_count}",
            bg='black',
            fg='white',
            width=14,
            height=2,
            font=("", 18)
        )
        Cell.cell_count_label_object = lbl
        Cell.cell_count_label_object.place(x=x, y=y)
