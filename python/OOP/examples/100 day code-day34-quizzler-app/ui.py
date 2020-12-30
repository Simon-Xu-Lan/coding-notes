from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=50, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text= self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)

        true_img = PhotoImage(file="images/true.gif")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.click_true_btn)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.gif")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.click_false_btn)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of questions")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")


    def click_true_btn(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_false_btn(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
