def register():
    with open("users.txt", "a") as file:
        name = input("Enter your name: ").lower()
        enroll_no = input("Enter your enrollment number: ").lower()
        
        with open("users.txt", "r") as read_file:
            for line in read_file:
                if enroll_no in line:
                    print("Enrollment number already exists.")
                    return False
        
        file.write(f"{enroll_no}|{name}\n")
        print("Registration successful!")
        return True

def login():
    enroll_no = input("Enter your enrollment number: ").lower()
    name = input("Enter your name: ").lower()
    
    with open("users.txt", "r") as file:
        for line in file:
            stored_enroll_no, stored_name = line.strip().split("|")
            if stored_enroll_no == enroll_no and stored_name == name:
                print(f"Welcome, {stored_name}!")
                return enroll_no
    print("Invalid credentials. Please try again.")
    return None

def load_questions(section):
    questions = []
    with open("questions.txt", "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if parts[0].lower() == section.lower():
                questions.append(parts[1:])
    return questions

def play_quiz(enroll_no):
    print("Choose a quiz section:")
    print("1. DBMS")
    print("2. DSA")
    print("3. Python")
    
    section_choice = input("Enter the section number (1-3): ")
    section_map = {"1": "DBMS", "2": "DSA", "3": "Python"}
    
    if section_choice not in section_map:
        print("Invalid section choice. Returning to main menu.")
        return
    
    section = section_map[section_choice]
    questions = load_questions(section)
    if not questions:
        print("No questions found for this section.")
        return
    
    score = 0
    for question in questions:
        print(question[0])
        for option in question[1:5]:
            print(option)
        answer = input("Enter your answer (1-4): ")
        if answer.isdigit() and int(answer) == int(question[5]):
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")
    
    print(f"Your score: {score}/{len(questions)}")
    with open("results.txt", "a") as file:
        file.write(f"{enroll_no}|{section}|{score}\n")

def show_results(enroll_no):
    print("Your past scores:")
    found = False
    with open("results.txt", "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) != 3:  # Skip invalid lines
                continue
            stored_enroll_no, section, score = parts
            if stored_enroll_no == enroll_no:
                print(f"{section}: {score}")
                found = True
    if not found:
        print("No results found for you.")


def main():
    while True:
        print("\nWelcome to the Python Programming Quiz Application!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            enroll_no = login()
            if enroll_no:
                while True:
                    print("\n1. Play Quiz")
                    print("2. Show Results")
                    print("3. Logout")
                    action = input("Choose an action: ")
                    if action == "1":
                        play_quiz(enroll_no)
                    elif action == "2":
                        show_results(enroll_no)
                    elif action == "3":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid action. Please try again.")
        elif choice == "3":
            print("Thank you for playing the Quiz. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
