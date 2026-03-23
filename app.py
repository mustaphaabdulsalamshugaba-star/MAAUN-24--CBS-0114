from flask import Flask, render_template, request, redirect, url_for
from models import Question
from datetime import datetime

app = Flask(__name__, template_folder='assigment4/templates')

# Questions
questions = [
    Question("2 + 2 = ?", ["2", "3", "4", "5"], "4"),
    Question("Capital of Nigeria?", ["Abuja", "Lagos", "Kano"], "Abuja"),
    Question("Python is a?", ["Snake", "Programming Language", "Car"], "Programming Language")
]

current_index = 0
score = 0

# Stack for answers (Requirement)
answer_stack = []

@app.route('/')
def start():
    return render_template('start.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global current_index, score

    if request.method == 'POST':
        answer = request.form['answer']
        answer_stack.append(answer)  # STACK

        if questions[current_index].check_answer(answer):
            score += 1

        current_index += 1

    if current_index >= len(questions):
        return redirect(url_for('result'))

    return render_template('quiz.html', question=questions[current_index])


@app.route('/result')
def result():
    time_submitted = datetime.now()
    return render_template('result.html',
                           score=score,
                           total=len(questions),
                           time=time_submitted,
                           answers=answer_stack)


if __name__ == '__main__':
    app.run(debug=True)