import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, is_int

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.jinja_env.filters["usd"] = usd

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///finance.db")

if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_portfolio = db.execute(
        "SELECT id, symbol, name, SUM(shares)  FROM trades WHERE id = ? GROUP BY symbol HAVING SUM(shares) > 0 ORDER BY price DESC", session["user_id"])

    user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

    current_worth = 0
    for stock in user_portfolio:
        stock_data = lookup(stock["symbol"])
        stock["currentprice"] = stock_data["price"]
        stock["totalprice"] = stock_data["price"] * stock["SUM(shares)"]
        current_worth += stock["totalprice"]

    return render_template("index.html", user_portfolio=user_portfolio, user_cash=user_cash, current_worth=current_worth)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_nbr = request.form.get("shares")

        if symbol == "":
            return apology("MISSING SYMBOL", 400)
        if shares_nbr == "" or shares_nbr.isalpha():
            return apology("MISSING SHARES", 400)
        if not is_int(shares_nbr):
            return apology("fractional not supported", 400)
        if int(shares_nbr) <= 0:
            return apology("share number can't be negative number or zero!", 400)

        stock_quote = lookup(symbol)

        if not stock_quote:
            return apology("INVALID SYMBOL", 400)

        total_cost = int(shares_nbr) * stock_quote["price"]

        user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        if user_cash[0]["cash"] < total_cost:
            return apology("CAN'T AFFORD", 400)

        else:
            db.execute("INSERT INTO trades (id, symbol, name, shares, price) VALUES(?, ?, ?, ?, ?)",
                       session["user_id"], stock_quote['symbol'], stock_quote['name'], int(shares_nbr), stock_quote['price'])
            cash = user_cash[0]["cash"]
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total_cost, session["user_id"])
            flash('Bought!')
            return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    user_transactions = db.execute(
        "SELECT id, symbol, shares, price, transacted  FROM trades WHERE id = ? ORDER BY transacted", session["user_id"])

    return render_template("history.html", user_transactions=user_transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if symbol == "":
            return apology("input is blank", 400)

        stock_quote = lookup(symbol)

        if not stock_quote:
            return apology("INVALID SYMBOL", 400)
        else:
            return render_template("quoted.html", symbol=stock_quote)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if not (password == confirmation):
            return apology("the passwords do not match", 400)

        if password == "" or confirmation == "" or username == "":
            return apology("input is blank", 400)

        if len(rows) == 1:
            return apology("username already exist", 400)
        else:
            hashcode = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashcode)

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_nbr = request.form.get("shares")

        if symbol == "":
            return apology("MISSING SYMBOL", 400)
        if shares_nbr == "" or shares_nbr.isalpha():
            return apology("MISSING SHARES", 400)
        if not is_int(shares_nbr):
            return apology("fractional not supported", 400)
        if int(shares_nbr) <= 0:
            return apology("share number can't be negative number or zero!", 400)
        stock_quote = lookup(symbol)

        if not stock_quote:
            return apology("INVALID SYMBOL", 400)

        user_portfolio = db.execute(
            "SELECT id, symbol, SUM(shares) FROM trades WHERE id = ? AND symbol = ? GROUP BY symbol HAVING SUM(shares)>0 ", session["user_id"], stock_quote['symbol'])
        user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        user_cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        if user_portfolio[0]["SUM(shares)"] < int(shares_nbr):
            return apology("TOO MANY SHARES", 400)
        else:
            currentprice = stock_quote['price'] * int(shares_nbr)
            cash = user_cash[0]["cash"]
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + currentprice, session["user_id"])
            db.execute("INSERT INTO trades (id, symbol, name, shares, price) VALUES(?, ?, ?, ?, ?)",
                       session["user_id"], stock_quote['symbol'], stock_quote['name'], -int(shares_nbr), stock_quote['price'])
            flash('Sold!')
        return redirect("/")

    else:
        user_portfolio = db.execute(
            "SELECT id, symbol, SUM(shares) FROM trades WHERE id = ? GROUP BY symbol HAVING SUM(shares)>0 ORDER BY symbol", session["user_id"])

        return render_template("sell.html", user_portfolio=user_portfolio)


@app.route("/settings")
@login_required
def settings():
    username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])
    return render_template("settings.html", username=username[0]['username'])


@app.route("/passwordupdate", methods=["GET", "POST"])
@login_required
def passwordupdate():
    if request.method == "POST":

        currentpassword = request.form.get("currentpassword")
        newpassword = request.form.get("newpassword")
        confirmation = request.form.get("confirmation")

        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        if not (newpassword == confirmation):
            return apology("the passwords do not match", 400)

        if currentpassword == "" or newpassword == "" or confirmation == "":
            return apology("input is blank", 400)

        if not check_password_hash(rows[0]["hash"], currentpassword):
            return apology("invalid password", 403)
        else:
            hashcode = generate_password_hash(newpassword, method='pbkdf2:sha256', salt_length=8)
            db.execute("UPDATE users SET hash = ? WHERE id = ?", hashcode, session["user_id"])

        return redirect("/settings")

    else:
        return render_template("passwordupdate.html")
