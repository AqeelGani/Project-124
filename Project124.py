from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
    'id' : 1,
    'name' : 'abc',
    'contact' : '1234567890',
    'done' : False
    },
    {
    'id' : 2,
    'name' : 'xyz',
    'contact' : '0987654321',
    'done' : False
    },
]

@app.route('/get-data')
def getTask():
    return jsonify({
        'data' : contacts
    })

@app.route('/add-data', methods = ['POST'])
def addTask():
    if not request.json:
        return jsonify({
            'status' : 'Error',
            'message' : 'Please Provise The Data'
        }, 400)
    
    contact = {
    'id' : contacts[-1]['id'] + 1,
    'name' : request.json['title'],
    'contact' : request.json.get('description', ''),
    'done' : False
    }

    contacts.append(contact)

    return jsonify({
            'status' : 'Success',
            'message' : 'Task Added Successfully'
        }, 100)

if __name__ == '__main__':
    app.run(debug = True)