from flask import Flask, jsonify, send_file, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Sample music library - UPDATE THESE TO MATCH YOUR MP3 FILES
MUSIC_LIBRARY = [
    {"id": 1, "title": "Summer Vibes", "artist": "Chill Wave", "file": "songs/song1.mp3"},
    {"id": 2, "title": "Relaxing Piano", "artist": "Classical Dreams", "file": "songs/song2.mp3"},
    {"id": 3, "title": "Upbeat Electronic", "artist": "Digital Pulse", "file": "songs/song3.mp3"}
]

@app.route('/')
def home():
    return send_from_directory('templates', 'index.html')

@app.route('/api/songs')
def get_songs():
    return jsonify(MUSIC_LIBRARY)

@app.route('/api/songs/<int:song_id>')
def get_song(song_id):
    song = next((s for s in MUSIC_LIBRARY if s['id'] == song_id), None)
    if song and os.path.exists(song['file']):
        return send_file(song['file'])
    return jsonify({"error": "Song not found"}), 404

@app.route('/api/gesture', methods=['POST'])
def handle_gesture():
    data = request.json
    gesture = data.get('gesture')
    print(f"Received gesture: {gesture}")  # For debugging
    return jsonify({"status": "success", "gesture": gesture})

if __name__ == '__main__':
    os.makedirs('songs', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    app.run(host='0.0.0.0', port=5001, debug=True)
