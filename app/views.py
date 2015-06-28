from flask import render_template
from app import app

@app.route('/login.html')
def login():
    return render_template('pages/login.html', title="Login")

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('pages/index.html', title="Home", header="Home")

@app.route('/blank.html')
def blank():
    return render_template('pages/blank.html', title="Blank", header="Blank", nav="Blank Page")

@app.route('/flot.html')
def flot():
    return render_template('pages/flot.html', title="Flot", header="Flot Charts", nav="Flot Page")

@app.route('/morris.html')
def morris():
    return render_template('pages/morris.html', title="Morris", header="Morris.js Charts", nav="Morris Page")

@app.route('/tables.html')
def tables():
    return render_template('pages/tables.html', title="Tables", header="Tables", nav="Tables Page")

@app.route('/forms.html')
def forms():
    return render_template('pages/forms.html', title="Forms", header="Forms", nav="Forms Page")

@app.route('/panels-wells.html')
def panels_wells():
    return render_template('pages/panels-wells.html', title="Panels and Wells", header="Panels and Wells", nav="Panels and Wells Page")

@app.route('/buttons.html')
def buttons():
    return render_template('pages/buttons.html', title="Buttons", header="Buttons", nav="Buttons Page")

@app.route('/notifications.html')
def notifications():
    return render_template('pages/notifications.html', title="Notifications", header="Notifications", nav="Notifications Page")

@app.route('/typography.html')
def typography():
    return render_template('pages/typography.html', title="Typography", header="Typography", nav="Typography Page")

@app.route('/icons.html')
def icons():
    return render_template('pages/icons.html', title="Icons", header="Icons", nav="Icons Page")

@app.route('/grid.html')
def grid():
    return render_template('pages/grid.html', title="Grid", header="Grid", nav="Grid Page")