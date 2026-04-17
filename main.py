from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
    return "Calculator API is running!"

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json

    operation = data.get("operation")
    a = float(data.get("a", 0))
    b = data.get("b", 0))

    try:
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            result = a / b
        elif operation == "mod":
            result = a % b
        elif operation == "power":
            result = a ** b
        elif operation == "log":
            # log_b(a) 형태
            result = math.log(a, b)
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
