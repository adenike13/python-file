# CBT EXAMINATION
print("enter candidates name")
input()
print("enter 'START' to begin")
reply = input().upper()
def Question() :
    
    english = [
       {
          "question":"1. what did the author of the book study",
           "options":["B.Sc(Ed)Mathematics","B. B.A English langusge","C. B.A Literary studies", "D. BSc Political science"],
           "Answer":"A"
       },
       {
           "question":"2. the book described Talle as a?",
           "options":["A.the precious child","B.the quiet one","C.the friendly child","D.the holy child"],
           "Answer":"B"
       },
       {
           "question":"3. who was omar's immediate sister",
            "options":["A.ummi","B.omar","C.salma","D.teemah"],
            "answer":"D"
       },
       {
           "question":"4. ummi's husband wanted to study law but the providence chose that he study-----",
           "options":["A.commerce","B.accounting","C.law","D.history"],
            "answer":"B"
       },
       {
           "question":"5. the full meaning of IPO ------",
           "options":["A.independent police officer","B.international police officer","C.investigating police officer","D.investigative police officer"],
           "answer":"C"
       },
       {
           "question":"6. what is ummi's occupation",
           "options":["A.trader","B.teacher","C.bussiness woman","nurse"],
           "answer":"B"
       },
       {
           "Question":"7. what is ummi's matric number",
           "options":["A.UG0001","B.UG00001","C.UG001","D.UG0011"],
           "answer":"A"
       },
       {
           "question":"8. who was the narrator of the life changer",
           "options":["A.salma","B.ummi","C.omar","D.bint"],
           "answer":"B"
       },
       {
           "question":"9. how old is bint",
           "options":["A.6yrs","B.5yrs","C.7yrs","D.4yrs"],
           "answer":"C"
       },
       {
           "question":"10. how much did habib give tomiwa personally",
           "options":["A.10000","B.15000","C.20000","D.5000"],
           "answer":"C"
        },
    ]   
    for quest in english:
    
        print(quest["question"])
    for opt in quest["options"]:
        print(opt)    
    answer = input().upper()
    if answer == quest["answer"]:
        print("Wow you get it right")
        score = 0
        score = score + 1
    else:
        print("The answer is",quest["answer"])
        print(score)
    
biology = [
        {
            "question":"11. the organ responsible for the production of bile is--------",
            "options":["A.gall bladder","B.liver","C.hepacytes","D.planaria"],
            "answer":"B"
        },
        {
            "question":"12. which of the following is not regarded as pollutant on land and in air",
            "options":["A.smoke","B.nitrogen","C.noise","D.sulphur dioxide"],
            "answer":"B"
        },
        {
            "question":"13. which of the following is a direct photosynthesis",
            "options":["A.starch","B.glucose","C.protein","D.latex"],
            "answer":"B"
        },
        {
            "question":"14. aged erythrocytes are destroyed in the?",
            "options":["A.pancreas","B.lymph nodes","C.kidney","D.liver"],
            "answer":"B"
        },
        {
        "question":"15. the possession of chloroplast in euglena virids enables it to ?",
            "options":["A.store starch","B.carry out photosynthesis","C.reproduce","D.respond to light"],
            "answer":"B"
        },
        {
            "question":"16. agglutination is the------ of the -------",
            "options":["A.coagulation with white blood cells","B.coagulation with water","C.white and red blood cells","D.coagulation with red blood cells"],
            "answer":"D"
        },
        {
        "question":"17. the sensory cell that responds to dim light is referred to as the",
        "options":["A.cone","B.lens","C.rod","D.iris"],
        "answer":"C"
        },
        {
        "question":"18. the enzyme that is present in saliva",
        "options":["A.renin","B.lipase","C.pepsin","D.ptyalin"],
        "answer":"B"
        },
        {
        "question":"19. monocot stem differ from dicot stem and that monocot have",
        "options":["A.no cambium","B.no pith","C.fewer vascular bundles","D.phloems with parenchyma"],
        "answer":"A"
        },
        {
        "question":"20. the host of liver flake are --------?",
        "options":["A.pig and snail","B.pig and sheep","C.sheep and snail","D.pig"],
        "answer":"C"
        },
        {
        "question":"21. the activity of ptyalin is likely to decrease with an increase in the concentration of?",
        "options":["A.oxygen","B.starch","C.protein","D.acid"],
        "answer":"D"
        },
        {
        "question":"22. which of the following is most advanced in the evoluntary trend of animals",
        "options":["A.liverfluke","B.earthworm","C.snail","D.cockroach"],
            "answer":"D"
        },
        
    ]

for quest in biology:
    
    print(quest["question"])
    for opt in quest["options"]:
        print(opt)    
    answer = input().upper()
    if answer == quest["answer"]:
        print("Wow you get it right")
        score = 0
        score = score + 1
    else:
        print("The answer is",quest["answer"])
    print("score")
    print("do you want to continue yes/no")
    input()  
    if answer == "yes":
        print("continue")
    else:
        print("good day")
    