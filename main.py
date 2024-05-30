from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open("src/Thyroid_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('predict.html')

@app.route("/moreinfo", methods=["GET", "POST"])
def moreinfo():
    return render_template('moreinfo.html')

@app.route("/predictresult", methods=["POST"])
def predictresult():
    if request.method == "POST":
        Age = float(request.form.get('age'))
        Sex = request.form.get('sex')
        Level_thyroid_stimulating_hormone = float(request.form.get('TSH'))
        Total_thyroxine_TT4 = float(request.form.get('TT4'))
        Free_thyroxine_index = float(request.form.get('FTI'))
        On_thyroxine = request.form.get('on_thyroxine')
        On_antithyroid_medication = request.form.get('on_antithyroid_medication')
        Goitre = request.form.get('goitre')
        Hypopituitary = request.form.get('hypopituitary')
        Psychological_symptoms = request.form.get('psych')
        T3_measured = request.form.get('T3_measured')

        # Convert categorical variables to numerical
        Sex = 1 if Sex == "Male" else 0
        On_thyroxine = 1 if On_thyroxine == "True" else 0
        On_antithyroid_medication = 1 if On_antithyroid_medication == "True" else 0
        Goitre = 1 if Goitre == "True" else 0
        Hypopituitary = 1 if Hypopituitary == "True" else 0
        Psychological_symptoms = 1 if Psychological_symptoms == "True" else 0
        T3_measured = 1 if T3_measured == "True" else 0

        arr = np.array([[Age, Sex, Level_thyroid_stimulating_hormone, Total_thyroxine_TT4, Free_thyroxine_index,
                         On_thyroxine, On_antithyroid_medication, Goitre, Hypopituitary, Psychological_symptoms,
                         T3_measured]])
        pred = model.predict(arr)

        if pred == 0:
            res_Val = "Compensated Hypothyroid"
        elif pred == 1:
            res_Val = "No Thyroid"
        elif pred == 2:
            res_Val = 'Primary Hypothyroid'
        elif pred == 3:
            res_Val = 'Secondary Hypothyroid'

        output = f"Patient has {res_Val}"
        return render_template('predictresult.html', output=output)

if __name__ == "__main__":
    app.run(debug=False)
