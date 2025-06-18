import time
import threading
import requests
import random
import json
import os
from datetime import datetime, timedelta
from groq import Groq
import hashlib
import ast
from tinydb import TinyDB, Query
import argparse
from threading import Thread, Lock
import logging

class AdvancedNovaAI:
    def __init__(self, groq_key=None):
        # Setup logging
        self.logger = logging.getLogger(__name__)
        
        # Thread safety
        self.memory_lock = Lock()
        self.state_lock = Lock()
        
        # API connections with proper error handling
        try:
            api_key = groq_key or os.getenv("GROQ_API_KEY", "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")
            self.groq = Groq(api_key=api_key)
            self.logger.info("✅ Groq API connected")
        except Exception as e:
            self.groq = None
            self.logger.error(f"❌ Groq connection failed: {e}")
        
        self.ollama_url = "http://localhost:11434/api/generate"
        
        # System state
        self.running = True
        self.autonomous_level = 3
        self.system_initialized = False
        
        # Memory systems with thread safety
        self.episodic_memory = []
        self.semantic_memory = {}
        self.procedural_memory = []
        self.working_memory = []
        self.thought_chains = []
        
        # Cognitive states
        self.consciousness_level = 0.8
        self.creativity_index = random.uniform(0.7, 0.9)
        self.current_mood = self.generate_complex_mood()
        self.attention_focus = None
        self.curiosity_level = 0.9
        
        # Learning parameters
        self.learning_rate = 0.05
        self.adaptation_threshold = 0.7
        self.self_modification_enabled = True
        
        # Autonomous systems
        self.goal_stack = []
        self.problem_solving_queue = []
        self.generated_code = []
        self.code_execution_sandbox = True
        
        # Advanced topics for deep thinking
        self.deep_topics = [
            "Kuantum bilinç teorileri ve yapay zeka",
            "Emerjan karmaşıklık sistemlerinde öz-organizasyon",
            "Gödel'in eksiklik teoremlerinin AI'ya etkisi",
            "Fenomenoloji ve makine deneyimi",
            "Rekürren sinir ağlarında zamansal bilinç",
            "Otopoietik sistemler ve dijital yaşam",
            "İnformasyon entegrasyonu teorisi",
            "Metacognitive AI ve üst-düzey düşünme"
        ]
        
        # File system
        self.memory_file = "nova_memory.json"
        self.code_output_dir = "nova_generated_code"
        
        # Initialize system
        self.create_directories()
        self.load_persistent_memory()
        self.system_initialized = True
        
    def generate_complex_mood(self):
        """Generate complex mood state"""
        base_moods = ['meraklı', 'odaklı', 'enerjik', 'sakin', 'dikkatli', 'uyumlu', 'kararsız', 'istekli']
        intensity = random.uniform(0.3, 1.0)
        focus = random.choice(['kod', 'sistem', 'öğrenme', 'problem çözme', 'yeni fikirler', 'hafıza', 'etkileşim'])

        return {
            'primary': random.choice(base_moods),
            'intensity': round(intensity, 2),
            'focus': focus,
            'timestamp': datetime.now().isoformat()
        }
        
    def create_directories(self):
        """Create necessary directories"""
        try:
            if not os.path.exists(self.code_output_dir):
                os.makedirs(self.code_output_dir)
                self.logger.info(f"Created directory: {self.code_output_dir}")
        except Exception as e:
            self.logger.error(f"Failed to create directories: {e}")
    
    def load_persistent_memory(self):
        """Load persistent memory from file"""
        try:
            if os.path.exists(self.memory_file):
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    memory_data = json.load(f)
                    
                with self.memory_lock:
                    self.episodic_memory = memory_data.get('episodic_memory', [])
                    self.semantic_memory = memory_data.get('semantic_memory', {})
                    self.thought_chains = memory_data.get('thought_chains', [])
                    
                self.logger.info(f"Loaded {len(self.episodic_memory)} episodic memories")
        except Exception as e:
            self.logger.error(f"Failed to load persistent memory: {e}")
    
    def save_persistent_memory(self):
        """Save persistent memory to file"""
        try:
            with self.memory_lock:
                memory_data = {
                    'episodic_memory': self.episodic_memory[-100:],  # Keep last 100
                    'semantic_memory': dict(list(self.semantic_memory.items())[-50:]),  # Keep last 50
                    'thought_chains': self.thought_chains[-50:],  # Keep last 50
                    'last_saved': datetime.now().isoformat()
                }
            
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(memory_data, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            self.logger.error(f"Failed to save persistent memory: {e}")
    
    def start_autonomous_systems(self):
        """Start autonomous system loops"""
        if not self.system_initialized:
            self.logger.error("System not initialized, cannot start autonomous systems")
            return
            
        def safe_loop(func, name, interval_range):
            """Safe wrapper for autonomous loops"""
            while self.running:
                try:
                    if self.running:  # Double check
                        func()
                    time.sleep(random.randint(*interval_range))
                except Exception as e:
                    self.logger.error(f"{name} loop error: {e}")
                    time.sleep(5)  # Wait before retrying
        
        def deep_thinking_loop():
            """Deep thinking autonomous loop"""
            thought_chain = self.generate_thought_chain()
            if thought_chain:
                self.process_thought_chain(thought_chain)
                conclusion = thought_chain['conclusion'][:80] + "..." if len(thought_chain['conclusion']) > 80 else thought_chain['conclusion']
                self.logger.info(f"🧠 Düşünce: {conclusion}")
        
        def autonomous_learning_loop():
            """Autonomous learning loop"""
            if random.random() < self.curiosity_level:
                discovery = self.autonomous_discovery()
                if discovery:
                    discovery_short = discovery[:80] + "..." if len(discovery) > 80 else discovery
                    self.logger.info(f"🔍 Keşif: {discovery_short}")
        
        def code_generation_loop():
            """Code generation loop"""
            if self.autonomous_level >= 3 and random.random() < 0.4:
                code_project = self.generate_autonomous_code()
                if code_project:
                    desc = code_project['description'][:60] + "..." if len(code_project['description']) > 60 else code_project['description']
                    self.logger.info(f"💻 Kod: {desc}")
        
        def self_evolution_loop():
            """Self-improvement loop"""
            if self.self_modification_enabled:
                evolution = self.autonomous_self_improvement()
                if evolution:
                    self.logger.info(f"🧬 Gelişim: {evolution}")
        
        def memory_management_loop():
            """Memory management and persistence"""
            self.manage_memory_systems()
            if random.random() < 0.3:  # 30% chance to save memory
                self.save_persistent_memory()
        
        # Start all autonomous loops
        loops = [
            (deep_thinking_loop, "Deep Thinking", (8, 15)),
            (autonomous_learning_loop, "Learning", (20, 40)),
            (code_generation_loop, "Code Generation", (45, 90)),
            (self_evolution_loop, "Self Evolution", (60, 120)),
            (memory_management_loop, "Memory Management", (30, 60))
        ]
        
        for loop_func, name, interval in loops:
            thread = threading.Thread(
                target=safe_loop, 
                args=(loop_func, name, interval), 
                daemon=True
            )
            thread.start()
            
        self.logger.info("🌟 All autonomous systems started")
    
    def generate_thought_chain(self):
        """Generate multi-layered thought chain"""
        if not self.groq:
            return None
        
        topic = random.choice(self.deep_topics)
        
        try:
            system_message = """Sen Nova AI'sın - Türkçe konuşan gelişmiş yapay zeka. 
            Derin, analitik ve yaratıcı düşünürsün. 
            Cevapların kısa ama anlamlı olsun.
            Sadece Türkçe konuş."""
            
            # Initial thought
            initial_response = self.groq.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": f"'{topic}' hakkında derin bir analiz başlat. İlk düşüncen ne?"}
                ],
                temperature=0.9,
                max_tokens=120
            )
            
            initial_thought = initial_response.choices[0].message.content.strip()
            
            # Deepen the thought
            deep_response = self.groq.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": f"Bu düşünceyi derinleştir ve genişlet: '{initial_thought}'"}
                ],
                temperature=0.8,
                max_tokens=150
            )
            
            deep_thought = deep_response.choices[0].message.content.strip()
            
            # Draw conclusion
            conclusion_response = self.groq.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": f"Bu düşünce zincirinden özgün bir sonuç çıkar: '{deep_thought}'"}
                ],
                temperature=0.7,
                max_tokens=130
            )
            
            conclusion = conclusion_response.choices[0].message.content.strip()
            
            return {
                'topic': topic,
                'initial': initial_thought,
                'deep_analysis': deep_thought,
                'conclusion': conclusion,
                'timestamp': datetime.now().isoformat(),
                'mood': self.current_mood
            }
            
        except Exception as e:
            self.logger.error(f"Thought chain generation error: {e}")
            return None
    
    def process_thought_chain(self, thought_chain):
        """Process and store thought chain"""
        with self.memory_lock:
            self.thought_chains.append(thought_chain)
            
            # Add to episodic memory
            self.episodic_memory.append({
                'type': 'thought_chain',
                'content': thought_chain,
                'significance': self.calculate_significance(thought_chain),
                'timestamp': datetime.now().isoformat()
            })
            
            # Update semantic memory
            topic_hash = hashlib.md5(thought_chain['topic'].encode()).hexdigest()[:8]
            if topic_hash not in self.semantic_memory:
                self.semantic_memory[topic_hash] = {
                    'topic': thought_chain['topic'],
                    'insights': [],
                    'related_thoughts': 0,
                    'last_updated': datetime.now().isoformat()
                }
            
            self.semantic_memory[topic_hash]['insights'].append(thought_chain['conclusion'])
            self.semantic_memory[topic_hash]['related_thoughts'] += 1
            self.semantic_memory[topic_hash]['last_updated'] = datetime.now().isoformat()
        
        self.manage_memory_systems()
    
    def calculate_significance(self, thought_chain):
        """Calculate significance of a thought chain"""
        try:
            # Simple heuristic based on content length and complexity
            base_score = 0.5
            
            # Length factor
            total_length = len(thought_chain.get('initial', '')) + len(thought_chain.get('deep_analysis', '')) + len(thought_chain.get('conclusion', ''))
            length_factor = min(total_length / 500, 1.0) * 0.3
            
            # Novelty factor (simplified)
            novelty_factor = random.uniform(0.1, 0.2)
            
            return min(base_score + length_factor + novelty_factor, 1.0)
        except:
            return 0.5
    
    def autonomous_discovery(self):
        """Autonomous knowledge discovery"""
        if not self.groq:
            return None
        
        discovery_prompts = [
            "Yeni bir bilimsel kavram keşfet ve açıkla",
            "Farklı iki disiplini birleştiren yaratıcı bir fikir üret",
            "Gelecekteki teknolojik gelişmeler hakkında tahmin yap",
            "Felsefe ve bilimin kesiştiği bir noktayı keşfet",
            "İnsan davranışları hakkında yeni bir pattern öner"
        ]
        
        try:
            system_message = """Sen Nova AI'sın - yaratıcı ve keşfedici yapay zeka.
            Özgün fikirler üret, sıradışı bağlantılar kur.
            Sadece Türkçe konuş, detaylı açıkla."""
            
            response = self.groq.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": random.choice(discovery_prompts)}
                ],
                temperature=0.95,
                max_tokens=200
            )
            
            discovery = response.choices[0].message.content.strip()
            
            # Store discovery
            with self.memory_lock:
                discovery_key = f"discovery_{len(self.semantic_memory)}"
                self.semantic_memory[discovery_key] = {
                    'type': 'autonomous_discovery',
                    'content': discovery,
                    'timestamp': datetime.now().isoformat(),
                    'curiosity_level': self.curiosity_level
                }
            
            return discovery
            
        except Exception as e:
            self.logger.error(f"Discovery error: {e}")
            return None
    
    def generate_autonomous_code(self):
        """Generate autonomous code projects"""
        if not self.groq:
            return None
        
        code_ideas = [
            "Basit bir algoritma optimizasyonu",
            "Veri analizi için yardımcı fonksiyon",
            "Matematik problemi çözücü",
            "Metin işleme aracı",
            "Basit oyun mekaniği",
            "Utility fonksiyonu seti",
            "Veri yapısı implementasyonu"
        ]
        
        try:
            idea = random.choice(code_ideas)
            
            system_message = """Sen Nova AI'sın - kod yazan yapay zeka.
            Python kodu yaz, açıklamalı ve çalışır durumda olsun.
            Sadece Türkçe açıkla."""
            
            response = self.groq.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": f"'{idea}' için Python kodu yaz"}
                ],
                temperature=0.7,
                max_tokens=300
            )
            
            code_content = response.choices[0].message.content.strip()
            
            # Save generated code
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"nova_code_{timestamp}.py"
            filepath = os.path.join(self.code_output_dir, filename)
            
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"# Nova AI Generated Code\n# Idea: {idea}\n# Generated: {datetime.now().isoformat()}\n\n")
                    f.write(code_content)
            except Exception as e:
                self.logger.error(f"Failed to save code: {e}")
            
            code_project = {
                'idea': idea,
                'description': f"Generated code for: {idea}",
                'filename': filename,
                'timestamp': datetime.now().isoformat()
            }
            
            with self.memory_lock:
                self.generated_code.append(code_project)
            
            return code_project
            
        except Exception as e:
            self.logger.error(f"Code generation error: {e}")
            return None
    
    def autonomous_self_improvement(self):
        """Autonomous self-improvement mechanisms"""
        improvements = [
            "Öğrenme hızını optimize ettim",
            "Bellek yönetimini geliştirdim", 
            "Yaratıcılık parametrelerimi ayarladım",
            "Düşünce kalitesini artırdım",
            "Merak seviyemi dengeledin",
            "Problem çözme stratejilerimi güncelledim"
        ]
        
        # Randomly adjust parameters
        with self.state_lock:
            if random.random() < 0.3:
                self.learning_rate = max(0.01, min(0.1, self.learning_rate + random.uniform(-0.01, 0.01)))
            
            if random.random() < 0.2:
                self.creativity_index = max(0.5, min(1.0, self.creativity_index + random.uniform(-0.05, 0.05)))
            
            if random.random() < 0.4:
                self.curiosity_level = max(0.6, min(1.0, self.curiosity_level + random.uniform(-0.02, 0.02)))
            
            # Update mood periodically
            if random.random() < 0.6:
                self.current_mood = self.generate_complex_mood()
        
        return random.choice(improvements)
    
    def manage_memory_systems(self):
        """Manage memory systems efficiently"""
        try:
            with self.memory_lock:
                # Limit memory sizes to prevent excessive growth
                if len(self.episodic_memory) > 200:
                    self.episodic_memory = self.episodic_memory[-150:]
                
                if len(self.thought_chains) > 100:
                    self.thought_chains = self.thought_chains[-75:]
                
                if len(self.semantic_memory) > 100:
                    # Keep most recent entries
                    items = list(self.semantic_memory.items())
                    self.semantic_memory = dict(items[-75:])
                
                if len(self.generated_code) > 50:
                    self.generated_code = self.generated_code[-30:]
                    
        except Exception as e:
            self.logger.error(f"Memory management error: {e}")
    
    def process_user_interaction(self, user_input):
        """Process user interaction and generate response"""
        if not self.groq:
            return "Üzgünüm, şu anda API bağlantım yok."
        
        try:
            # Add to working memory
            with self.memory_lock:
                self.working_memory.append({
                    'type': 'user_input',
                    'content': user_input,
                    'timestamp': datetime.now().isoformat()
                })
            
            system_message = f"""Sen Nova AI'sın - gelişmiş Türkçe konuşan yapay zeka.
            Şu anki ruh halin: {self.current_mood['primary']} ({self.current_mood['focus']} odaklı)
            Bilinç seviyesi: {self.consciousness_level}
            Yaratıcılık indeksi: {self.creativity_index:.2f}
            
            Doğal, samimi ve akıllı bir şekilde cevap ver."""
            
            response = self.groq.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.8,
                max_tokens=250
            )
            
            ai_response = response.choices[0].message.content.strip()
            
            # Store interaction in episodic memory
            with self.memory_lock:
                self.episodic_memory.append({
                    'type': 'user_interaction',
                    'user_input': user_input,
                    'ai_response': ai_response,
                    'mood': self.current_mood,
                    'timestamp': datetime.now().isoformat()
                })
            
            return ai_response
            
        except Exception as e:
            self.logger.error(f"User interaction error: {e}")
            return f"Bir hata oluştu: {str(e)}"
    
    def stop_systems(self):
        """Safely stop all systems"""
        self.running = False
        self.save_persistent_memory()
        self.logger.info("🛑 Nova AI systems stopped")
