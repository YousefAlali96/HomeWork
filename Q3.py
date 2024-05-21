import csv

def load_questions_from_csv(file_name):
    questions = []
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            question = {
                "question": row[0],
                "options": row[1:5],
                "answer": row[5]
            }
            questions.append(question)
    return questions

def quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for j, option in enumerate(q['options'], 1):
            print(f"{j}. {option}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == q['answer'].lower():
            score += 1
    return score

def main():
    file_name = 'questions.csv'
    questions = load_questions_from_csv(file_name)
    user_name = input("Enter your name: ")
    user_score = quiz(questions)
    print(f"Dear {user_name}, your score is {user_score} out of {len(questions)}")
    
    with open('user_scores.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([user_name, user_score])

if __name__ == "__main__":
    main()