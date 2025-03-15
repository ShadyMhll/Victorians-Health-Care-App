app = Flask(__name__)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json

    weight = float(data['weight'])
    height = float(data['height'])
    temperature = float(data['temperature'])
    headache = data['headache']
    stomachPain = data['stomachPain']
    gender = data['gender']
    dizzy = data['dizzy']
    cholesterol = data['cholesterol']
    bloodPressure = data['bloodPressure']

    diagnosis = []

    if temperature > 37.5:
        diagnosis.append("- Fever. Take Paracetamol (500mg).")
    if headache == "yes":
        diagnosis.append("- Headache. Take Ibuprofen (400mg).")
    if stomachPain == "yes":
        diagnosis.append("- Stomach pain. Take Omeprazole (20mg).")
    if dizzy == "yes":
        diagnosis.append("- Dizziness. Rest and drink water.")
    if cholesterol == "yes":
        diagnosis.append("- High cholesterol. Consult a doctor.")
    if bloodPressure == "low":
        diagnosis.append("- Low blood pressure. Increase salt intake.")
    if bloodPressure == "high":
        diagnosis.append("- High blood pressure. Consult a doctor.")

    bmi = weight / ((height / 100) * (height / 100))
    if bmi > 25:
        diagnosis.append("- Overweight. Exercise and eat healthy.")
    elif bmi < 18.5:
        diagnosis.append("- Underweight. Consult a nutritionist.")
    else:
        diagnosis.append("- Healthy weight.")

    return jsonify({"diagnosis": "\n".join(diagnosis)})

if _name_ == '_main_':
    app.run(debug=True)