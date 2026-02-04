print("==== Welcome To Quiz Game ====")
questions = [
    {
        "question" : "which of the following is used to define a function in Python?",
        "options" : ["1. Function", "2. Def", "3. Define", "4. Func"],
        "answer" : "2" 
    },
    {
        "question" : "What will be the output of this code?\n x = [1, 2, 3]\n print(len(x))",
        "options" : ["1. 2", "2. 3", "3. 4", "4. Error"],
        "answer" : "3"
    },
    {
        "question" : "What will be the output of this code?\n x = \"python\"\n print(x[0])",
        "options" : ["1. P", "2. y", "3. n", "4. x"],
        "answer" : "1"
    }
]
while True:
    print("1. Start The Quiz")
    print("2. Exit")
    choose_option = int(input("Choose An Option: "))
    if choose_option == 2:
        print("Exiting...")
        print("Goodbye")
        break
    elif choose_option == 1:
        score = 0
        for q in questions:
            print(q["question"])
            for option in q["options"]:
                print(option)
            ans_choose = input("Enter Your Option: ")
            if ans_choose == q["answer"]:
                print("Correct Answer!")
                score +=1
            elif ans_choose != q["answer"]:  
                correct_answer = q["answer"]                
                print(f"Wrong Answer! Correct Option is {correct_answer}")
            else :
                print("Error Choose The Correct Option")
        print("Game Over!")
        print(f"Your Total Score: {score} / {len(questions)}")    
    else:
        print("Error Try Again")

