from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Api, Resource, reqparse

import requests
import os
from math import gcd


class GCDService(Resource):
    def get(self, argument0, argument1):
        return gcd(argument0, argument1), 200

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

api = Api(app)
api.add_resource(GCDService, '/<int:argument0>/<int:argument1>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )