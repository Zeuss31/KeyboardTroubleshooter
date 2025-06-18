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
        console.log('🚀 Initializing Nova AI App');
        
        // Initialize based on current page
        if (window.location.pathname === '/chat') {
            this.initializeChat();
        } else {
            this.initializeIndex();
        }
        
        // Setup keyboard shortcuts
        this.setupKeyboardShortcuts();
        
        this.isInitialized = true;
    }
    
    initializeIndex() {
        console.log('📊 Initializing index page');
        
        // Start status updates
        this.updateStatus();
        this.statusUpdateInterval = setInterval(() => {
            this.updateStatus();
        }, 5000);
        
        // Start memory updates
        this.updateMemories();
        this.memoryUpdateInterval = setInterval(() => {
            this.updateMemories();
        }, 10000);
        
        // Setup control buttons
        this.setupControlButtons();
        
        // Setup autonomy slider
        this.setupAutonomySlider();
    }
    
    initializeChat() {
        console.log('💬 Initializing chat page');
        
        this.chatActive = true;
        
        // Update AI status in chat
        this.updateChatStatus();
        setInterval(() => {
            this.updateChatStatus();
        }, 5000);
        
        // Setup chat form
        this.setupChatForm();
        
        // Update recent thoughts
        this.updateRecentThoughts();
        setInterval(() => {
            this.updateRecentThoughts();
        }, 15000);
        
        // Focus on input
        document.getElementById('message-input')?.focus();
    }
    
    async updateStatus() {
        try {
            const response = await fetch('/api/status');
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            
            const data = await response.json();
            
            // Update consciousness level
            const consciousnessEl = document.getElementById('consciousness-level');
            if (consciousnessEl) {
                consciousnessEl.innerHTML = `
                    <div class="progress mb-2">
                        <div class="progress-bar bg-primary" style="width: ${data.consciousness_level * 100}%"></div>
                    </div>
                    <small>${(data.consciousness_level * 100).toFixed(1)}%</small>
                `;
            }
            
            // Update creativity index
            const creativityEl = document.getElementById('creativity-index');
            if (creativityEl) {
                creativityEl.innerHTML = `
                    <div class="progress mb-2">
                        <div class="progress-bar bg-warning" style="width: ${data.creativity_index * 100}%"></div>
                    </div>
                    <small>${(data.creativity_index * 100).toFixed(1)}%</small>
                `;
            }
            
            // Update mood
            const moodEl = document.getElementById('current-mood');
            if (moodEl && data.current_mood) {
                moodEl.innerHTML = `
                    <strong>${data.current_mood.primary}</strong><br>
                    <small class="text-muted">
                        ${data.current_mood.focus} odaklı<br>
                        Yoğunluk: ${data.current_mood.intensity}
                    </small>
                `;
            }
            
            // Update curiosity level
            const curiosityEl = document.getElementById('curiosity-level');
            if (curiosityEl) {
                curiosityEl.innerHTML = `
                    <div class="progress mb-2">
                        <div class="progress-bar bg-info" style="width: ${data.curiosity_level * 100}%"></div>
                    </div>
                    <small>${(data.curiosity_level * 100).toFixed(1)}%</small>
                `;
            }
            
            // Update memory stats
            if (data.memory_stats) {
                const episodicEl = document.getElementById('episodic-count');
                const semanticEl = document.getElementById('semantic-count');
                const thoughtsEl = document.getElementById('thoughts-count');
                
                if (episodicEl) episodicEl.textContent = data.memory_stats.episodic;
                if (semanticEl) semanticEl.textContent = data.memory_stats.semantic;
                if (thoughtsEl) thoughtsEl.textContent = data.memory_stats.thought_chains;
            }
            
            // Update activity log
            this.addActivityItem(`💡 Sistem durumu güncellendi - ${data.status}`, 'info');
            
        } catch (error) {
            console.error('Status update error:', error);
            this.addActivityItem(`❌ Durum güncellenirken hata: ${error.message}`, 'error');
        }
    }
    
    async updateMemories() {
        try {
            const response = await fetch('/api/memories');
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }
            
            const data = await response.json();
            
            if (data.recent_thoughts && data.recent_thoughts.length > 0) {
                const latest = data.recent_thoughts[data.recent_thoughts.length - 1];
                this.addActivityItem(`🧠 Yeni düşünce: ${latest.conclusion?.substring(0, 60)}...`, 'thought');
            }
            
        } catch (error) {
            console.error('Memory update error:', error);
        }
    }
    
    async updateChatStatus() {
        try {
            const response = await fetch('/api/status');
            const data = await response.json();
            
            // Update status indicator
            const statusEl = document.getElementById('ai-status');
            if (statusEl) {
                statusEl.innerHTML = `
                    <span class="status-indicator ${data.status === 'active' ? 'status-active' : 'status-inactive'}"></span>
                    ${data.status === 'active' ? 'Aktif' : 'Pasif'}
                `;
            }
            
            // Update mood display
            const moodEl = document.getElementById('ai-mood');
            if (moodEl && data.current_mood) {
                moodEl.textContent = `${data.current_mood.primary} • ${data.current_mood.focus} odaklı`;
            }
            
            // Update sidebar stats
            document.getElementById('sidebar-consciousness')?.textContent = 
                `${(data.consciousness_level * 100).toFixed(1)}%`;
            document.getElementById('sidebar-creativity')?.textContent = 
                `${(data.creativity_index * 100).toFixed(1)}%`;
            document.getElementById('sidebar-curiosity')?.textContent = 
                `${(data.curiosity_level * 100).toFixed(1)}%`;
            document.getElementById('sidebar-focus')?.textContent = 
                data.current_mood?.focus || '--';
            
        } catch (error) {
            console.error('Chat status update error:', error);
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
                    thoughtEl.innerHTML = `
                        <div class="mb-1">
                            <strong>${thought.topic?.substring(0, 30)}...</strong>
                        </div>
                        <div class="text-muted small">
                            ${thought.conclusion?.substring(0, 80)}...
                        </div>
                        <div class="text-muted small mt-1">
                            ${new Date(thought.timestamp).toLocaleTimeString('tr-TR')}
                        </div>
                    `;
                    thoughtsContainer.appendChild(thoughtEl);
                });
            }
            
        } catch (error) {
            console.error('Recent thoughts update error:', error);
        }
    }
    
    setupControlButtons() {
        const pauseBtn = document.getElementById('pause-btn');
        const resumeBtn = document.getElementById('resume-btn');
        
        pauseBtn?.addEventListener('click', () => {
            this.controlAI('pause');
        });
        
        resumeBtn?.addEventListener('click', () => {
            this.controlAI('resume');
        });
    }
    
    setupAutonomySlider() {
        const slider = document.getElementById('autonomy-level');
        
        slider?.addEventListener('change', (e) => {
            const level = parseInt(e.target.value);
            this.controlAI('adjust_autonomy', { level });
        });
    }
    
    async controlAI(action, params = {}) {
        try {
            const response = await fetch('/api/control', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ action, ...params })
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                this.addActivityItem(`✅ ${data.message}`, 'success');
            } else {
                this.addActivityItem(`❌ ${data.message}`, 'error');
            }
            
        } catch (error) {
            console.error('Control error:', error);
            this.addActivityItem(`❌ Kontrol hatası: ${error.message}`, 'error');
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
            
            // Clear input immediately
            input.value = '';
            
            // Add user message
            this.addChatMessage(message, 'user');
            
            // Show loading state
            sendBtn.disabled = true;
            sendBtn.innerHTML = '<div class="loading"></div>';
            
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message })
                });
                
                const data = await response.json();
                
                if (data.status === 'success') {
                    this.addChatMessage(data.response, 'ai');
                } else {
                    this.addChatMessage(`Hata: ${data.message}`, 'ai', true);
                }
                
            } catch (error) {
                console.error('Chat error:', error);
                this.addChatMessage(`Bağlantı hatası: ${error.message}`, 'ai', true);
            } finally {
                // Reset send button
                sendBtn.disabled = false;
                sendBtn.innerHTML = '<i class="fas fa-paper-plane"></i>';
                input.focus();
            }
        });
        
        // Handle Enter key
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                form.dispatchEvent(new Event('submit'));
            }
        });
    }
    
    addChatMessage(content, sender, isError = false) {
        const messagesContainer = document.getElementById('chat-messages');
        if (!messagesContainer) return;
        
        const messageEl = document.createElement('div');
        messageEl.className = `message ${sender}-message`;
        
        const avatar = sender === 'user' ? 
            '<i class="fas fa-user"></i>' : 
            '<i class="fas fa-robot"></i>';
        
        const name = sender === 'user' ? 'Sen' : 'Nova AI';
        const time = new Date().toLocaleTimeString('tr-TR');
        
        messageEl.innerHTML = `
            <div class="message-avatar">
                ${avatar}
            </div>
            <div class="message-content ${isError ? 'border-danger' : ''}">
                <strong>${name}</strong>
                <p>${content}</p>
                <small class="text-muted">${time}</small>
            </div>
        `;
        
        messagesContainer.appendChild(messageEl);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    
    addActivityItem(text, type = 'info') {
        const activityLog = document.getElementById('activity-log');
        if (!activityLog) return;
        
        const item = document.createElement('div');
        item.className = 'activity-item';
        
        const time = new Date().toLocaleTimeString('tr-TR');
        item.innerHTML = `
            <div>${text}</div>
            <small class="text-muted">${time}</small>
        `;
        
        // Add to top of log
        activityLog.insertBefore(item, activityLog.firstChild);
        
        // Keep only last 20 items
        while (activityLog.children.length > 20) {
            activityLog.removeChild(activityLog.lastChild);
        }
        
        // Auto-scroll if at bottom
        if (activityLog.scrollTop + activityLog.clientHeight >= activityLog.scrollHeight - 10) {
            activityLog.scrollTop = activityLog.scrollHeight;
        }
    }
    
    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Ctrl + L: Clear chat
            if (e.ctrlKey && e.key === 'l' && this.chatActive) {
                e.preventDefault();
                this.clearChat();
            }
            
            // Escape: Cancel current action
            if (e.key === 'Escape') {
                this.cancelCurrentAction();
            }
        });
    }
    
    clearChat() {
        const messagesContainer = document.getElementById('chat-messages');
        if (messagesContainer) {
            messagesContainer.innerHTML = `
                <div class="message ai-message">
                    <div class="message-avatar">
                        <i class="fas fa-robot"></i>
                    </div>
                    <div class="message-content">
                        <strong>Nova AI</strong>
                        <p>Chat temizlendi. Yeni bir konuşma başlayalım!</p>
                        <small class="text-muted">${new Date().toLocaleTimeString('tr-TR')}</small>
                    </div>
                </div>
            `;
        }
    }
    
    cancelCurrentAction() {
        // Reset any loading states
        const sendBtn = document.getElementById('send-btn');
        if (sendBtn && sendBtn.disabled) {
            sendBtn.disabled = false;
            sendBtn.innerHTML = '<i class="fas fa-paper-plane"></i>';
        }
        
        // Clear input focus if needed
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

// Global functions for template access
function initializeChat() {
    if (window.novaApp) {
        window.novaApp.destroy();
    }
    window.novaApp = new NovaAIApp();
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('🎯 DOM loaded, initializing Nova AI App');
    
    if (!window.novaApp) {
        window.novaApp = new NovaAIApp();
    }
});

// Handle page unload
window.addEventListener('beforeunload', function() {
    if (window.novaApp) {
        window.novaApp.destroy();
    }
});
