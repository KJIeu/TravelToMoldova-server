from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the survey questions
questions = [
    {
        "id": 1,
        "question": "What is your age?",
        "answers": [
            {
                "id": 1,
                "answer": "Under 18",
                "image": "https://example.com/answer1.png"
            },
            {
                "id": 2,
                "answer": "18-24",
                "image": "https://example.com/answer2.png"
            },
            {
                "id": 3,
                "answer": "25-34",
                "image": "https://example.com/answer3.png"
            }
        ]
    },
    {
        "id": 2,
        "question": "What is your favorite color?",
        "answers": [
            {
                "id": 1,
                "answer": "Red",
                "image": "https://example.com/answer1.png"
            },
            {
                "id": 2,
                "answer": "Blue",
                "image": "https://example.com/answer2.png"
            },
            {
                "id": 3,
                "answer": "Green",
                "image": "https://example.com/answer3.png"
            }
        ]
    }
]

# Define the endpoint for retrieving the survey questions
@app.route('/survey', methods=['GET'])
def get_survey():
    return jsonify({'questions': questions})

# Define the endpoint for submitting survey responses
@app.route('/survey', methods=['POST'])
def submit_survey():
    data = request.get_json()
    # Parse the survey responses and do further analysis here
    # ...

    return jsonify({'message': 'Survey submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
