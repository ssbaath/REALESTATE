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


@app.route('/get_location_names', methods= ['GET'])
def get_location_names():
    response = jsonify({
        'locations': abby.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_house_price', methods= ['GET','POST'])
def predict_house_price():

    suburbs = request.form['suburbs']
    bedroom2 = int(request.form['bedroom2'])
    bathroom = int(request.form['bathroom'])
    car = int(request.form['car'])
    buildingarea = float(request.form['buildingarea'])


    response = jsonify({
        'estimated_price': abby.price_estimate(suburbs, bedroom2, bathroom, car, buildingarea)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    abby.load_saved_artifcats()
    app.run(debug=True, host='0.0.0.0', port=8080)

