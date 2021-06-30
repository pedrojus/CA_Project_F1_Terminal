<<<<<<< HEAD
# F1 Trivia Terminal-Based Game
# Made by Pedro Jusino on 06/13/21

=======
>>>>>>> 6cdb8e24f958dd46e2ab5d55b44648f0333a74b1
class Question:
    def __init__(self, question, answerChoices, correctAnswer):
        self.question = question
        self.answerChoices = answerChoices
        self.correctAnswer = correctAnswer
        
class Category:
    def __init__(self, categoryName, questions, points):
        self.categoryName = categoryName
        self.points = points
        self.list = [None] * len(questions)
        
        for i in range(0, len(questions)):
            self.list[i] = questions[i]

Q1 = Question("In which country was the term 'Grand Prix' first used for a motor race", "a. France\nb. Germany\nc. Monaco\nd. United Kingdom", "a")
Q2 = Question("Brazillian driver Rubens Barrichello broke an F1 record at the 2008 Turkish Grand Prix. What was it?", "a. Most Race Starts from Pole\nb. Most DNFs\nc. Most Laps Led\nd. Most Race Starts", "d")
Q3 = Question("The first Formula 1 race took place in 1946 in Turin. Who was the winner of this race?", "a. Juan Manuel Fangio\nb. Achille Varzi\nc. Alberto Ascari\nd. Stirling Moss", "b")
Q4 = Question("Which racing team has the nickname 'The Pranching Horse'?", "a. Alfa-Romeo\nb. BAR\nc. Ferrari\nd. AlphaTauri", "c")
Q5 = Question("'The Iceman' is the nickname given to which Finnish Formula 1 World Champion?","a. Kimi Raikonnen\nb. Mika Hakkinen\nc. Valterri Bottas\nd. Keke Rosberg", "a")
Q6 = Question("Sahara Force India F1 Team was changed to what name in 2018?", "a. Giraffe Force India\nb. Scuderia Force India\nc. Racing Point Force India\nd. AMG Force India", "c")
Q7 = Question("What city is the United States Grand Prix hosted at?", "a. Miami\nb. New York\nc. Atlanta\nd. Austin", "d")
Q8 = Question("Which Grand Prix was heavily critizied due to its 'tire controversy?", "a. 2005 Indianapolis GP\nb. 2008 Singapore GP\nc. 1982 San Marino GP\nd. 1997 Jerez GP", "a")
Q9 = Question("Which track is home to one of the most thrilling turns known as 'Eau Rouge'?", "a. Red Bull Ring\nb. Spa-Francorchamps\nc. Hockenheim\nd. Imola", "b")
Q10 = Question("Which driver holds the record for most wins?", "a. Sir Lewis Hamilton\nb. Michael Schumacher\nc. Max Verstappen\nd. Sebastian Vettel", "a")
Q111 = Question("Who was the first F1 world champion?", "a. Juan Manuel Fangio\nb. Nino Farina\nc. Mike Hawthorn\nd. Alberto Ascari", "b")

teamTrivia = Category("Team Trivia", [Q4, Q5], 5)
driverTrivia = Category("Driver Trivia", [Q2, Q3, Q9], 10)
trackTrivia = Category("Track Trivia", [Q6, Q8], 20)
historyTrivia = Category("History Trivia", [Q1, Q7, Q10], 25)
