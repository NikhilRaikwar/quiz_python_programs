users = {}
results = {}

def register():
    print("Register:")
    name = input("Enter your name: ").lower()
    enroll_no = input("Enter your enrollment number: ").lower()
    if enroll_no in users:
        print("Enrollment number already exists. Please try logging in.")
        return False
    else:
        users[enroll_no] = name
        results[enroll_no] = 0
        print("Registration successful!")
        return True

def login():
    print("Login:")
    enroll_no = input("Enter your enrollment number: ").lower()
    name = input("Enter your name: ").lower()
    if enroll_no in users and users[enroll_no] == name:
        print(f"Welcome, {users[enroll_no]}!")
        return enroll_no
    else:
        print("Invalid credentials. Please try again.")
        return None

def dsa_quiz():
    score = 0
    questions = [
        {"question": "What is the full form of DSA?", 
         "options": ["1. Data Structure and Algorithm", "2. Data Science Algorithm", "3. Data Sort Algorithm", "4. Domain Search Algorithm"], 
         "answer": 1},
        {"question": "What is the average time complexity of searching for an element in a balanced BST?", 
         "options": ["1. O(1)", "2. O(log n)", "3. O(n)", "4. O(n log n)"], 
         "answer": 2},
        {"question": "Which data structure uses LIFO principle?", 
         "options": ["1. Queue", "2. Stack", "3. Array", "4. Linked List"], 
         "answer": 2},
        {"question": "What is the time complexity of accessing an element in an array?", 
         "options": ["1. O(n)", "2. O(1)", "3. O(log n)", "4. O(n log n)"], 
         "answer": 2},
        {"question": "Which algorithm is used to find the shortest path in a graph?", 
         "options": ["1. DFS", "2. BFS", "3. Dijkstra's Algorithm", "4. Kruskal's Algorithm"], 
         "answer": 3}
    ]
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (1-4): ")
        if answer.isdigit() and int(answer) == q["answer"]:
            score += 1
    return score

def dbms_quiz():
    score = 0
    questions = [
        {"question": "Which of the following is a primary key?", 
         "options": ["1. A unique identifier for each record", "2. A key that accepts null values", "3. A key for relationships", "4. A key that allows duplicates"], 
         "answer": 1},
        {"question": "What does ACID stand for in databases?", 
         "options": ["1. Atomicity, Consistency, Isolation, Durability", "2. Accuracy, Consistency, Integrity, Durability", "3. Atomicity, Coherence, Isolation, Data", "4. Availability, Consistency, Isolation, Durability"], 
         "answer": 1},
        {"question": "Which SQL statement is used to create a table?", 
         "options": ["1. INSERT INTO", "2. UPDATE", "3. CREATE TABLE", "4. ALTER TABLE"], 
         "answer": 3},
        {"question": "Which join returns all rows matching in either table?", 
         "options": ["1. INNER JOIN", "2. LEFT JOIN", "3. RIGHT JOIN", "4. FULL JOIN"], 
         "answer": 4},
        {"question": "What is the purpose of normalization?", 
         "options": ["1. To reduce redundancy", "2. To increase redundancy", "3. To ensure data in one table", "4. To simplify queries"], 
         "answer": 1}
    ]
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (1-4): ")
        if answer.isdigit() and int(answer) == q["answer"]:
            score += 1
    return score

def python_quiz():
    score = 0
    questions = [
        {"question": "Which of the following is a mutable data type?", 
         "options": ["1. Tuple", "2. List", "3. String", "4. Integer"], 
         "answer": 2},
        {"question": "Which keyword is used to define a function?", 
         "options": ["1. func", "2. def", "3. define", "4. function"], 
         "answer": 2},
        {"question": "Which function gets the length of a string?", 
         "options": ["1. length()", "2. strlen()", "3. len()", "4. size()"], 
         "answer": 3},
        {"question": "How do you assign 5 to a variable?", 
         "options": ["1. int x = 5", "2. x = 5", "3. declare x=5", "4. x:=5"], 
         "answer": 2},
        {"question": "What is the type of print(type(3.14))?", 
         "options": ["1. int", "2. float", "3. double", "4. string"], 
         "answer": 2}
    ]
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (1-4): ")
        if answer.isdigit() and int(answer) == q["answer"]:
            score += 1
    return score

def play_quiz(enroll_no):
    print("Welcome to the Quiz! Let's begin.")
    print("Choose a quiz section:")
    print("1. DSA")
    print("2. DBMS")
    print("3. Python")
    section = input("Enter your choice (1-3): ")
    if section == "1":
        score = dsa_quiz()
    elif section == "2":
        score = dbms_quiz()
    elif section == "3":
        score = python_quiz()
    else:
        print("Invalid section.")
        return
    results[enroll_no] = score
    if score >= 3:
        print(f"Congratulations! You passed the quiz with a score of {score}/5.")
    else:
        print(f"You did not pass the quiz. Your score is {score}/5.")

def main():
    while True:
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
                    print("1. Play Quiz")
                    print("2. Logout")
                    action = input("Choose an action: ")
                    if action == "1":
                        play_quiz(enroll_no)
                    elif action == "2":
                        break
                    else:
                        print("Invalid action.")
        elif choice == "3":
            print("Thank you for playing the Quiz. Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
