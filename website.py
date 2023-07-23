from flask import Flask, redirect,url_for, render_template, request

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ej1", methods = ["GET","POST"])
def ej1():
    if request.method == "POST":
        numinput = request.form["numinput"]
        numbers = list(range(1,int(numinput)+1))
        return render_template("ejercicio1.html", numinput = numinput, numbers=numbers)
    return render_template("ejercicio1.html")

@app.route("/ej2", methods = ["GET","POST"])
def ej2():
    if request.method == "POST":
        numinput = request.form["numinput"]
        numbers = list(range(1,int(numinput)+1))
        return render_template("ejercicio2.html", numinput = numinput, numbers=numbers)
    return render_template("ejercicio2.html")

@app.route("/ej3", methods = ["GET","POST"])
def ej3():
    if request.method == "POST":
        numinput = request.form["numinput"]
        numbers = []

        for num in range(1, int(numinput)+1):
            if int(numinput) % num == 0:
                numbers.append(num)

        return render_template("ejercicio3.html", numinput = numinput, numbers=numbers)
    return render_template("ejercicio3.html")

if __name__ == "__main__":
    app.run(debug = True)

