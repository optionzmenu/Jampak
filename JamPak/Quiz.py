def quizgame():
     class Question:
          def __init__(self, prompt, answer):
               self.prompt = prompt
               self.answer = answer

     print("Welcome to the Marvel Quiz Game!")

     questionlist = [
          "What does Groot always say??\n (a)He is Groot\n (b)They are Groot \n (c)I am Groot\n",
          "How many Infinity Stones are there?\n (a)Three\n (b)Six \n (c)Eight\n",
          "Sharon Carter is whose great-niece?\n (a)Peggy Carter\n (b)Maegan Carter \n (c)Briana Carter\n",
          "What type of doctor is Doctor Strange?\n (a)Plastic Surgeon\n (b)Endodontics \n (c)Neurosurgeon\n",
          "Vibranium comes from where?\n (a)America \n (b)Latveria  \n (c)Wakanda\n",
          "What is Tony Stark's daughter's name?\n (a)Taylor \n (b)Morgan \n (c)Jessica\n",
          "Where is Thor from?\n (a)Earth\n (b)Asgard\n (c)Hades\n",
          "Thor's Mjolnir is made from the metal of a dying ___? \n (a)Star\n (b)Universe \n (c)Planet\n",
          "Who is Bruce Banner's cousin?\n (a)Amanda\n (b)Jennifer \n (c)Monica\n",
          "Who is Star Lord's Father?\n (a)Tom\n (b)Ego \n (c)Bob\n",
     ]

     questions = [
          Question(questionlist[0], "c"),
          Question(questionlist[1], "b"),
          Question(questionlist[2], "a"),
          Question(questionlist[3], "c"),
          Question(questionlist[4], "c"),
          Question(questionlist[5], "b"),
          Question(questionlist[6], "b"),
          Question(questionlist[7], "a"),
          Question(questionlist[8], "b"),
          Question(questionlist[9], "b"),
     ]

     score = 0
     for question in questions:
          answer = input(question.prompt).lower()
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions), "correct")