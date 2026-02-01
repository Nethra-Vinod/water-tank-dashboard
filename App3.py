from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# Store tank data
tank_data = {
    "level": 50,  # Numeric for visualization
    "status": "UNKNOWN",
    "last_update": "Never"
}

# Mapping from ESP32 status to numeric percentage for visualization
STATUS_TO_PERCENTAGE = {
    "LOW WATER": 10,   # Show 10% when EMPTY (so you can see some water)
    "WATER OK": 95     # Show 95% when FULL
}

# DASHBOARD
@app.route("/", methods=["GET"])
def dashboard():
    return render_template("index.html")

# ESP32 POSTS DATA HERE
@app.route("/update", methods=["POST"])
def update():
    global tank_data

    try:
        data = request.get_json(force=True)
        print(f"[ESP32] Received data: {data}")
        
        if "level" in data:
            esp_status = data["level"]  # "LOW WATER" or "WATER OK"
            
            # Update tank data
            tank_data["status"] = esp_status
            tank_data["level"] = STATUS_TO_PERCENTAGE.get(esp_status, 50)
            tank_data["last_update"] = datetime.now().strftime("%H:%M:%S")
            
            print(f"[ESP32] Status: {esp_status} -> Level: {tank_data['level']}%")
            return jsonify({"status": "ok"}), 200
        else:
            return jsonify({"error": "Missing 'level' field"}), 400
            
    except Exception as e:
        print(f"[ERROR] Failed to parse data: {e}")
        return jsonify({"error": str(e)}), 400

# DASHBOARD FETCHES DATA HERE
@app.route("/level", methods=["GET"])
def level():
    return jsonify({
        "level": tank_data["level"],
        "last_update": tank_data["last_update"]
    })

if __name__ == "__main__":
    print("Starting AquaVision Tank Tracker Server...")
    print("Dashboard: http://localhost:5000")
    print("ESP32 Mapping: LOW WATER -> 10% (EMPTY), WATER OK -> 95% (FULL)")
    
    app.run(host="0.0.0.0", port=5000, debug=True)


