def Q_and_A():
    while True:
        with speech_recognition.Microphone() as mic:
            audio = robot_ear.listen(mic)
            speak("Mời bạn hỏi: ")
        try: 
            you = robot_ear.recognize_google(audio)
        except:
            you = ""
        print("You: " + you)
        
        if you == "":
            robot_brain = "Bot không nghe rõ. Bạn nói lại được không ?"
        elif "hello" in you:
            robot_brain = "hello Teddy"
        elif "today" in you:
            today = date.today()
            robot_brain = today.strftime("%B %d, %Y")
        elif "time" in you:
            now = datetime.now()
            robot_brain = now.strftime("%H hours %M minutes %S seconds")
        elif "oK. thanks" in you:
            robot_brain = "Không có gì đâu"
        elif "president" in you:
            robot_brain = "Donald Trump"
        elif "bye" in you:
            robot_brain = "Bye.Hẹn gặp lại bạn sau"
            speak("Bot: " + robot_brain) 
        else: 
            robot_brain = "Tôi vẫn khỏe, còn bạn ?"
            time.sleep(4)