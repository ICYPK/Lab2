def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)
    print("BMI = " + str(bmi))

    # Determine weight classification based on BMI
    if bmi < 18.5:
        classification = "Under Weight"
    elif 18.5 <= bmi <= 25.0:
        classification = "Normal Weight"
    else:
        classification = "Over Weight"

    # Display the classification
    print("Weight Classification = " + classification)

# Example call with weight=57 kg and height=1.73 m
calculate_bmi(weight=57, height=1.73)
