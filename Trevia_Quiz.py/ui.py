from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Quizler:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title(string="Quizleer")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # score label
        self.score_label = Label(text="Score: 0", fg='white', bg= THEME_COLOR, font=("Arial", 10, "bold"))
        self.score_label.grid(row= 0, column= 1)

        # canvas
        self.canvas = Canvas(width= 300, height=300, bg= "white")
        self.ques_text = self.canvas.create_text(150,
                                                 125,
                                                 width= 270,
                                                 text="Some text as placeholder",
                                                 font=("Arial", 15, "italic"))
        self.canvas.grid(row =1, column=0, columnspan =2, pady = 50)

        # true and false button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image= true_image, highlightthickness=0, command= self.true_pressed)
        self.true_button.grid(row =2, column = 0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command= self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # calling get_next_question to directly enter the question instead of any dummy text
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            self.canvas.itemconfigure(self.ques_text, text = q_text)

        else:
            self.canvas.itemconfigure(self.ques_text, text= "You have reached the end of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        self.canvas.config(bg="white")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)



    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if(is_right):
            # flash green
            self.canvas.config(bg ='green')

        else:
            #flash red
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)



