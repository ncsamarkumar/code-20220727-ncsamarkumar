"""
To calculate the BMI of a person and
 to get BMI Category and the Health Risk
"""

from decimal import Decimal

from constants import STANDARDS, U_WEIGHT, N_WEIGHT, O_WEIGHT, M_OBESE, S_OBESE, VS_OBESE
import errors
import utils


class BMI:
    """
    Bmi Class to calculate Bmi and get Bmi status
    """

    def __init__(self, height: float = "", weight: float = "", bmi_value: float = ""):
        self.height = height
        self.weight = weight
        self.bmi_value = bmi_value

    def compare_bmi(self):

        """
        Based on Bmi value it will return category and healthrisk of a person
        """

        # Removing spaces if present any
        bmi_value = (str(self.bmi_value)).strip()

        try:
            bmi_value = float(bmi_value)
        except ValueError:
            return errors.BMI_MISSING

        # As per given standards limiting to single decimal.
        bmi_value = round(bmi_value, 1)

        # removing the trailing zeros from decimal
        bmi_value = utils.remove_exponent(Decimal(str(bmi_value)))

        # Comparing the Bmi status
        if bmi_value <= 18.4:
            return [U_WEIGHT]+STANDARDS[U_WEIGHT]
        if 18.5 < bmi_value <= 24.9:
            return [N_WEIGHT]+STANDARDS[N_WEIGHT]
        if 25 < bmi_value <= 29.9:
            return [O_WEIGHT]+STANDARDS[O_WEIGHT]
        if 30 < bmi_value <= 34.9:
            return [M_OBESE]+STANDARDS[M_OBESE]
        if 35 < bmi_value <= 39.9:
            return [S_OBESE]+STANDARDS[S_OBESE]

        return [VS_OBESE]+STANDARDS[VS_OBESE]

    def to_calculate_bmi(self):

        """
        Based on Height and weight it will calculate BMI
        """

        height = (str(self.height)).strip()
        weight = (str(self.weight)).strip()

        # Checking the value is only number.
        try:
            height = float(height)
        except ValueError:
            return errors.HEIGHT_MISSING

        try:
            weight = float(weight)
        except ValueError:
            return errors.WEIGHT_MISSING

        # Performing BMI calculation
        height_to_meters = height / 100
        self.bmi_value = weight / (height_to_meters ** 2)
        return round(self.bmi_value, 2)


if __name__ == "__main__":
    bmi = BMI()
