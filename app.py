import os
import logging
from flask import Flask, render_template, request, jsonify, session
from nova_ai import AdvancedNovaAI
import threading
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "nova-ai-secret-key-fallback")

# Global AI instance
nova_ai = None
ai_thread = None

def initialize_ai():
    """Initialize the AI system"""
    global nova_ai
    try:
        groq_key = os.getenv("GROQ_API_KEY", "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")
        nova_ai = AdvancedNovaAI(groq_key=groq_key)
        app.logger.info("✅ Nova AI initialized successfully")
        return True
    except Exception as e:
        app.logger.error(f"❌ Failed to initialize Nova AI: {e}")
        return False

def start_ai_systems():
    """Start AI autonomous systems in background"""
    global ai_thread
    if nova_ai and not ai_thread:
        ai_thread = threading.Thread(target=nova_ai.start_autonomous_systems, daemon=True)
        ai_thread.start()
        app.logger.info("🌟 AI autonomous systems started")

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/chat')
def chat():
    """Chat interface"""
    return render_template('chat.html')

@app.route('/api/status')
def api_status():
    """Get AI system status"""
    if not nova_ai:
        return jsonify({
            'status': 'error',
            'message': 'AI system not initialized'
        }), 500
    
    try:
        status = {
            'status': 'active' if nova_ai.running else 'inactive',
            'autonomous_level': nova_ai.autonomous_level,
            'consciousness_level': nova_ai.consciousness_level,
            'creativity_index': nova_ai.creativity_index,
            'current_mood': nova_ai.current_mood,
            'memory_stats': {
                'episodic': len(nova_ai.episodic_memory),
                'semantic': len(nova_ai.semantic_memory),
                'thought_chains': len(nova_ai.thought_chains)
            },
            'curiosity_level': nova_ai.curiosity_level
        }
        return jsonify(status)
    except Exception as e:
        app.logger.error(f"Error getting status: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def api_chat():
    """Chat with Nova AI"""
    if not nova_ai:
        return jsonify({
            'status': 'error',
            'message': 'AI system not initialized'
        }), 500
    
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'status': 'error',
                'message': 'Message cannot be empty'
            }), 400
        
        # Get AI response
        response = nova_ai.process_user_interaction(user_message)
        
        if response:
            return jsonify({
                'status': 'success',
                'response': response,
                'mood': nova_ai.current_mood
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Failed to get AI response'
            }), 500
            
    except Exception as e:
        app.logger.error(f"Chat error: {e}")
        return jsonify({
            'status': 'error',
            'message': f'Chat error: {str(e)}'
        }), 500

@app.route('/api/memories')
def api_memories():
    """Get recent memories and thoughts"""
    if not nova_ai:
        return jsonify({
            'status': 'error',
            'message': 'AI system not initialized'
        }), 500
    
    try:
        recent_thoughts = nova_ai.thought_chains[-5:] if nova_ai.thought_chains else []
        recent_memories = nova_ai.episodic_memory[-10:] if nova_ai.episodic_memory else []
        
        return jsonify({
            'status': 'success',
            'recent_thoughts': recent_thoughts,
            'recent_memories': recent_memories,
            'semantic_memory_keys': list(nova_ai.semantic_memory.keys())[:10]
        })
    except Exception as e:
        app.logger.error(f"Memory retrieval error: {e}")
        return jsonify({
            'status': 'error',
            'message': f'Memory error: {str(e)}'
        }), 500

@app.route('/api/control', methods=['POST'])
def api_control():
    """Control AI system"""
    if not nova_ai:
        return jsonify({
            'status': 'error',
            'message': 'AI system not initialized'
        }), 500
    
    try:
        data = request.get_json()
        action = data.get('action')
        
        if action == 'pause':
            nova_ai.running = False
            return jsonify({'status': 'success', 'message': 'AI systems paused'})
        elif action == 'resume':
            nova_ai.running = True
            return jsonify({'status': 'success', 'message': 'AI systems resumed'})
        elif action == 'adjust_autonomy':
            level = int(data.get('level', 3))
            nova_ai.autonomous_level = max(1, min(5, level))
            return jsonify({'status': 'success', 'message': f'Autonomy level set to {level}'})
        else:
            return jsonify({'status': 'error', 'message': 'Unknown action'}), 400
            
    except Exception as e:
        app.logger.error(f"Control error: {e}")
        return jsonify({
            'status': 'error',
            'message': f'Control error: {str(e)}'
        }), 500

if __name__ == '__main__':
    # Initialize AI system
    if initialize_ai():
        start_ai_systems()
    
    # Start Flask app
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
