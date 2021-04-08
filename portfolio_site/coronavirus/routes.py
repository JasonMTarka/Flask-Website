from flask import Blueprint, render_template, url_for
from portfolio_site.coronavirus.Coronavirus_Tracker.coronavirus_scraper import COVID19_Scraper
from portfolio_site.coronavirus.forms import Covid19Form

covid = Blueprint("covid", __name__)


@covid.route("/coronavirus_tracker", methods=["GET", "POST"])
def coronavirus_tracker():

    form = Covid19Form()
    graph_img = url_for("static", filename="graphs/" + "Figure_1.png")

    if form.validate_on_submit():
        scraper = COVID19_Scraper()
        data = scraper.package_data(scraper.get_dayton_stats(), scraper.get_tokyo_stats())
        return render_template("coronavirus_tracker.html", title="Coronavirus Tracker", form=form, data=data, graph_img=graph_img)

    return render_template("coronavirus_tracker.html", title="Coronavirus Tracker", form=form, data={}, graph_img=graph_img)
