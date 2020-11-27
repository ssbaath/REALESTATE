from flask import Flask, request, jsonify, render_template
import abby

app = Flask(__name__)

@app.route("/")
def first():
    return render_template("firstpage.html")

@app.route("/second")
def second():
    return render_template("app.html")

@app.route("/third")
def third():
    return render_template("task.html")

@app.route("/fourth")
def fourth():
    return render_template("ipynb.html")

@app.route('/price', methods= ['GET','POST'])
def price_prediction():

    suburbs = request.form['suburbs']
    bedroom2 = int(request.form['bedroom2'])
    bathroom = int(request.form['bathroom'])
    car = int(request.form['car'])
    buildingarea = float(request.form['buildingarea'])


    input = jsonify({
        'suburb_price': abby.price(suburbs, bedroom2, bathroom, car, buildingarea)
    })
    input.headers.add('Access', '*')

    return input

@app.route('/suburbs', methods= ['GET'])
def suburbs():
    input = jsonify({
        'sub': abby.suburbs()
    })
    input.headers.add('Access', '*')

    return input



if __name__ == "__main__":
    abby.savedvals()
    app.run(debug=True, host='0.0.0.0', port=8080)

