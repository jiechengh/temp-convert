from flask import Flask, request, render_template_string

app = Flask(__name__)


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        temp = float(request.form.get("temperature"))
        conversion_type = request.form.get("conversion_type")

        if conversion_type == "ftoc":
            result = fahrenheit_to_celsius(temp)
            result = f"{temp}°F is equal to {result:.2f}°C"
        elif conversion_type == "ctof":
            result = celsius_to_fahrenheit(temp)
            result = f"{temp}°C is equal to {result:.2f}°F"

    return render_template_string("""
        <!doctype html>
        <title>Temperature Conversion</title>
        <h1>Temperature Conversion Tool</h1>
        <form method="post">
            <label for="temperature">Enter Temperature:</label>
            <input type="number" step="0.01" id="temperature" name="temperature" required>
            <br>
            <label for="ftoc">Fahrenheit to Celsius</label>
            <input type="radio" id="ftoc" name="conversion_type" value="ftoc" required>
            <br>
            <label for="ctof">Celsius to Fahrenheit</label>
            <input type="radio" id="ctof" name="conversion_type" value="ctof" required>
            <br>
            <input type="submit" value="Convert">
        </form>
        {% if result %}
            <h2>{{ result }}</h2>
        {% endif %}
    """, result=result)


if __name__ == "__main__":
    app.run(debug=True)
