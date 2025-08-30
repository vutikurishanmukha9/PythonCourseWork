import speech_recognition as sr
import pyttsx3
import random

class FriendlyAssistant:
    def __init__(self):
        try:
            self.engine = pyttsx3.init()
            print("🔄 Initializing speech engine...")
        except Exception as e:
            print(f"⚠️ Warning: Speech engine initialization failed: {e}")
            self.engine = None
            
        self.current_language = 'en'  # Default language
        self.speech_working = True
        self.language_codes = {
            'english': 'en',
            'spanish': 'es',
            'french': 'fr',
            'german': 'de',
            'italian': 'it',
            'portuguese': 'pt',
            'russian': 'ru',
            'japanese': 'ja',
            'chinese': 'zh',
            'korean': 'ko',
            'arabic': 'ar',
            'hindi': 'hi',
            'bengali': 'bn',
            'tamil': 'ta',
            'telugu': 'te',
            'marathi': 'mr',
            'gujarati': 'gu',
            'punjabi': 'pa'
        }
        
        # Friendly responses in different languages
        self.responses = {
            'greetings': {
                'en': [
                    "Hi there! I'm your friendly virtual assistant. How can I brighten your day?",
                    "Hello! Great to see you! What can I help you with today?",
                    "Hey! I'm excited to help you today. What's on your mind?"
                ],
                'es': [
                    "¡Hola! Soy tu asistente virtual amigable. ¿Cómo puedo alegrar tu día?",
                    "¡Hola! ¡Genial verte! ¿En qué puedo ayudarte hoy?"
                ],
                'fr': [
                    "Salut! Je suis votre assistant virtuel amical. Comment puis-je égayer votre journée?",
                    "Bonjour! Ravi de vous voir! Comment puis-je vous aider aujourd'hui?"
                ],
                'hi': [
                    "नमस्ते! मैं आपका मित्रवत आभासी सहायक हूं। आज मैं आपकी कैसे मदद कर सकता हूं?",
                    "हैलो! आपसे मिलकर खुशी हुई! आज मैं आपके लिए क्या कर सकता हूं?"
                ]
            },
            'music': {
                'en': [
                    "Awesome choice! Let me get your music started right away! 🎵",
                    "Great! Time for some tunes! Music is now playing! 🎶",
                    "Perfect! Let's get this party started with some music! 🎉"
                ],
                'es': [
                    "¡Excelente elección! ¡Te pongo música ahora mismo! 🎵",
                    "¡Genial! ¡Es hora de música! ¡La música está sonando! 🎶"
                ],
                'fr': [
                    "Excellent choix! Je lance votre musique tout de suite! 🎵",
                    "Parfait! C'est l'heure de la musique! 🎶"
                ],
                'hi': [
                    "बेहतरीन पसंद! मैं अभी आपके लिए संगीत चला रहा हूं! 🎵",
                    "शानदार! संगीत का समय! 🎶"
                ]
            },
            'reminder': {
                'en': [
                    "Got it! I've set a friendly reminder for you to push code at 5pm. I'll make sure you don't forget! ⏰",
                    "Perfect! Reminder set! I'll give you a gentle nudge at 5pm to push your code! 📝"
                ],
                'es': [
                    "¡Entendido! He establecido un recordatorio para que subas el código a las 5pm. ⏰",
                    "¡Perfecto! ¡Recordatorio establecido! 📝"
                ],
                'fr': [
                    "Compris! J'ai défini un rappel pour pousser le code à 17h. ⏰",
                    "Parfait! Rappel défini! 📝"
                ],
                'hi': [
                    "समझ गया! मैंने शाम 5 बजे कोड पुश करने के लिए रिमाइंडर सेट कर दिया है। ⏰",
                    "परफेक्ट! रिमाइंडर सेट कर दिया! 📝"
                ]
            },
            'geopolitics': {
                'en': [
                    "That's a deep topic! Regarding geopolitics, transparency and civic engagement are indeed crucial for maintaining stability and addressing public concerns effectively.",
                    "Interesting question about geopolitics! Democratic participation and transparent governance are key to resolving conflicts peacefully."
                ],
                'es': [
                    "¡Ese es un tema profundo! En cuanto a geopolítica, la transparencia y la participación cívica son cruciales.",
                    "¡Pregunta interesante sobre geopolítica!"
                ],
                'fr': [
                    "C'est un sujet profond! Concernant la géopolitique, la transparence est cruciale.",
                    "Question intéressante sur la géopolitique!"
                ],
                'hi': [
                    "यह एक गहरा विषय है! भू-राजनीति के संबंध में, पारदर्शिता और नागरिक सहभागिता महत्वपूर्ण है।",
                    "भू-राजनीति के बारे में दिलचस्प सवाल!"
                ]
            },
            'goodbye': {
                'en': [
                    "It was wonderful chatting with you! Have an absolutely amazing day! Take care! 👋",
                    "Goodbye, my friend! Hope you have a fantastic day ahead! See you soon! 😊",
                    "Take care and have a beautiful day! It was great helping you! Bye! 🌟"
                ],
                'es': [
                    "¡Fue maravilloso charlar contigo! ¡Que tengas un día increíble! ¡Cuídate! 👋",
                    "¡Adiós, mi amigo! ¡Espero que tengas un día fantástico! 😊"
                ],
                'fr': [
                    "C'était merveilleux de discuter avec vous! Passez une journée fantastique! 👋",
                    "Au revoir, mon ami! J'espère que vous passerez une excellente journée! 😊"
                ],
                'hi': [
                    "आपसे बात करके बहुत अच्छा लगा! आपका दिन शानदार हो! खुश रहिए! 👋",
                    "अलविदा, मित्र! आपका दिन बेहतरीन हो! 😊"
                ]
            },
            'language_changed': {
                'en': "Great! I've switched to English. How can I help you?",
                'es': "¡Excelente! He cambiado al español. ¿Cómo puedo ayudarte?",
                'fr': "Parfait! J'ai basculé en français. Comment puis-je vous aider?",
                'hi': "बढ़िया! मैंने हिंदी में बदल लिया है। मैं आपकी कैसे मदद कर सकता हूं?",
                'de': "Großartig! Ich habe auf Deutsch umgestellt. Wie kann ich helfen?",
                'it': "Perfetto! Ho cambiato in italiano. Come posso aiutarti?",
                'pt': "Ótimo! Mudei para português. Como posso ajudar?",
                'ja': "素晴らしい！日本語に切り替えました。どのようにお手伝いできますか？",
                'zh': "太好了！我已经切换到中文。我能如何帮助您？",
                'ko': "좋습니다! 한국어로 전환했습니다. 어떻게 도와드릴까요?",
                'ar': "رائع! لقد تحولت إلى العربية. كيف يمكنني مساعدتك؟",
                'ta': "சிறப்பு! நான் தமிழுக்கு மாறியுள்ளேன். நான் எப்படி உதவ முடியும்?",
                'te': "అద్భుతం! నేను తెలుగుకు మార్చుకున్నాను. నేను ఎలా సహాయం చేయగలను?",
                'mr': "उत्तम! मी मराठीत बदललो आहे. मी तुम्हाला कशी मदत करू शकतो?",
                'gu': "સરસ! હું ગુજરાતીમાં બદલાઈ ગયો છું. હું તમારી કેવી રીતે મદદ કરી શકું?",
                'bn': "দুর্দান্ত! আমি বাংলায় পরিবর্তিত হয়েছি। আমি কিভাবে সাহায্য করতে পারি?",
                'pa': "ਬਹੁਤ ਵਧੀਆ! ਮੈਂ ਪੰਜਾਬੀ ਵਿੱਚ ਬਦਲ ਗਿਆ ਹਾਂ। ਮੈਂ ਕਿਵੇਂ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ?"
            },
            'unknown': {
                'en': [
                    "Hmm, I'm still learning that one! But I'm always eager to help in other ways! What else can I do for you? 😊",
                    "I don't have that feature yet, but I'm growing every day! Is there something else I can help you with? 🌱",
                    "That's not in my toolkit right now, but I'd love to help you with something else! What would you like to try? ✨"
                ],
                'es': [
                    "¡Hmm, todavía estoy aprendiendo eso! ¡Pero siempre estoy ansioso por ayudar de otras maneras! 😊",
                    "No tengo esa función todavía, pero estoy creciendo cada día! 🌱"
                ],
                'fr': [
                    "Hmm, j'apprends encore cela! Mais je suis toujours impatient d'aider d'autres façons! 😊",
                    "Je n'ai pas cette fonction encore, mais je grandis chaque jour! 🌱"
                ],
                'hi': [
                    "हम्म, मैं अभी भी वह सीख रहा हूं! लेकिन मैं हमेशा अन्य तरीकों से मदद करने के लिए उत्सुक हूं! 😊",
                    "मेरे पास अभी वह सुविधा नहीं है, लेकिन मैं हर दिन बढ़ रहा हूं! 🌱"
                ]
            }
        }
        
        self.setup_voice()
    
    def setup_voice(self):
        """Setup voice properties"""
        try:
            if not self.engine:
                print("🔄 Attempting to reinitialize speech engine...")
                self.engine = pyttsx3.init()
            
            voices = self.engine.getProperty('voices')
            # Try to set a pleasant voice (usually female voice is at index 1)
            if len(voices) > 1:
                self.engine.setProperty('voice', voices[1].id)
            else:
                self.engine.setProperty('voice', voices[0].id)
            
            # Set speech rate (slower for better understanding)
            self.engine.setProperty('rate', 180)
            # Set volume
            self.engine.setProperty('volume', 0.9)
            
            self.speech_working = True
            print("🔊 Voice engine initialized successfully!")
            
        except Exception as e:
            print(f"⚠️ Voice setup warning: {e}")
            self.speech_working = False
    
    def speak(self, text):
        """Convert text to speech with improved error handling"""
        print(f"🤖 Assistant: {text}")
        
        if not self.speech_working or not self.engine:
            print("🔇 Speech is disabled - text response only")
            return
        
        try:
            # Stop any previous speech
            self.engine.stop()
            
            # Add a small delay to ensure engine is ready
            import time
            time.sleep(0.1)
            
            # Say the text
            self.engine.say(text)
            self.engine.runAndWait()
            
            print("✅ Speech completed")
            
        except Exception as e:
            print(f"❌ Speech error: {e}")
            print("🔄 Trying to recover speech engine...")
            
            # Try to recover the engine
            try:
                self.engine.stop()
                time.sleep(0.2)
                self.engine = pyttsx3.init()
                self.setup_voice()
                
                if self.speech_working:
                    self.engine.say(text)
                    self.engine.runAndWait()
                    print("✅ Speech recovered successfully")
                else:
                    print("❌ Speech recovery failed - continuing with text only")
                    
            except Exception as e2:
                print(f"❌ Speech engine recovery failed: {e2}")
                print("💡 Continuing with text-only responses...")
                self.speech_working = False
    
    def get_random_response(self, category, language=None):
        """Get a random response from a category in the specified language"""
        if language is None:
            language = self.current_language
        
        if language in self.responses[category]:
            return random.choice(self.responses[category][language])
        else:
            # Fallback to English if language not available
            return random.choice(self.responses[category]['en'])
    
    def change_language(self, command):
        """Change the assistant's language based on command"""
        for lang_name, lang_code in self.language_codes.items():
            if lang_name in command.lower():
                self.current_language = lang_code
                response = self.responses['language_changed'].get(lang_code, 
                          self.responses['language_changed']['en'])
                self.speak(response)
                return True
        return False
    
    def get_input_mode(self):
        """Ask user to choose input mode"""
        print("\n" + "="*50)
        print("🎯 Choose your input method:")
        print("1️⃣  Voice input → Voice output (speak & hear)")
        print("2️⃣  Text input → Voice output (type & hear)")
        print("3️⃣  Voice only output → No voice input (type & hear, no mic needed)")
        print("4️⃣  Auto mode (try voice, fallback to text)")
        print("="*50)
        
        while True:
            try:
                choice = input("Enter your choice (1/2/3/4) or just press Enter for auto mode: ").strip()
                if choice == '' or choice == '4':
                    return 'auto'
                elif choice == '1':
                    return 'voice'
                elif choice == '2':
                    return 'text'
                elif choice == '3':
                    return 'text_only'
                else:
                    print("❌ Please enter 1, 2, 3, or 4")
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                return None

    def listen_voice(self):
        """Listen to user voice input and convert speech to text"""
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("🎤 Listening... (Speak now)")
                recognizer.pause_threshold = 1
                recognizer.energy_threshold = 300
                
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                # Use language-specific recognition
                lang_for_recognition = f"{self.current_language}-in" if self.current_language == 'en' else self.current_language
                command = recognizer.recognize_google(audio, language=lang_for_recognition)
                print(f"🗣️ You said: {command}")
                return command.lower()
                
        except sr.WaitTimeoutError:
            print("⏰ No speech detected.")
            return None
        except sr.UnknownValueError:
            print("❌ Sorry, I didn't understand that")
            return None
        except sr.RequestError as e:
            print(f"❌ Speech service error: {e}")
            return None
        except Exception as e:
            print(f"❌ Microphone error: {e}")
            return None

    def get_text_input(self):
        """Get text input from user"""
        try:
            print("💬 Type your message (or 'voice' to switch to voice mode):")
            command = input("👤 You: ").strip()
            if command:
                print(f"📝 You typed: {command}")
                return command.lower()
            return None
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            return "exit"
        except Exception as e:
            print(f"❌ Input error: {e}")
            return None

    def listen(self, input_mode='auto'):
        """Get user input based on selected mode"""
        if input_mode == 'voice':
            return self.listen_voice()
        elif input_mode == 'text' or input_mode == 'text_only':
            # Text input but still give voice output
            return self.get_text_input()
        elif input_mode == 'auto':
            # Try voice first, fallback to text
            print("\n🎯 Auto mode: Trying voice input first...")
            print("💡 Tip: If voice doesn't work, I'll ask for text input!")
            
            voice_command = self.listen_voice()
            if voice_command:
                return voice_command
            
            print("🔄 Voice didn't work, switching to text input...")
            print("🔊 Don't worry, I'll still respond with voice!")
            return self.get_text_input()
        
        return None
    
    def process_command(self, command, input_mode='auto'):
        """Process the user command and respond appropriately"""
        if not command:
            return True, input_mode
        
        # Check for input mode switching
        if command == 'voice':
            print("🎤 Switched to voice input mode!")
            self.speak("Switched to voice input mode! Now you can speak to me!")
            return True, 'voice'
        elif command == 'text':
            print("💬 Switched to text input mode! I'll still respond with voice.")
            self.speak("Switched to text input mode! Type your messages and I'll respond with my voice!")
            return True, 'text'
        elif command == 'text only' or command == 'textonly':
            print("💬 Switched to text-only mode! Perfect for quiet environments.")
            self.speak("Switched to text-only input mode! Type your messages and I'll speak back to you!")
            return True, 'text_only'
        elif command == 'auto':
            print("🎯 Switched to auto mode!")
            self.speak("Switched to auto mode! I'll try voice first, then text if needed!")
            return True, 'auto'
        
        # Check for language change requests
        if 'speak in' in command or 'change to' in command or 'switch to' in command:
            if self.change_language(command):
                return True, input_mode
        
        # Check for exit commands
        exit_words = ['exit', 'stop', 'bye', 'goodbye', 'quit', 'see you']
        if any(word in command for word in exit_words):
            goodbye_msg = self.get_random_response('goodbye')
            self.speak(goodbye_msg)
            return False, input_mode
        
        # Process other commands
        if 'play music' in command or 'music' in command:
            music_msg = self.get_random_response('music')
            self.speak(music_msg)
            
        elif 'reminder' in command:
            reminder_msg = self.get_random_response('reminder')
            self.speak(reminder_msg)
            
        elif 'geo politic' in command or 'geopolitics' in command:
            geo_msg = self.get_random_response('geopolitics')
            self.speak(geo_msg)
            
        elif 'hello' in command or 'hi' in command or 'hey' in command:
            greeting_msg = self.get_random_response('greetings')
            self.speak(greeting_msg)
            
        elif 'how are you' in command:
            self.speak("I'm doing fantastic! Thank you for asking! I'm here and ready to help you with anything you need. How are you doing today?")
            
        elif 'what can you do' in command or 'help' in command:
            help_msg = (
                "I'm your friendly assistant! Here's what I can do: "
                "🎵 Play music, ⏰ Set reminders, 🌍 Discuss geopolitics, "
                "🗣️ Change languages by saying 'speak in' followed by language name, "
                "💬 Switch input modes - say 'voice' for voice input, 'text' for typing with voice response, or 'auto' for flexible mode, "
                "and have friendly conversations with you! "
                "I always respond with voice no matter how you input your message!"
            )
            self.speak(help_msg)
            
        elif 'thank you' in command or 'thanks' in command:
            self.speak("You're absolutely welcome! It's my pleasure to help you! Is there anything else you'd like me to do?")
            
        else:
            unknown_msg = self.get_random_response('unknown')
            self.speak(unknown_msg)
        
        return True, input_mode
    
    def run(self):
        """Main function to run the assistant"""
        print("🤖 Welcome to your Friendly Virtual Assistant!")
        print("✨ I support multiple input methods and ALWAYS respond with voice!")
        print("🔊 No matter how you communicate with me, I'll always speak back to you!")
        
        # Get initial input mode preference
        input_mode = self.get_input_mode()
        if input_mode is None:
            return
        
        # Initial greeting
        greeting = self.get_random_response('greetings')
        self.speak(greeting)
        
        # Show mode explanations
        mode_explanations = {
            'voice': "🎤 VOICE MODE: Speak to me and I'll speak back!",
            'text': "💬 TEXT MODE: Type your messages, I'll respond with voice!",
            'text_only': "📝 TEXT-ONLY MODE: Type your messages, I'll speak back! (Perfect when mic isn't available)",
            'auto': "🎯 AUTO MODE: I'll try voice first, fallback to text if needed, always speak back!"
        }
        
        print(f"\n{mode_explanations[input_mode]}")
        print("🔊 I ALWAYS respond with voice - you'll hear me speak!")
        print("💬 Switch modes anytime: 'voice', 'text', 'text only', or 'auto'")
        print("🌍 Change languages: 'speak in [language name]'")
        print("❌ Exit: 'goodbye' or 'exit'")
        print("-" * 60)
        
        while True:
            try:
                command = self.listen(input_mode)
                should_continue, input_mode = self.process_command(command, input_mode)
                if not should_continue:
                    break
                    
                # Show current mode after each interaction
                if command:
                    status = "🔊 Voice Working" if self.speech_working else "🔇 Text Only"
                    print(f"📍 Input mode: {input_mode.upper()} | Status: {status}")
                    print("-" * 30)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Thanks for using the assistant!")
                self.speak("Goodbye! Thanks for chatting with me!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")
                self.speak("Sorry, something went wrong. Let's try again!")
                continue

# Create and run the assistant
if __name__ == "__main__":
    assistant = FriendlyAssistant()
    assistant.run()