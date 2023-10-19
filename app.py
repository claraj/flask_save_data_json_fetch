from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route('/')
def home_page():
    example_number = 3
    example_string = 'python'
    example_list = ['snow', 'rain', 'fog']
    data = { 'number': example_number, 'string': example_string, 'list': example_list}
    return render_template('index.html', data=data)


@app.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()
    print(data)
    # # TODO save to db
    return 'saved'  
    # you should not render_template here, return an OK message or an error code 
    # since the response will be handled by the script in the browser  


