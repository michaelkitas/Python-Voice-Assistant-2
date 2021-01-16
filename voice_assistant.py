import pyttsx3
import speech_recognition as sr
import getpass
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:/Users/" + getpass.getuser() + "/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def music(song):
    speak("1 second")
    driver.get("https://www.youtube.com/results?search_query=" + song)
    delay = 3
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'video-title')))
    driver.find_element_by_css_selector("a[id='video-title']").click()
    speak("Enjoy " + song)

while True:
    print("Listening")
    text = get_audio()

    if "hello" in text:
        speak("Hello there, how are you?")

    elif "fine and you" in text:
        speak("I am doing great")
    
    elif "fine" in text:
        speak("That's great")

    elif "say" in text:
        speak("Everyone like and subscribe for a better 2021")
    elif "play" in text:
        music(text.split('play')[1])