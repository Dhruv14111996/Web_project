from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

# If i need to run html file then i can run using this same method but for that we need to call render_templetes


@app.route('/')
def my_home():
    return render_template('index.html')

# By using string we can define all page route together we dont need to write for each and every html file.


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong please try again!'


# @app.route('/components.html')
# def components():
#     return render_template('components.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')
