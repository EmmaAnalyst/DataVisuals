from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Raw data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Age': [28, 35, 42, 31, 25, 39],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'Height(cm)': [165, 178, 172, 160, 170, 180],
    'Weight(kg)': [60, 80, 75, 55, 68, 85],
    'Blood Pressure': ['120/80', '130/85', '125/78', '115/70', '118/72', '135/88']
}

# Creating a DataFrame
df = pd.DataFrame(data)
df[['Systolic_BP', 'Diastolic_BP']] = df['Blood Pressure'].str.split('/', expand=True)
df['Systolic_BP'] = df['Systolic_BP'].astype(int)
df['Diastolic_BP'] = df['Diastolic_BP'].astype(int)

@app.route('/')
def index():
    data = {
        'ages': df['Age'].tolist(),
        'heights': df['Height(cm)'].tolist(),
        'weights': df['Weight(kg)'].tolist(),
        'genders': df['Gender'].tolist(),
        'systolic_bp': df['Systolic_BP'].tolist(),
        'diastolic_bp': df['Diastolic_BP'].tolist()
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

