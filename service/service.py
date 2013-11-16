from flask import Blueprint, jsonify, request, json, request
from config.configuration import Config
from data.note import NoteDao

note_service = Blueprint('note_service', __name__)
note_dao = NoteDao(Config())


@note_service.route('/get_notes')
def get_notes():
    start_id = request.values.get('start_id', '-1')
    if int(start_id) == -1:
        start_id = None
    try:
        tmp = jsonify(results=note_dao.get_notes(start_id))
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
