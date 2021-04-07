import pyperclip
from flask import Blueprint, render_template, request, url_for, redirect
from portfolio_site.pass_gen.password_generator import Password
from portfolio_site.pass_gen.forms import PassGenForm

pass_gen = Blueprint("pass_gen", __name__)


@pass_gen.route("/password_generator", methods=["GET", "POST"])
def password_generator():
    form = PassGenForm()
    password = Password()

    if form.validate_on_submit():
        password = Password(lowercase=form.lowercase.data, uppercase=form.uppercase.data, nums=form.nums.data,
                            syms=form.syms.data, min_nums=form.min_nums.data, min_syms=form.min_syms.data,
                            pass_len=form.pass_len.data)
        password.generate()
        form.display.data = password
        return render_template("password_generator.html", title="Password Generator", form=form, password=password)

    form.lowercase.data = password.lowercase
    form.uppercase.data = password.uppercase
    form.nums.data = password.nums
    form.syms.data = password.syms
    form.min_nums.data = password.min_nums
    form.min_syms.data = password.min_syms
    form.pass_len.data = password.pass_len

    return render_template("password_generator.html", title="Password Generator", form=form, password="")
