
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Define temperature conversion functions
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

# Define HTML template as a string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Temperature Converter</title>
</head>
<body>
    <h1>Temperature Converter</h1>
    <form method="post">
        <label for="choice">Choose a conversion:</label>
        <select id="choice" name="choice" onchange="toggleInputs()">
            <option value="">Select an option</option>
            <option value="1">Fahrenheit to Celsius</option>
            <option value="2">Celsius to Fahrenheit</option>
        </select><br><br>

        <div id="fahrenheit-input" style="display:none;">
            <label for="fahrenheit">Enter temperature in Fahrenheit:</label>
            <input type="text" id="fahrenheit" name="fahrenheit"><br><br>
        </div>

        <div id="celsius-input" style="display:none;">
            <label for="celsius">Enter temperature in Celsius:</label>
            <input type="text" id="celsius" name="celsius"><br><br>
        </div>

        <input type="submit" value="Convert">
    </form>

    <div>
        <h2>Result:</h2>
        <p>{{ result }}</p>
    </div>

    <script>
        function toggleInputs() {
            var choice = document.getElementById('choice').value;
            document.getElementById('fahrenheit-input').style.display = choice == '1' ? 'block' : 'none';
            document.getElementById('celsius-input').style.display = choice == '2' ? 'block' : 'none';
        }
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == '1':
            try:
                f_temp = float(request.form.get('fahrenheit'))
                c_temp = fahrenheit_to_celsius(f_temp)
                result = f"{f_temp}°F is approximately {c_temp:.2f}°C."
            except ValueError:
                result = "Invalid input. Please enter a valid numeric value."
        elif choice == '2':
            try:
                c_temp = float(request.form.get('celsius'))
                f_temp = celsius_to_fahrenheit(c_temp)
                result = f"{c_temp}°C is approximately {f_temp:.2f}°F."
            except ValueError:
                result = "Invalid input. Please enter a valid numeric value."
        else:
            result = "Invalid choice. Please select 1 or 2."

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
