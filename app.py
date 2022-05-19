#import flask
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

#Animals in the PetShop
Animals = [
    {'id': 0,
     'name': 'Jerry',
     'type': 'I am a Cat',
     'eat' : 'Mice',
     'price': 100,
     'age': 20},
    {'id': 1,
     'name': 'Batty',
     'type': 'I am a Bat',
     'eat' : 'Insects',
     'price': 69,
     'age': 69},
     {'id': 2,
     'name': 'Doggy',
     'type': 'I am a Dog',
     'eat' : 'Cats',
     'price': 101,
     'age': 101.5},
     {'id':3,
     'name': 'Pengu',
     'type': 'I am a Penguin',
     'eat' : 'Fish',
     'price': 404,
     'age': 3},
     {'id':4,
     'name': 'Pigi',
     'type': 'I am a Pigeon',
     'eat' : 'Crumbs',
     'price': 2,
     'age': 39},
     {'id':5,
     'name': 'Goldi',
     'type': 'I am a GoldFish',
     'eat' : 'Plants',
     'price': 5,
     'age': 10},
     {'id':6,
     'name': 'Hammy',
     'type': 'I am a Hamster',
     'eat' : 'Fruits',
     'price': 30,
     'age': 1}
]

@app.route('/', methods=['GET'])
def home():
    return ("<h1>Welcome to the Animal Shop!</h1> <p>Browse our <a href='/api/stock'>stock</a></p> <p>Our most expensive <a href='/api?id=3'>Animal!</a></p> <p>Our cheapest <a href='/api/somearea?price=2'>Animal</a> for you peasants</p>")

@app.route('/api/stock', methods=['GET'])
def api_all():
    return jsonify(Animals)

#loop to find the cheapest/most expensive 

@app.route('/api', methods=['GET'])
def get_pet_by_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error"

    results = []

    for Animal in Animals:
        if Animal['id'] == id:
            results.append(Animal)

    return jsonify(results)


@app.route('/api/somearea', methods=['GET'])
def get_pet_by_price():

    if 'price' in request.args:
        price = int(request.args['price'])
    else:
        return "Error"

    resultsPrice = []

    for Animal1 in Animals:
        if Animal1['price'] == price:
            resultsPrice.append(Animal1)

    return jsonify(resultsPrice)



if __name__ == '__main__': 
    app.run() 








