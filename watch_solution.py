# Run this program to provide a solution to the puzzle, the aim is to solve the puzzle in as few moves as possible.
from tkinter import Frame, Label, CENTER
import constants as c
from puzzle_functions import logic
import solution
import time


class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.matrix_history = list()
        # self.matrix = logic.new_game(c.GRID_LEN)
        self.matrix = solution.start_state
        self.grid()
        self.master.title('Number Slider')
        # self.master.bind("<Key>", self.key_down)

        self.commands = {c.KEY_UP: logic.up, c.KEY_DOWN: logic.down,
                         c.KEY_LEFT: logic.left, c.KEY_RIGHT: logic.right}

        self.grid_cells = []
        self.init_grid()
        self.update_grid_cells()
        self.play_moves(solution.solution_moves)

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR,
                        fg=c.CELL_COLOR)
        self.update_idletasks()
        self.update()

    # def key_down(self, event):
    #     key = repr(event.char)
    #     if key in self.commands:
    #         # record last move
    #         self.commands[key](self.matrix)
    #         self.matrix_history.append(self.matrix)
    #         self.update_grid_cells()
    #         if logic.game_state(self.matrix, c.GRID_LEN) == 'win':
    #             self.grid_cells[-1][-1].configure(
    #                 text="DONE", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    def play_moves(self, moves):
        for move in moves:
            key = repr(move)
            if key in self.commands:
                # record last move
                self.commands[key](self.matrix)
                self.matrix_history.append(self.matrix)
                self.update_grid_cells()
                if logic.game_state(self.matrix, c.GRID_LEN) == 'win':
                    self.grid_cells[-1][-1].configure(
                        text="DONE", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
            time.sleep(0.2)


game_grid = GameGrid()
