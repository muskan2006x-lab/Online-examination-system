def questions():
    return [{"question": "Q1, which keyword is used to define a function in python?",
             "options": ["a) func", "b)def", "c)function", "d)define"],
             "answer": "b"},
            {"question": "Q2, which data type is used to store key-value in python?",
             "options": ["a)list", "b)tuple", "c)dictionary", "d)set"],
             "answer": "c"},
            {"question": "Q3, what is the output of 2**3 in python?",
             "options": ["a)6", "b)8", "c)9", "d)5"],
             "answer": "b"},
            {"question": "Q4, which method adds an elementto the end of a list?",
             "options": ["a)add()", "b)appand()", "c)insert()", "d)push()"],
             "answer": "b"},
            {"question": "Q5, how do you start a single-line comment in python?",
             "options": ["a)//", "b)#", "c)/*", "d)--"],
             "answer": "b"}]
def exam(question):
    user_answer=[]
    valid_choices={'a', 'b', 'c', 'd', 's'}
    print("ONLINE EXAMINATION")
    print("Instructions: Enter a, b, c, or d to answer, or 's' to skip.\n")
    for index, item in enumerate(question, start=1):
        print(item["question"])
        for opt in item["options"]:
            print(f" {opt}")

        while True:
            choice=input(f"Enter answer for Q{index}: ").strip().lower()
            if choice in valid_choices:
                user_answer.append(choice)
                print(f"Answer recorded for Q{index} {choice}\n")
                break
            else:
                print("Invalid option, Enter a, b, c, d or s to skip.")
    return user_answer
def evaluate_exam(question, user_answer):
    correct=0
    wrong=0
    skipped=0
    marks_per_question=2

    for item, ans in zip(question, user_answer):
        if ans=='s':
            skipped+=1
        elif ans==item["answer"]:
            correct+=1
        else:
            wrong+=1

    total_marks=len(question)*marks_per_question
    score=correct*marks_per_question
    percentage=(score/total_marks)*100
    result="Pass" if percentage >= 40.0 else "Fail"

    return {
        "correct": correct,
        "wrong": wrong,
        "skipped": skipped,
        "score": score,
        "total_marks": total_marks,
        "percentage": percentage,
        "result": result
    }
def display_summary(summary):
    print("=========================")
    print("       RESULT  SUMMARY      ")
    print("=========================")
    print(f"Correct: {summary['correct']} | Wrong: {summary['wrong']} | Skipped: {summary['skipped']}")
    print(f"Score: {summary['score']}/{summary['total_marks']} | Percentage: {summary['percentage']:.2f}% | Result: {summary['result']}")
    print("=========================")

def main():
    question=questions()
    user_answer=exam(question)
    summary=evaluate_exam(question, user_answer)
    display_summary(summary)

if __name__ == "__main__":
    main()
