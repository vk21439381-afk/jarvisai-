from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 15

    Label:
        text: 'J.A.R.V.I.S'
        font_size: 32
        bold: True

    Label:
        id: answer
        text: 'नमस्ते! मैं आपका Jarvis हूँ।'
        font_size: 20

    TextInput:
        id: question
        hint_text: 'अपना सवाल लिखें...'
        size_hint_y: None
        height: 55
        multiline: False

    Button:
        text: 'ASK JARVIS'
        size_hint_y: None
        height: 55
        on_release: app.ask_jarvis()
'''

class JarvisApp(App):

    def build(self):
        return Builder.load_string(KV)

    def ask_jarvis(self):
        question = self.root.ids.question.text.lower()

        if 'hello' in question or 'नमस्ते' in question:
            answer = 'नमस्ते! मैं आपकी कैसे मदद कर सकता हूँ?'
        elif 'नाम' in question:
            answer = 'मेरा नाम JARVIS है।'
        elif 'समय' in question:
            from datetime import datetime
            answer = datetime.now().strftime('%I:%M %p')
        else:
            answer = 'आपका सवाल मिला। AI कनेक्शन अगला चरण है।'

        self.root.ids.answer.text = answer
        self.root.ids.question.text = ''

JarvisApp().run()
