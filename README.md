# Old Bike Price Prediction

This project is a Machine Learning-based web application that predicts the resale price of used bikes. The model is trained on historical used bike data and estimates the expected selling price based on user inputs.

## Features
- Predicts the resale price of old bikes.
- Simple and user-friendly web interface.
- Machine Learning model for price prediction.
- Supports multiple bike brands and owner types.
- Instant price prediction.

## Technologies Used
- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML
- CSS

## Input Parameters
- Brand
- Owner Type
- Age of Bike
- Kilometers Driven
- Power (CC)

## Output
- Predicted resale price of the used bike.

## Project Structure

```
Old-Bike-Price-Prediction/
│── Data/
│   └── Used_Bikes.csv
│
│── Model/
│   └── RandomForestRegressor.lb
│
│── static/
│   ├── css/
│   └── images/
│
│── templates/
│   ├── index.html
│   ├── about.html
│   └── contact.html
│
│── app.py
│── requirements.txt
│── README.md
```

## How to Run

1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Author

Krishan
