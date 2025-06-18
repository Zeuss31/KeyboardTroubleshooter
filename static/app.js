// Nova AI Frontend Application
class NovaAIApp {
    constructor() {
        this.isInitialized = false;
        this.chatActive = false;
        this.statusUpdateInterval = null;
        this.memoryUpdateInterval = null;
        
        this.init();
    }
    
    init() {
        console.log('🚀 Nova AI App başlatılıyor');
        
        if (window.location.pathname === '/chat') {
            this.initializeChat();
        } else {
            this.initializeIndex();
        }
        
        this.setupKeyboardShortcuts();
        this.isInitialized = true;
    }
    
    initializeIndex() {
        console.log('📊 Ana sayfa başlatılıyor');
        
        this.updateStatus();
        this.statusUpdateInterval = setInterval(() => {
            this.updateStatus();
        }, 5000);
        
        this.updateMemories();
        this.memoryUpdateInterval = setInterval(() => {
            this.updateMemories();
        }, 10000);
        
        this.setupControlButtons();
        this.setupAutonomySlider();
    }
    
    initializeChat() {
        console.log('💬 Chat sayfası başlatılıyor');
        
        this.chatActive = true;
        
        this.updateChatStatus();
        setInterval(() => {
            this.updateChatStatus();
        }, 5000);
        
        this.setupChatForm();
        
        this.updateRecentThoughts();
        setInterval(() => {
            this.updateRecentThoughts();
        }, 15000);
        
        const messageInput = document.getElementById('message-input');
        if (messageInput) {
            messageInput.focus();
        }
    }
    
    async updateStatus() {
        try {
            const response = await fetch('/api/status');
            
            if (!response.ok) {
                throw new Error('HTTP ' + response.status);
            }
            
            const data = await response.json();
            
            const consciousnessEl = document.getElementById('consciousness-level');
            if (consciousnessEl) {
                consciousnessEl.innerHTML = '<div class="progress mb-2"><div class="progress-bar bg-primary" style="width: ' + (data.consciousness_level * 100) + '%"></div></div><small>' + (data.consciousness_level * 100).toFixed(1) + '%</small>';
            }
            
            const creativityEl = document.getElementById('creativity-index');
            if (creativityEl) {
                creativityEl.innerHTML = '<div class="progress mb-2"><div class="progress-bar bg-warning" style="width: ' + (data.creativity_index * 100) + '%"></div></div><small>' + (data.creativity_index * 100).toFixed(1) + '%</small>';
            }
            
            const moodEl = document.getElementById('current-mood');
            if (moodEl && data.current_mood) {
                moodEl.innerHTML = '<strong>' + data.current_mood.primary + '</strong><br><small class="text-muted">' + data.current_mood.focus + ' odaklı<br>Yoğunluk: ' + data.current_mood.intensity + '</small>';
            }
            
            const curiosityEl = document.getElementById('curiosity-level');
            if (curiosityEl) {
                curiosityEl.innerHTML = '<div class="progress mb-2"><div class="progress-bar bg-info" style="width: ' + (data.curiosity_level * 100) + '%"></div></div><small>' + (data.curiosity_level * 100).toFixed(1) + '%</small>';
            }
            
            if (data.memory_stats) {
                const episodicEl = document.getElementById('episodic-count');
                const semanticEl = document.getElementById('semantic-count');
                const thoughtsEl = document.getElementById('thoughts-count');
                
                if (episodicEl) episodicEl.textContent = data.memory_stats.episodic;
                if (semanticEl) semanticEl.textContent = data.memory_stats.semantic;
                if (thoughtsEl) thoughtsEl.textContent = data.memory_stats.thought_chains;
            }
            
            this.addActivityItem('💡 Sistem durumu güncellendi - ' + data.status, 'info');
            
        } catch (error) {
            console.error('Durum güncelleme hatası:', error);
            this.addActivityItem('❌ Durum güncellenirken hata: ' + error.message, 'error');
        }
    }
    
    async updateMemories() {
        try {
            const response = await fetch('/api/memories');
            
            if (!response.ok) {
                throw new Error('HTTP ' + response.status);
            }
            
            const data = await response.json();
            
            if (data.recent_thoughts && data.recent_thoughts.length > 0) {
                const latest = data.recent_thoughts[data.recent_thoughts.length - 1];
                this.addActivityItem('🧠 Yeni düşünce: ' + (latest.conclusion || '').substring(0, 60) + '...', 'thought');
            }
            
        } catch (error) {
            console.error('Hafıza güncelleme hatası:', error);
        }
    }
    
    async updateChatStatus() {
        try {
            const response = await fetch('/api/status');
            const data = await response.json();
            
            const statusEl = document.getElementById('ai-status');
            if (statusEl) {
                statusEl.innerHTML = '<span class="status-indicator ' + (data.status === 'active' ? 'status-active' : 'status-inactive') + '"></span>' + (data.status === 'active' ? 'Aktif' : 'Pasif');
            }
            
            const moodEl = document.getElementById('ai-mood');
            if (moodEl && data.current_mood) {
                moodEl.textContent = data.current_mood.primary + ' • ' + data.current_mood.focus + ' odaklı';
            }
            
            const sidebarConsciousness = document.getElementById('sidebar-consciousness');
            if (sidebarConsciousness) {
                sidebarConsciousness.textContent = (data.consciousness_level * 100).toFixed(1) + '%';
            }
            
            const sidebarCreativity = document.getElementById('sidebar-creativity');
            if (sidebarCreativity) {
                sidebarCreativity.textContent = (data.creativity_index * 100).toFixed(1) + '%';
            }
            
            const sidebarCuriosity = document.getElementById('sidebar-curiosity');
            if (sidebarCuriosity) {
                sidebarCuriosity.textContent = (data.curiosity_level * 100).toFixed(1) + '%';
            }
            
            const sidebarFocus = document.getElementById('sidebar-focus');
            if (sidebarFocus) {
                sidebarFocus.textContent = (data.current_mood && data.current_mood.focus) || '--';
            }
            
        } catch (error) {
            console.error('Chat durum güncelleme hatası:', error);
        }
    }
    
    async updateRecentThoughts() {
        try {
            const response = await fetch('/api/memories');
            const data = await response.json();
            
            const thoughtsContainer = document.getElementById('recent-thoughts');
            if (thoughtsContainer && data.recent_thoughts) {
                thoughtsContainer.innerHTML = '';
                
                data.recent_thoughts.slice(-3).forEach(thought => {
                    const thoughtEl = document.createElement('div');
                    thoughtEl.className = 'thought-item';
                    thoughtEl.innerHTML = '<div class="mb-1"><strong>' + ((thought.topic || '').substring(0, 30)) + '...</strong></div><div class="text-muted small">' + ((thought.conclusion || '').substring(0, 80)) + '...</div><div class="text-muted small mt-1">' + new Date(thought.timestamp).toLocaleTimeString('tr-TR') + '</div>';
                    thoughtsContainer.appendChild(thoughtEl);
                });
            }
            
        } catch (error) {
            console.error('Son düşünceler güncelleme hatası:', error);
        }
    }
    
    setupControlButtons() {
        const pauseBtn = document.getElementById('pause-btn');
        const resumeBtn = document.getElementById('resume-btn');
        
        if (pauseBtn) {
            pauseBtn.addEventListener('click', () => {
                this.controlAI('pause');
            });
        }
        
        if (resumeBtn) {
            resumeBtn.addEventListener('click', () => {
                this.controlAI('resume');
            });
        }
    }
    
    setupAutonomySlider() {
        const slider = document.getElementById('autonomy-level');
        
        if (slider) {
            slider.addEventListener('change', (e) => {
                const level = parseInt(e.target.value);
                this.controlAI('adjust_autonomy', { level: level });
            });
        }
    }
    
    async controlAI(action, params) {
        params = params || {};
        try {
            const response = await fetch('/api/control', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(Object.assign({ action: action }, params))
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                this.addActivityItem('✅ ' + data.message, 'success');
            } else {
                this.addActivityItem('❌ ' + data.message, 'error');
            }
            
        } catch (error) {
            console.error('Kontrol hatası:', error);
            this.addActivityItem('❌ Kontrol hatası: ' + error.message, 'error');
        }
    }
    
    setupChatForm() {
        const form = document.getElementById('chat-form');
        const input = document.getElementById('message-input');
        const sendBtn = document.getElementById('send-btn');
        
        if (!form || !input || !sendBtn) return;
        
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const message = input.value.trim();
            if (!message) return;
            
            input.value = '';
            
            this.addChatMessage(message, 'user');
            
            sendBtn.disabled = true;
            sendBtn.innerHTML = '<div class="loading"></div>';
            
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message: message })
                });
                
                const data = await response.json();
                
                if (data.status === 'success') {
                    this.addChatMessage(data.response, 'ai');
                } else {
                    this.addChatMessage('Hata: ' + data.message, 'ai', true);
                }
                
            } catch (error) {
                console.error('Chat hatası:', error);
                this.addChatMessage('Bağlantı hatası: ' + error.message, 'ai', true);
            } finally {
                sendBtn.disabled = false;
                sendBtn.innerHTML = '<i class="fas fa-paper-plane"></i>';
                input.focus();
            }
        });
        
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                form.dispatchEvent(new Event('submit'));
            }
        });
    }
    
    addChatMessage(content, sender, isError) {
        isError = isError || false;
        const messagesContainer = document.getElementById('chat-messages');
        if (!messagesContainer) return;
        
        const messageEl = document.createElement('div');
        messageEl.className = 'message ' + sender + '-message';
        
        const avatar = sender === 'user' ? 
            '<i class="fas fa-user"></i>' : 
            '<i class="fas fa-robot"></i>';
        
        const name = sender === 'user' ? 'Sen' : 'Nova AI';
        const time = new Date().toLocaleTimeString('tr-TR');
        
        messageEl.innerHTML = '<div class="message-avatar">' + avatar + '</div><div class="message-content ' + (isError ? 'border-danger' : '') + '"><strong>' + name + '</strong><p>' + content + '</p><small class="text-muted">' + time + '</small></div>';
        
        messagesContainer.appendChild(messageEl);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    
    addActivityItem(text, type) {
        type = type || 'info';
        const activityLog = document.getElementById('activity-log');
        if (!activityLog) return;
        
        const item = document.createElement('div');
        item.className = 'activity-item';
        
        const time = new Date().toLocaleTimeString('tr-TR');
        item.innerHTML = '<div>' + text + '</div><small class="text-muted">' + time + '</small>';
        
        activityLog.insertBefore(item, activityLog.firstChild);
        
        while (activityLog.children.length > 20) {
            activityLog.removeChild(activityLog.lastChild);
        }
        
        if (activityLog.scrollTop + activityLog.clientHeight >= activityLog.scrollHeight - 10) {
            activityLog.scrollTop = activityLog.scrollHeight;
        }
    }
    
    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'l' && this.chatActive) {
                e.preventDefault();
                this.clearChat();
            }
            
            if (e.key === 'Escape') {
                this.cancelCurrentAction();
            }
        });
    }
    
    clearChat() {
        const messagesContainer = document.getElementById('chat-messages');
        if (messagesContainer) {
            messagesContainer.innerHTML = '<div class="message ai-message"><div class="message-avatar"><i class="fas fa-robot"></i></div><div class="message-content"><strong>Nova AI</strong><p>Chat temizlendi. Yeni bir konuşma başlayalım!</p><small class="text-muted">' + new Date().toLocaleTimeString('tr-TR') + '</small></div></div>';
        }
    }
    
    cancelCurrentAction() {
        const sendBtn = document.getElementById('send-btn');
        if (sendBtn && sendBtn.disabled) {
            sendBtn.disabled = false;
            sendBtn.innerHTML = '<i class="fas fa-paper-plane"></i>';
        }
        
        const input = document.getElementById('message-input');
        if (input && document.activeElement === input) {
            input.blur();
        }
    }
    
    destroy() {
        if (this.statusUpdateInterval) {
            clearInterval(this.statusUpdateInterval);
        }
        if (this.memoryUpdateInterval) {
            clearInterval(this.memoryUpdateInterval);
        }
    }
}

function initializeChat() {
    if (window.novaApp) {
        window.novaApp.destroy();
    }
    window.novaApp = new NovaAIApp();
}

document.addEventListener('DOMContentLoaded', function() {
    window.novaApp = new NovaAIApp();
});
