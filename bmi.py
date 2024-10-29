def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)
    print("BMI = " + str(bmi))

    # Determine weight classification based on BMI and return corresponding value
    if bmi < 18.5:
        classification = "Under Weight"
        return -1
    elif 18.5 <= bmi <= 25.0:
        classification = "Normal Weight"
        return 0
    else:
        classification = "Over Weight"
        return 1

# Example call with weight=57 kg and height=1.73 m
result = calculate_bmi(weight=57, height=1.73)
print("Return Value = " + str(result))
