from flask import Flask, request
import numpy
import pandas

app = Flask(__name__)


@app.route("/getbmidata", methods=["POST"])
def bmi_calc():
    """
    This functions takes the input JSON as GET request and process the BMI data and count of overweight persons in html
    """
    userdata = request.get_json()   # Receives the input JSON
    userdata = pandas.DataFrame(userdata)   # Prepared dataframe of the JSON payload
    userdata["BMI"] = userdata["WeightKg"] / (userdata["HeightCm"] / 100) ** 2  # Dataframe operation to calculate BMI

    def bmi_category(bmi):
        """
        This function takes BMI value as a parameter and returns BMI category and Health risk of each person as a tuple
        """
        if bmi < 18.5:
            return "Underweight", "Malnutrition risk"
        elif bmi < 25:
            return "Normal weight", "Low risk"
        elif bmi < 30:
            return "Overweight", "Enhanced risk"
        elif bmi < 35:
            return "Moderately obese", "Medium risk"
        elif bmi < 40:
            return "Severely obese", "High risk"
        else:
            return "Very severely obese", "Very high risk"

    category = numpy.array(userdata["BMI"].apply(bmi_category).tolist())    # Numpy array of BMI category data
    userdata["BMI Category"], userdata["Health risk"] = category[:, 0], category[:, 1]  # New columns added
    count = userdata[userdata["BMI Category"] == "Overweight"]["BMI Category"].count()  # Number of  overweight people
    update_str = f"</br><b> The total number of overweight people is {count} </b>"
    html_data = f"{userdata.to_html()}{update_str}"
    return html_data


app.run()



