from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from app import db

class ThoughtChain(db.Model):
    """AI thought chains for deep thinking processes"""
    __tablename__ = 'thought_chains'
    
    id = Column(Integer, primary_key=True)
    topic = Column(String(255), nullable=False)
    initial_thought = Column(Text)
    deep_analysis = Column(Text)
    conclusion = Column(Text)
    mood_data = Column(JSON)
    significance = Column(Float, default=0.5)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'topic': self.topic,
            'initial': self.initial_thought,
            'deep_analysis': self.deep_analysis,
            'conclusion': self.conclusion,
            'mood': self.mood_data,
            'significance': self.significance,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

class EpisodicMemory(db.Model):
    """AI episodic memories for experiences"""
    __tablename__ = 'episodic_memories'
    
    id = Column(Integer, primary_key=True)
    memory_type = Column(String(100), nullable=False)
    content = Column(JSON)
    significance = Column(Float, default=0.5)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.memory_type,
            'content': self.content,
            'significance': self.significance,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

class SemanticMemory(db.Model):
    """AI semantic memories for knowledge"""
    __tablename__ = 'semantic_memories'
    
    id = Column(Integer, primary_key=True)
    memory_key = Column(String(255), unique=True, nullable=False)
    topic = Column(String(255))
    content = Column(JSON)
    insights = Column(JSON)
    related_thoughts = Column(Integer, default=0)
    last_updated = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'key': self.memory_key,
            'topic': self.topic,
            'content': self.content,
            'insights': self.insights,
            'related_thoughts': self.related_thoughts,
            'last_updated': self.last_updated.isoformat() if self.last_updated else None
        }

class ChatHistory(db.Model):
    """Chat interactions with users"""
    __tablename__ = 'chat_history'
    
    id = Column(Integer, primary_key=True)
    user_message = Column(Text, nullable=False)
    ai_response = Column(Text)
    ai_mood = Column(JSON)
    session_id = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_message': self.user_message,
            'ai_response': self.ai_response,
            'ai_mood': self.ai_mood,
            'session_id': self.session_id,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

class GeneratedCode(db.Model):
    """AI generated code projects"""
    __tablename__ = 'generated_code'
    
    id = Column(Integer, primary_key=True)
    project_name = Column(String(255), nullable=False)
    description = Column(Text)
    code_content = Column(Text)
    language = Column(String(50), default='python')
    execution_result = Column(Text)
    autonomous_level = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'project_name': self.project_name,
            'description': self.description,
            'code_content': self.code_content,
            'language': self.language,
            'execution_result': self.execution_result,
            'autonomous_level': self.autonomous_level,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

class SystemMetrics(db.Model):
    """AI system performance metrics"""
    __tablename__ = 'system_metrics'
    
    id = Column(Integer, primary_key=True)
    consciousness_level = Column(Float)
    creativity_index = Column(Float)
    curiosity_level = Column(Float)
    autonomous_level = Column(Integer)
    current_mood = Column(JSON)
    memory_count_episodic = Column(Integer, default=0)
    memory_count_semantic = Column(Integer, default=0)
    thought_chain_count = Column(Integer, default=0)
    is_running = Column(Boolean, default=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'consciousness_level': self.consciousness_level,
            'creativity_index': self.creativity_index,
            'curiosity_level': self.curiosity_level,
            'autonomous_level': self.autonomous_level,
            'current_mood': self.current_mood,
            'memory_stats': {
                'episodic': self.memory_count_episodic,
                'semantic': self.memory_count_semantic,
                'thought_chains': self.thought_chain_count
            },
            'is_running': self.is_running,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }