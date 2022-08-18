from flask import Flask, render_template, request, redirect

app = Flask(__name__)
taskList = []


class Tasks:
    number = 0

    def __init__(self, content):
        self.content = content
        self.id = Tasks.number
        Tasks.number += 1

    def __repr__(self):
        return self.content


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('home_page.html', tasks=taskList)


@app.route('/add/', methods=['POST', 'GET'])
def addTask():
    if request.method == 'POST':
        content = request.form['content']
        taskList.append(Tasks(content))
        return redirect('/')
    else:
        return render_template('add_task.html')


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def updateTask(id):
    if request.method == 'POST':
        content = request.form['content']

        for task in taskList:
            if task.id == id:
                task.content = content
                break

        return redirect('/')
    else:
        for task in taskList:
            if task.id == id:
                content = task.content
                break

        return render_template('update_task.html', content=content)


@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def deleteTask(id):
    for task in taskList:
        if task.id == id:
            taskList.remove(task)
            break

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
