# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:10:31 2019

@author: suresh
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

import expenses as ex

app = Flask(__name__)
CORS(app)


@app.route('/v1.0/expenses', methods=['GET'])
def expenses():
    response = {}
    response['total_expenses'] = ex.total_expenses()
    response['top_expenses'] = ex.top_expenses()
    response['daywise_expenses'] = ex.daywise_transaction()
    response['datewise_expenses'] = ex.datewise_transaction()
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', 
            port='5005', 
            debug=True)
