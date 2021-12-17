from tkinter import *
from Question_Handling import *

score = 0
highscore = 0

class Game:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quiz Game')
        self.window.config(bg='#FED2AA', padx=50, pady=50)

        self.Score_Label = Label(text=f'Score: {score}', fg='black', bg='#FED2AA', font=('Arial', 20, 'bold'))
        self.Score_Label.grid(row=0, column=1)

        self.High_Score_Label = Label(text=f'High Score: {highscore}', fg='black', bg='#FED2AA', font=('Arial', 20, 'bold'))
        self.High_Score_Label.grid(row=0, column=0)

        self.canvas = Canvas(master=self.window, height=500, width=500, bg='#84DFFF', bd=0)
        self.Question = self.canvas.create_text(250, 250,
                                                justify='center',
                                                width='400',
                                                text="Question Samples",
                                                fill='black',
                                                font=('Arial', 20, 'italic')
                                                )
        self.canvas.grid(row=1, column=0, columnspan=2)

        tick_image = PhotoImage(file='tick.png')
        cross_image = PhotoImage(file='cross.png')

        self.tick_Button = Button(image=tick_image, command=self.tick, highlightthickness=0)
        self.tick_Button.grid(row=2, column=0, pady=20)

        self.cross_Button = Button(image=cross_image, command=self.cross, highlightthickness=0)
        self.cross_Button.grid(row=2, column=1, pady=20)

        self.canvas.itemconfig(self.Question, text=next_question())
        self.high_score()

        self.window.mainloop()

    def tick(self):
        global score
        if input_answer(True):
            score += 1
        self.update_score()

    def cross(self):
        global score
        if input_answer(False):
            score += 1
        self.update_score()


    def update_score(self):
        global highscore
        self.Score_Label.config(text=f"Score: {score}")
        if score > highscore:
            highscore = score
        self.High_Score_Label.config(text=f'High Score: {highscore}')
        self.update_details()

    def update_details(self):
        if check_more_questions_left():
            self.canvas.itemconfig(self.Question, text=next_question())
        else:
            self.tick_Button.config(state='disabled')
            self.cross_Button.config(state='disabled')
            with open('highscore.txt', 'w') as file:
                file.write(str(highscore))
            self.canvas.itemconfig(self.Question, text='Game Over!!!!!')

    def high_score(self):
        global highscore
        with open('highscore.txt', 'r') as file:
            data123 = int(file.readline())
        highscore = data123
        self.High_Score_Label.config(text=f'High Score: {data123}')