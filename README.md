# BMI calculator along with the tests

## Python BMI Calculator Coding Challenge
Problem Statement:<br/>
Given the following JSON data
`[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]` ​ as the input with weight and height parameters of a person,
we have to perform the following:

- Calculate the BMI (Body Mass Index) using ​ Formula 1​ , BMI Category and Health
risk ​ from Table 1​ of the person and add them as 3 new columns
- Count the total number of overweight people using ranges in the column BMI
Category of ​ Table 1,​ check this is consistent programmatically and add any other
observations in the documentation
- Create build, tests to make sure the code is working as expected and this can be
added to an automation build / test / deployment pipeline

### Prerequisites:
- python 3.6 or greater
- python dependencies like pandas etc which are in requirements.txt

### Steps:

- clone the repo
- setup virutal env and install python dependencies with **pip install -r requirements.txt**
- next we have to set in the path to the json file and the result type in the calculate_bmi.py (at the end)
- There is also parallelize option which is discussed below.

## Approach 1 - Working
- For approach 1, we calculate the BMI using the function calculate_BMI which will also evaluate the category and health risk based on the BMI

## Aproach 2 - Working:
- In this approach i have made use of pandas DF to execute the functionality as pandas can handle approx 1 lac records.

## For the Question of Larger Json and Scaling up and parallelization
For the purpose of larger data and scaling up, we can make use of parrallelization using the CPU cores and pythons multiprocessing library. As in case of pandas Pandarallel. 


