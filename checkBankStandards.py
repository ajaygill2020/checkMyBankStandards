def conduct_survey():
    print("Welcome to Check My Bank Standards Application!")
    
    # Initialize a score to track the customer's security level
    security_score = 0
    
    # Ask questions related to bank security
    print("\nPlease answer the following questions with 'yes' or 'no' unless otherwise stated. Responding with no answer will result in the lowest score.")
    
    # Question 1
    answer1 = input("1. Do you use strong, unique passwords for your online banking AND mandate password resets every 4 months or earlier? ").lower()
    if answer1 == 'yes':
        security_score += 4  # Increment score if the password is strong and mandated password resets every 4 months. 
    
    # Question 2
    answer2 = input("2. Do you enable two-factor authentication (2FA) when available AND follow up on validating it every 3 months or earlier? ").lower()
    if answer2 == 'yes':
        security_score += 4  # Increment score if 2FA is enabled and follow-ups occur
    
    # Question 3
    answer3 = input("3. Do you mandate your customers to check their bank statements every 3 months or earlier for suspicious activities? ").lower()
    if answer3 == 'yes':
        security_score += 4  # Increment score if statements are regularly checked
    
    # Question 4
    answer4 = input("4. Have you installed AND regularly update antivirus software on your products? ").lower()
    if answer4 == 'yes':
        security_score += 3  # Increment score if antivirus is installed and updated
    
    # Question 5
    answer5 = input("5. What is your company size? Answer abc for 1-50, def for 51-99, ghi for 100 or more? ").lower()
    if answer5 == 'abc':
        security_score += 4  # Increment score 
    if answer5 == 'def':
        security_score += 2  # Increment score 
    if answer5 == 'ghi':
        security_score += 1  # Increment score 
    
# Question 6
    answer6 = input("6. What is your IT/security department size? Answer abc for 1-5, def for 6-19, ghi for 20 or more? ").lower()
    if answer6 == 'abc':
        security_score += 1  # Increment score 
    if answer6 == 'def':
        security_score += 2  # Increment score 
    if answer6 == 'ghi':
        security_score += 3  # Increment score

# Question 7
    answer7 = input("7. How often do you mandate employee security training? Answer abc for every 4 months, def for fewer than 4 months, ghi for more than 4 months. ").lower()
    if answer7 == 'abc':
        security_score += 1  # Increment score 
    if answer7 == 'def':
        security_score += 3  # Increment score 
    if answer7 == 'ghi':
        security_score += 0  # Increment score

    # Display the final security score
    print("\nThank you for answering the questions!")
    print(f"Your bank security score is: {security_score}/25")
    
    # Provide a recommendation based on the score
    if security_score >= 17:
        print("Great job! Your bank security practices are excellent. Refer to this link: https://www.cisa.gov/topics/cybersecurity-best-practices")
    elif 11 <= security_score < 17:
        print("Good effort, but there is room for improvement in bank security. Refer to this link: https://www.cisa.gov/topics/cybersecurity-best-practices")
    else:
        print("You scored poorly. Consider enhancing your bank security practices for better protection. Refer to this link: https://www.cisa.gov/topics/cybersecurity-best-practices")

# Run the questionnaire
conduct_survey()
