from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def check_odd_even(number):
    return "odd" if number % 2 != 0 else "even"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_odd_even', methods=['POST'])
def check_odd_even_route():
    try:
        data = request.get_json()
        number = data['number']
        result = check_odd_even(number)
        return jsonify({"result": result})
    except KeyError:
        return jsonify({"error": "Invalid input. 'number' field missing."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0",port=8000)

