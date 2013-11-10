from flask import Blueprint, jsonify, request, json
from config.configuration import Config
from data.note import NoteDao

note_service = Blueprint('note_service', __name__)
note_dao = NoteDao(Config())


@note_service.route('/allnotes')
def get_all_notes():
    try:
        tmp = jsonify(results=note_dao.get_all_notes())
    except Exception as e:
        print e
    return tmp


@note_service.route('/put', methods=['POST'])
def put_note():
    note_dao.put_note(json.loads(request.data))
    return '', 204



@note_service.route('/icon/<username>')
def get_icon(username):
    return username
