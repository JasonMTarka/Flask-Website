from flask import Blueprint, render_template
from portfolio_site.sudoku.Sudoku_Solver.sudoku_solver import Sudoku
from portfolio_site.sudoku.forms import SudokuForm


sudoku = Blueprint("sudoku", __name__)


@sudoku.route("/sudoku_lander", methods=["GET", "POST"])
def sudoku_lander() -> str:
    return render_template("sudoku_lander.html", title="Sudoku Solver")


@sudoku.route("/sudoku_solver/<difficulty>", methods=["GET", "POST"])
def sudoku_solver(difficulty: str) -> str:

    form = SudokuForm()
    sudoku = Sudoku(difficulty=difficulty)

    if form.validate_on_submit():
        sudoku.solve()
        return render_template("sudoku_solver.html", title="Sudoku Solver", form=form, grid=sudoku.grid, sudoku=sudoku)

    else:
        return render_template("sudoku_solver.html", title="Sudoku Solver", form=form, grid=sudoku.grid, sudoku=sudoku)
