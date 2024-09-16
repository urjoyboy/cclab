
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Define HTML template with embedded CSS
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGPA Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }

        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            width: 300px;
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        .subject {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
        }

        input {
            width: calc(100% - 22px);
            padding: 8px;
            margin-bottom: 5px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #28a745;
            border: none;
            color: white;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #218838;
        }

        #result {
            margin-top: 20px;
            font-size: 18px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>CGPA Calculator</h1>
        <form method="post">
            <div class="subject">
                <label for="sub1">Subject 1 Grade:</label>
                <input type="number" id="sub1" name="sub1" step="any" required>
                <label for="sub1_credits">Credits:</label>
                <input type="number" id="sub1_credits" name="sub1_credits" step="any" required>
            </div>
            <div class="subject">
                <label for="sub2">Subject 2 Grade:</label>
                <input type="number" id="sub2" name="sub2" step="any" required>
                <label for="sub2_credits">Credits:</label>
                <input type="number" id="sub2_credits" name="sub2_credits" step="any" required>
            </div>
            <div class="subject">
                <label for="sub3">Subject 3 Grade:</label>
                <input type="number" id="sub3" name="sub3" step="any" required>
                <label for="sub3_credits">Credits:</label>
                <input type="number" id="sub3_credits" name="sub3_credits" step="any" required>
            </div>
            <div class="subject">
                <label for="sub4">Subject 4 Grade:</label>
                <input type="number" id="sub4" name="sub4" step="any" required>
                <label for="sub4_credits">Credits:</label>
                <input type="number" id="sub4_credits" name="sub4_credits" step="any" required>
            </div>
            <div class="subject">
                <label for="sub5">Subject 5 Grade:</label>
                <input type="number" id="sub5" name="sub5" step="any" required>
                <label for="sub5_credits">Credits:</label>
                <input type="number" id="sub5_credits" name="sub5_credits" step="any" required>
            </div>
            <button type="submit">Calculate CGPA</button>
        </form>
        {% if cgpa is not none %}
        <div id="result">
            <h2>Calculated CGPA: {{ cgpa | round(2) }}</h2>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        grades = [
            float(request.form.get('sub1')),
            float(request.form.get('sub2')),
            float(request.form.get('sub3')),
            float(request.form.get('sub4')),
            float(request.form.get('sub5'))
        ]
        credits = [
            float(request.form.get('sub1_credits')),
            float(request.form.get('sub2_credits')),
            float(request.form.get('sub3_credits')),
            float(request.form.get('sub4_credits')),
            float(request.form.get('sub5_credits'))
        ]
        
        # Calculate CGPA
        total_credits = sum(credits)
        weighted_sum = sum(grade * credit for grade, credit in zip(grades, credits))
        cgpa = weighted_sum / total_credits if total_credits > 0 else 0
        
        return render_template_string(HTML_TEMPLATE, cgpa=cgpa)
    
    return render_template_string(HTML_TEMPLATE, cgpa=None)

if __name__ == '__main__':
    app.run(debug=True)
