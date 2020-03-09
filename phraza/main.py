from flask import Flask
from flask import render_template
from flask import request
import phrases

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    label = phrases.label()
    if request.method == 'POST':
        p = request.form['name']
        sentence = phrases.search(p)
        if sentence == 'Not found':
            return render_template('index.html', error=label[1], flag=True)
        return render_template('index.html', value="Мағынасы: " + sentence[0], example="Мысал: " + sentence[1],
                               sin=sentence[2], pol=sentence[3], flag=False)
    return render_template('index.html', sentence=label[0])



@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        idiom = request.form['idiom']
        value = request.form['value']
        example = request.form['example']
        sin = request.form['sin']
        pol = request.form['pol']
        sentence = phrases.create(idiom, value, example, sin, pol)
        return render_template('index.html', value="Мағынасы: " + sentence[0], example="Мысал: " + sentence[1],
                               sin=sentence[2], pol=sentence[3], flag=False)
    return render_template('create.html')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    idiom = phrases.show_last_idiom()
    sentence = phrases.search(idiom)
    if request.method == 'POST':
        idiom = request.form['idiom']
        value = request.form['value']
        example = request.form['example']
        sin = request.form['sin']
        pol = request.form['pol']
        sentence = phrases.edit(idiom, value, example, sin, pol)
        return render_template('index.html', value="Мағынасы: " + sentence[0], example="Мысал: " + sentence[1],
                               sin=sentence[2], pol=sentence[3], flag=False)
    return render_template('edit.html', idiom=idiom, value=sentence[0], example=sentence[1], sin=sentence[2], pol=sentence[3])


@app.route('/delete')
def delete():
    phrases.delete()
    return render_template('index.html', warning="Фразеологизм жойылды")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)