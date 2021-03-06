from flask import Flask, render_template, make_response, send_from_directory
app = Flask(__name__)

"""The following routes corrospond to folders in the 'templates' folder"""

@app.route('/lab1')
def lab1():
    vxml = render_template('lab1/lab1.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab2')
def lab2():
    vxml = render_template('lab2/lab2.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab2_part2')
def lab2_part2():
    vxml = render_template('lab2/lab2_part2.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab3')
def lab3():
    vxml = render_template('lab3/lab3.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/lab4')
def lab4():
    vxml = render_template('lab4/lab4.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/grammars/<path:path>')
def send_grammar(path):
    return send_from_directory('grammars', path)

@app.route('/delayed_flights')
def delayed_flights():
    vxml = render_template('lab1/delayed_flights.xml', temp=temp)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/life_advice')
def life_advice():
    vxml = render_template('lab1/life_advice.xml', temp=temp)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/flight_booking')
def flight_booking():
    vxml = render_template('lab1/flight_booking.xml', temp=temp)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response
