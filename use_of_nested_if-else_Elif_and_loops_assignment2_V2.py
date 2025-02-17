def determine_grades():
    scores = [90, 60, 40, 100, 80, 70, 10, 100, 100, 100]  # List of scores
    
    for score in scores:
        if score > 80:
            grade = 'A'
        elif 70 <= score <= 80:
            grade = 'B'
        elif 60 <= score < 70:
            grade = 'C'
        elif 50 <= score < 60:
            grade = 'D'
        else:
            grade = 'F'  # For scores less than 50
        
        print(f"Score: {score}, Grade: {grade}")

# Call the function directly
determine_grades()
