## flask app for hello world

# from flask import Flask
# # import numpy as np
# # import pandas as pd

# app=Flask(__name__)

# @app.route('/',methods=['GET'])
# def home():
#     return "Hello World"



# if __name__=="__main__":
#     app.run(host="0.0.0.0",port=8000)


def check_odd_even(number):
    
    if number%2==0 :
        print('The number is even')
    else :
        print('The number is odd')


test = check_odd_even(10)