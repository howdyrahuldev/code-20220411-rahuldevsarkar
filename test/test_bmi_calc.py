import requests


def test_bmidata():
    json_body = [
                     {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                     {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
                     {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
                     {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                     {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                     {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
                     {"Gender": "Female", "HeightCm": 175, "WeightKg": 75},
                     {"Gender": "Male", "HeightCm": 189, "WeightKg": 100},
                     {"Gender": "Female", "HeightCm": 189, "WeightKg": 100}
                ]
    expected_output = open("test.html").read()
    response = requests.post(r"http://127.0.0.1:5000/getbmidata", json=json_body)
    assert expected_output == response.text
