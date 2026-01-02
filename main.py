import webbrowser
import time
import random
import urllib.parse
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import mainthread


running = True
remaining_searches = 0  
class SearchApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text=f"Remaining Searches: {remaining_searches}", font_size=20)
        self.layout.add_widget(self.label)
        
        self.start_button = Button(text="Start Search", background_color=(0, 1, 0, 1))
        self.start_button.bind(on_press=self.start_search)
        self.layout.add_widget(self.start_button)
        
        self.stop_button = Button(text="Stop Search", background_color=(1, 0, 0, 1))
        self.stop_button.bind(on_press=self.stop_search)
        self.layout.add_widget(self.stop_button)
        
        self.exit_button = Button(text="Exit", background_color=(0.5, 0.5, 0.5, 1))
        self.exit_button.bind(on_press=self.stop)
        self.layout.add_widget(self.exit_button)
        
        return self.layout
    
    @mainthread
    def update_counter(self):
        self.label.text = f"Remaining Searches: {remaining_searches}"
    
    def start_search(self, instance):
        global running
        running = True
        thread = threading.Thread(target=self.open_random_keywords)
        thread.start()
    
    def stop_search(self, instance):
        global running
        running = False
    
    def open_random_keywords(self, delay=10):
        global running, remaining_searches
        random.shuffle(keywords)
        remaining_searches = len(keywords)
        self.update_counter()
        
        for i, keyword in enumerate(keywords, start=1):
            if not running:
                print("\nSearch stopped by the user.")
                break
            try:
                encoded_keyword = urllib.parse.quote(keyword)
                url = f'https://www.bing.com/search?q={encoded_keyword}&qs=n&form=QBRE&PC=EMMX01'
                print(f"Opening search {i}: {keyword}")
                webbrowser.open(url)
                remaining_searches -= 1
                self.update_counter()
                time.sleep(delay)
            except Exception as e:
                print(f"An error occurred while opening the link: {e}")
  
keywords = [
    'Artificial Intelligence', 'Data Science', 'Blockchain', 'Quantum Computing',
    'Sustainable Energy', 'Climate Change', 'Genetic Engineering', 'Robotics',
    'Augmented Reality', 'Virtual Reality', 'Digital Marketing', 'Space Exploration',
    'Nanotechnology', 'Cybersecurity', 'Machine Learning', 'Biotechnology',
    'Philosophy of Mind', 'Psychology', 'Global Economics', 'Cryptocurrency',
    'Ecosystem', 'Wildlife Conservation'
]

if __name__ == "__main__":
    SearchApp().run()
