from flask import Flask, abort, request, render_template, redirect, url_for,session,flash
from flask_bootstrap import Bootstrap
from forms import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] ='hardToGuessString'
bootstrap = Bootstrap(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():

        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
@app.route('/hello/')
def hello(name=None):
    if name is None:
         name=request.args.get("name")
         if name:
            return render_template('user.html', name=name)
         else:
             abort(404)

if __name__== '__main__':
    app.run(debug=True)