import json
"""
    Calculate_category_and_health_risk will calculate the BMI category & Health Risk of a particular 
    entry and add same to the array.
"""
def calculate_category_and_health_risk(input_value):
    if input_value['BMI'] <= 18.4:
        input_value['BMI Category'] = "Underweight"
        input_value['Health risk'] = "Malnutrition risk"

    elif input_value['BMI'] >= 18.5 and input_value['BMI'] <= 24.9:
        input_value['BMI Category'] = "Normal weight"
        input_value['Health risk'] = "Low risk"

    elif input_value['BMI'] >= 25  and input_value['BMI'] <= 29.9:
        input_value['BMI Category'] = "Overweight"
        input_value['Health risk'] = "Enhanced risk"

    elif input_value['BMI'] > 30 and input_value['BMI'] <= 34.9:
        input_value['BMI Category'] = "Moderately obese"
        input_value['Health risk'] = "Medium risk"

    elif input_value['BMI'] > 35 and input_value['BMI'] <= 39.9:
        input_value['BMI Category'] = "Severely obese"
        input_value['Health risk'] = "High risk"

    else:
        input_value['BMI Category'] = "Very severely obese"
        input_value['Health risk'] = "Very high risk"
    
    return input_value

"""
    the function will calculate the count of obese persons based on the category. For now we have 
    used variations of obese categories but later down the line we can take the category as input and calculate
"""
def calculate_category(input_values_updated):
    overweight_people = 0
    for val in input_values:
        if val['BMI Category'] in ['Overweight']:
            overweight_people += 1

    return overweight_people

"""
    Main function which will be called when the script will executed and will return no. of overweight people and updated array
"""

def calculate_BMI(input_values):

    if not type(input_values) is list:
        print("Input values must be a list, {} was passed".format(type(input_values)))

        return

    for val in input_values:
        try:
            val["BMI"] = round(val["WeightKg"]/round((val["HeightCm"]/100)**2, 2) ,2)
        except ZeroDivisionError as e:
            val["BMI"] = 0.0
        
        calculate_category_and_health_risk(val)

    return input_values



if __name__ == "__main__":

    input_data_filepath = "input_data.json"
    output_filepath = "output_data_approach1.json"
    input_values = {}

    with open(input_data_filepath, 'r') as fp:
        input_values = json.load(fp)

    try:    
        input_values_updated  = calculate_BMI(input_values)
        with open(output_filepath, 'w') as fp:
            fp.write(json.dumps(input_values_updated))

        overweight_people = calculate_category(input_values_updated)
        print("Total no of overweight people are {}".format(overweight_people))

    except Exception as err:
        print("Check your script, got following error {}".format(err))

   
