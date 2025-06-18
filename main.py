from app import app, initialize_ai, start_ai_systems

# Initialize AI system when module is imported
initialize_ai()
start_ai_systems()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
