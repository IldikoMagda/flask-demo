from application import app, db
from flask import request,jsonify
from application.models import FriendsCharacters

def format_character(character):
    return {
        'name': character.name,
        'age' : character.age,
        'catch_phrase': character.catch_phrase
    }


@app.route('/')
def hello_world():
    return '<p>Hello World!</p>'

@app.route('/characters', methods=['POST'])
def create_character():
    data = request.json
    character = FriendsCharacters(data['name'], data['age'], data['catch_phrase'])
    db.session.add(character)
    db.session.commit()
    return jsonify(id= character.id, name=character.name, age= character.age, catch_phrase=character.catch_phrase)

@app.route('/characters', methods=['GET'])
def get_characters():
    characters = FriendsCharacters.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return {'characters': character_list}


@app.route('/characters/<id>', methods=['GET'])
def get_character(id):
    character = FriendsCharacters.query.filter_by(id=id).first()
    return jsonify(id= character.id, name= character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route('/characters/<id>', methods=['DELETE'])
def delete_character(id):
    character = FriendsCharacters.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return 'Character Deleted'

@app.route('/characters/<id>', methods =['PATCH'])
def update_character(id):
    character = FriendsCharacters.query.filter_by(id=id)
    data = request.json
    character.update(dict(name=data['name'], age=data['age'], catch_phrase=data['catch_phrase']))
    db.session.commit()
    updated_character = character.first()
    return jsonify(id= updated_character.id, name= updated_character.name, age=updated_character.age, catch_phrase=updated_character.catch_phrase)



