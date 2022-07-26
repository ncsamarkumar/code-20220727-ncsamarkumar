
"""
All constants are declared here, useful for DRY (Don't repeat yourself)
"""

STANDARDS = {
    "Under Weight": ["<18.4", "Malnutrition risk"],
    "Normal Weight": ["18.5 - 24.9", "Low risk"],
    "Over Weight": ["25 - 29.9", "Enhanced risk"],
    "Moderately obese": ["30 - 34.9", "Medium risk"],
    "Severely obese": ["35 - 39.9", "High risk"],
    "Very severely obese": ["40+", "Very high risk"]
}

HEADER = ['Gender', 'HeightCm', 'WeightKg', 'BMI (kg/m²)',
          'BMI Category', 'BMI Range (kg/m2)', 'Health Risk']

RESULT = [[], ['Stats']]
GENDER = "Gender"
U_WEIGHT = "Under Weight"
N_WEIGHT = "Normal Weight"
O_WEIGHT = "Over Weight"
M_OBESE = "Moderately obese"
S_OBESE = "Severely obese"
VS_OBESE = "Very severely obese"
HEIGHTCM = 'HeightCm'
WEIGHTKG = 'WeightKg'
