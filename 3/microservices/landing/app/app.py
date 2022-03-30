from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

def get_result(number_1, number_2, operation):
    url = 'http://microservices_{}-service_1:5050/{}/{}'.format(operation, number_1, number_2)
    response = requests.get(url)
    result = response.text
    return result

@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        number_1 = int(request.form.get("first"))
        number_2 = int(request.form.get('second'))
        operation = request.form.get('operation')
        result = get_result(number_1, number_2, operation)

        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
    except e:
        pass
    finally:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )