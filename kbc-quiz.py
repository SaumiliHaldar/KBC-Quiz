import random

def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                break
            else:
                print("Invalid choice. Please enter a number corresponding to an option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if options[choice - 1] == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong answer. The correct answer was: {correct_answer}.")
        return False

# Main function
def main():
    # Define valid credentials
    valid_username = "user"
    valid_password = "password"

    # Prompt for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the entered credentials are correct
    if username == valid_username and password == valid_password:
        print("Login successful! Welcome to the KBC Quiz!")
        
        questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
                "answer": "Paris"
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["Oxygen", "Gold", "Silver", "Iron"],
                "answer": "Oxygen"
            },
            {
                "question": "Who wrote 'Pride and Prejudice'?",
                "options": ["Jane Austen", "Charles Dickens", "Emily Brontë", "Mary Shelley"],
                "answer": "Jane Austen"
            },
            {
                "question": "What is the hardest natural substance on Earth?",
                "options": ["Gold", "Diamond", "Iron", "Platinum"],
                "answer": "Diamond"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "Who won the FIFA World Cup in 2022?",
                "options": ["France", "Argentina", "Brazil", "Germany"],
                "answer": "Argentina"
            },
            {
                "question": "What does HTTP stand for?",
                "options": ["HyperText Transfer Protocol", "HighText Transfer Protocol", "HyperText Transmission Protocol", "HighText Transmission Protocol"],
                "answer": "HyperText Transfer Protocol"
            },
            {
                "question": "Which movie won the Oscar for Best Picture in 2023?",
                "options": ["Everything Everywhere All at Once", "Top Gun: Maverick", "The Fabelmans", "Elvis"],
                "answer": "Everything Everywhere All at Once"
            },
            {
                "question": "Who developed the theory of relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Galileo Galilei"],
                "answer": "Albert Einstein"
            },
            {
                "question": "In which year did the Titanic sink?",
                "options": ["1905", "1912", "1915", "1920"],
                "answer": "1912"
            },
            {
                "question": "What is the main ingredient in guacamole?",
                "options": ["Tomato", "Avocado", "Onion", "Pepper"],
                "answer": "Avocado"
            },
            {
                "question": "Which programming language is known as the 'mother of all languages'?",
                "options": ["Python", "Java", "C", "Fortran"],
                "answer": "C"
            },
            {
                "question": "What is the longest river in the world?",
                "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
                "answer": "Amazon"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
                "answer": "Leonardo da Vinci"
            },
            {
                "question": "What is the powerhouse of the cell?",
                "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"],
                "answer": "Mitochondria"
            },
            {
                "question": "Which company developed the iPhone?",
                "options": ["Microsoft", "Samsung", "Apple", "Google"],
                "answer": "Apple"
            },
            {
                "question": "Who is known as the 'King of Pop'?",
                "options": ["Elvis Presley", "Michael Jackson", "Prince", "David Bowie"],
                "answer": "Michael Jackson"
            },
            {
                "question": "What is the smallest planet in our solar system?",
                "options": ["Mercury", "Venus", "Mars", "Pluto"],
                "answer": "Mercury"
            },
            {
                "question": "Who wrote 'The Catcher in the Rye'?",
                "options": ["J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck"],
                "answer": "J.D. Salinger"
            },
            {
                "question": "What is the currency of Japan?",
                "options": ["Yuan", "Won", "Dollar", "Yen"],
                "answer": "Yen"
            }
        ]

        random.shuffle(questions)  # Shuffle questions to randomize the order
        score = 0

        print("Answer the following questions:\n")
        
        for q in questions:
            if ask_question(q["question"], q["options"], q["answer"]):
                score += 1
            print()

        print(f"Quiz over! Your score: {score}/{len(questions)}")
    else:
        print("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()
