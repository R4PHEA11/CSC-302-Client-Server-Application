from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample basketball player stats database
player_stats = {
    "LeBron James": {"points": 27.2, "rebounds": 7.5, "assists": 7.3},
    "Stephen Curry": {"points": 24.3, "rebounds": 4.6, "assists": 6.5},
    "Kevin Durant": {"points": 27.0, "rebounds": 7.1, "assists": 4.3},
}

@app.route('/player', methods=['GET'])
def get_player_stats():
    player_name = request.args.get('name')
    if not player_name:
        return jsonify({"error": "Please provide a player name."}), 400
    
    stats = player_stats.get(player_name)
    if stats:
        return jsonify({"player": player_name, "stats": stats})
    else:
        return jsonify({"error": "Player not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
