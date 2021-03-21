from flask import Blueprint, render_template, redirect
from random import choice
from portfolio_site.sudoku.sudoku_solver import Sudoku
from portfolio_site.sudoku.forms import SudokuForm
#from flask_caching import Cache

sudoku = Blueprint("sudoku", __name__)

@sudoku.route("/sudoku_lander", methods = ["GET", "POST"])
def sudoku_lander(token=None):
	return render_template("sudoku_lander.html", title="Sudoku Solver")

@sudoku.route("/sudoku_solver/<difficulty>", methods = ["GET", "POST"])
def sudoku_solver(difficulty):
	
	form = SudokuForm()
	sudoku = Sudoku(difficulty=difficulty)

	if form.validate_on_submit():
		sudoku.solve()
		return render_template("sudoku_solver.html", title="Sudoku Solver", form=form, grid=sudoku.grid, sudoku=sudoku)

	else:
		return render_template("sudoku_solver.html", title="Sudoku Solver", form=form, grid=sudoku.grid, sudoku=sudoku)
