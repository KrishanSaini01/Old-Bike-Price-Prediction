from flask import Flask,render_template, url_for,request
import pandas as pd
import joblib
model=joblib.load(r"Model\\RandomForestRegressor.lb")
app = Flask(__name__)

df =pd.read_csv('Data\\Used_Bikes.csv')

brand_list= df['brand'].unique().tolist()
brand_dict={b:i+1 for i,b in enumerate(brand_list)}


owner_list= df['owner'].unique().tolist()
owner_dict={o:i+1 for i,o in enumerate(owner_list)}

def get_dropdown_options():

    return {
        'brands': brand_list,
        'owners': owner_list,        
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/project')
def project():
    return render_template('project.html',**get_dropdown_options())


@app.route('/predict', methods=['POST'])
def predict():

    brand_name = request.form['brand_name']
    owner = request.form['owner']
    age = int(request.form['age'])
    power = int(request.form['power'])
    kms_driven = int(request.form['kms_driven'])

    brand_name = int(brand_dict.get(brand_name))
    owner = int(owner_dict.get(owner))

    data = [[brand_name, owner, age, power, kms_driven]]

    pred = int(model.predict(data)[0])

    print("Prediction >>>>", pred)

    return render_template(
        'project.html',
        **get_dropdown_options(),
        prediction= pred
    )
    

if __name__ == "__main__":
    app.run(debug=True)