from flask import Flask, render_template, request

aplikasi = Flask(__name__)

@aplikasi.route("/")
def app():
    return render_template("jajargenjang.html")

@aplikasi.route("/send", methods=["POST"])
def send(sum=sum):
    if request.method == "POST":
        jajargenjang = request.form["jajargenjang"]
        jajargenjang2 = request.form["jajargenjang2"]
        jajargenjang3 = request.form["jajargenjang3"]
        sum = float(jajargenjang)
        sum2 = float(jajargenjang2)
        sum3 = float(jajargenjang3)
        result = sum * sum2
        result2 = 2 * (sum + sum3)
        return render_template("jajargenjang.html", sum=result, sum2=result2, sum3=sum2)
    else:
        return render_template("jajargenjang.html")

if __name__ == '__main__':
    aplikasi.run(debug=True)
