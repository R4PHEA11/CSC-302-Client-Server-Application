import requests

server_url = "http://127.0.0.1:5000/player"  # Update this if running on a different machine

player_name = input("Enter basketball player name: ")
response = requests.get(server_url, params={"name": player_name})

if response.status_code == 200:
    data = response.json()
    print(f"{data['player']} - Points: {data['stats']['points']}, Rebounds: {data['stats']['rebounds']}, Assists: {data['stats']['assists']}")
else:
    print("Error:", response.json().get("error", "Unknown error"))
