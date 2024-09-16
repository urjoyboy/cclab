from flask import Flask, render_template_string, request

app = Flask(__name__)

# Define arithmetic functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

# Define HTML template as a string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
</head>
<body>
    <h1>Simple Calculator</h1>
    <form method="post">
        <label for="num1">Enter the first number:</label>
        <input type="text" id="num1" name="num1" required><br><br>
        
        <label for="num2">Enter the second number:</label>
        <input type="text" id="num2" name="num2" required><br><br>

        <label for="operation">Select an operation:</label>
        <select id="operation" name="operation">
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select><br><br>

        <input type="submit" value="Calculate">
    </form>

    <div>
        <h2>Result:</h2>
        <p>{{ result }}</p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')

            if operation == 'add':
                result = add(num1, num2)
            elif operation == 'subtract':
                result = subtract(num1, num2)
            elif operation == 'multiply':
                result = multiply(num1, num2)
            elif operation == 'divide':
                result = divide(num1, num2)
            else:
                result = "Invalid operation."
        except ValueError:
            result = "Invalid input. Please enter valid numeric values."

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
