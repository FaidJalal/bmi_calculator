import json
import pandas as pd
import math

PARALLELIZE = False

if PARALLELIZE:
    from pandarallel import pandarallel
    NUM_OF_CORES = 12
    pandarallel.initialize(nb_workers = NUM_OF_CORES)

# the mapping representing BMI category with BMI value range and health risk
MAPPING = {
    "Underweight"            : {'lower' : -math.inf, 'upper' : 18.49,    "risk" : 'Malnutrition Risk'},
    "Normal Weight"          : {'lower' : 18.50,     'upper' : 24.99,    "risk" : 'Low Risk'},
    "Overweight"             : {'lower' : 25,        'upper' : 29.99,    "risk" : 'Enhanced Risk'},
    "Moderately Obese"       : {'lower' : 30,        'upper' : 34.99,    'risk' : 'Medium Risk'},
    "Severely Obese"         : {'lower' : 35,        'upper' : 39.99,    'risk' : 'High Risk'},
    "Very Severly Obese"     : {'lower' : 40,        'upper' : math.inf, 'risk' : 'Very High Risk'}
    }


def cal_bmi(height, weight):
    """
    This function will calculate the BMI of a given entry.
    It will take 
    """

    height /= 100
    try:
        bmi = round(weight / (height**2), 2)
    except ZeroDivisionError as e:
        bmi = 0.0
    return bmi


def get_category_and_healthrisk(bmi_value):
    """

    """
    for category, range_risk in MAPPING.items():
        
        lower_limit = range_risk['lower']
        upper_limit = range_risk['upper']
        risk = range_risk['risk']
        
        if lower_limit <= bmi_value <= upper_limit:
            
            return category, risk


def generate_bmi_data(row):
    """
    """
    height_cm = row['HeightCm']
    weight_kg = row["WeightKg"]
    
    bmi = cal_bmi(height_cm, weight_kg)
    
    category, risk = get_category_and_healthrisk(bmi)
    
    row['BMI value'] = bmi
    row['BMI Category'] = category
    row['Health risk'] = risk
    
    return row


def get_counts_from_ranges(df, category):
    """
    """

    category_count = 0
    if category not in MAPPING:
        return 0
    for bmi_value in df['BMI value'].values:
        ranges_risk_dict = MAPPING.get(category)
        
        lower_limit = ranges_risk_dict['lower']
        upper_limit = ranges_risk_dict['upper']
            
        if lower_limit <= bmi_value <= upper_limit:
            
            category_count+=1
    return category_count
    

def main(json_file_path):
    """
    """

    with open(json_file_path, 'r') as fp:
        data = json.load(fp)

    df = pd.DataFrame(data)

    if not PARALLELIZE:
        # run when limited set of data
        df = df.apply(generate_bmi_data, axis = 1)
    else:
        # run when data is in millions | parallel mode
        df = df.parallel_apply(generate_bmi_data, axis=1)


    file_name = "output_data_approach2.json"
    df.to_json(file_name, orient = 'records', indent = 4)

    print("data saved : {}".format(file_name))


    check_category = 'Overweight'

    counts = get_counts_from_ranges(df, check_category)

    print('The counts for {} : {}'.format(check_category, counts))



if __name__ == '__main__':

    json_file_path = 'input_data.json'
    main(json_file_path) 
