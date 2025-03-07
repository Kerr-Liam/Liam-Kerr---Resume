
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

# Speech engine installation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female
activationWord = 'friday'  # single word

# Configure browser
opera_gx_path = r"E:\Users\Admin\AppData\Local\Programs\Opera GX\launcher.exe"
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(opera_gx_path))

def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand(timeout=2):
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        print('Listening...')
        try:
            audio = listener.listen(source, timeout=timeout)
        except sr.WaitTimeoutError:
            print('No speech detected')
            return 'None'

    try:
        print('Recognizing speech...')
        query = listener.recognize_google(audio, language='en-gb')
        print(f'The input speech was: {query}')
    except sr.UnknownValueError:
        print('Speech not recognized')
        speak('Speech not recognized')
        return 'None'
    except sr.RequestError:
        print('Sorry, I am currently unable to process your request.')
        speak('Sorry, I am currently unable to process your request.')
        return 'None'

    return query.lower()

def search_wikipedia(query=''):
    try:
        searchResults = wikipedia.search(query)
        if not searchResults:
            error_message = "No Wikipedia result found for '" + query + "'."
            print(error_message)
            speak(error_message)
            return 'No result received'

        wikiPage = wikipedia.page(searchResults[0])
        print(wikiPage.title)
        wikiSummary = str(wikiPage.summary)
        return wikiSummary
    except wikipedia.DisambiguationError as error:
        error_message = "Wikipedia disambiguation error: " + str(error)
        print(error_message)
        speak(error_message)
        return 'No result received'
    except wikipedia.PageError:
        error_message = "No Wikipedia page found for '" + query + "'."
        print(error_message)
        speak(error_message)
        return 'No result received'
    except wikipedia.WikipediaException as error:
        error_message = "Wikipedia exception occurred: " + str(error)
        print(error_message)
        speak(error_message)
        return 'No result received'

# Main loop
if __name__ == '__main__':
    isActivated = False

    while not isActivated:
        query = parseCommand()

        if query.lower() == activationWord:
            speak('How may I be of assistance?')
            isActivated = True

    while True:
        query = parseCommand().lower().split()

        # List commands
        if query[0] == 'say':
            if 'hello' in query:
                speak('Hello there')
            else:
                query.pop(0)  # removes 'say'
                speech = ' '.join(query)
                speak(speech)

        # Navigation
        if query[0] == 'go' and query[1] == 'to':
            speak('Opening..')
            query = ' '.join(query[2:])
            try:
                webbrowser.get('opera').open_new(query)
            except webbrowser.Error:
                error_message = "Failed to open the web page."
                print(error_message)
                speak(error_message)

        if query[0] == 'open':
            query.pop(0)
            query = str(query)
            speak('Opening...')
            try:
                webbrowser.get('opera').open_new(f'www.{query}')
            except webbrowser.Error:
                error_message = "Failed to open the web page."
                print(error_message)
                speak(error_message)

        # Wikipedia
        if query[0] == 'research':
            query = ' '.join(query[1:])
            speak('Searching Wikipedia...')
            result = search_wikipedia(query)
            speak(result)

        # Time
        if 'time' in query or 'current time' in query:
            current_time = datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        # Check for end loop condition
        if query[0] == 'thank' and query[1] == 'you':
            print('Goodbye!')
            speak('You are welcome, Goodbye!')
            exit()