from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model using joblib
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get user inputs
        high_price = float(request.form['high'])
        low_price = float(request.form['low'])
        open_price = float(request.form['open'])
        volume = float(request.form['volume'])

        # Create a DataFrame for prediction
        input_data = pd.DataFrame({
            'High': [high_price],
            'Low': [low_price],
            'Open': [open_price],
            'Volume': [volume]
        })

        # Predict the Close price
        prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)