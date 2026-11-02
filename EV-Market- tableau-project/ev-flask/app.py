from flask import Flask, render_template

app = Flask(__name__)

# Tableau Public workbook: EV_Market_17936062524990, sheet: Dashboard1
# Profile: narendra.nagda
DASHBOARD_URL = (
    "https://public.tableau.com/views/EV_Market_17936062524990/Dashboard1"
)


@app.route("/")
def home():
    return render_template("index.html", dashboard_url=DASHBOARD_URL)


if __name__ == "__main__":
    app.run(debug=True)
