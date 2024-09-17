from flask import Flask, render_template, request
import pickle
# render_template is a method called from Flask package
# get method - 'request' from the flask

#create object here app is object
app = Flask(__name__)

with open('churn_rfc_model', 'rb') as f:
    model = pickle.load(f)            # load the file 'f' and store it in the variable 'model'

# creating route to define API / endpoint
@app.route('/')  # by default GET http methods is taken here
def index():
    return render_template('index.html') #specify which page need to be displayed

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST','GET'])
def result():
    tenure = float(request.form.get('tenure'))   #get('tenure') -> from the front-end 'name' attribute we have to take 'name'
    monthly_charges = float(request.form.get('monthly_charges'))   
    total_charges = float(request.form.get('total_charges'))
    multiple_lines = int(request.form.get('multiple_lines'))  
    internet_service = int(request.form.get('internet_service'))   
    online_backup = int(request.form.get('online_backup'))   
    device_protection = int(request.form.get('device_protection'))   
    tech_support = int(request.form.get('tech_support'))   
    contract_encoder = int(request.form.get('contract_encoder'))    
    payment_method = int(request.form.get('payment_method')) 

    # while taking(input) data we have to take in 2-D array form
    # input is 1-D array and while predicting i have kept in 1-D array which has become 2-D array
    input=[tenure,monthly_charges,total_charges,multiple_lines,internet_service,online_backup,device_protection,tech_support,contract_encoder,payment_method]  #input shape is 1-D

    # model.predict([input])[0]  #here again we put the square brakect so it as become 2-D

    # instead of above code we write this
    predict=model.predict([input]) # input is given to the model to print
    print(predict)
    if predict==[0]:
        result="No Churn"
    else:
        result="Churn"

    # instead we can also do it directly by using double square bracket for input and no need to put square bracket in predicting side

    # res is a variable created to show the result in the front-end
    return render_template('result.html', res=result)

if __name__ == '__main__':
    app.run(debug=True)
