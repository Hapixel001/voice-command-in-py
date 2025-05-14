import speech_recognition as sr

# Inisialisasi recognizer
recognizer = sr.Recognizer()

# Menggunakan mikrofon untuk mendengarkan perintah
with sr.Microphone() as source:
    print("Mendengarkan...")
    audio = recognizer.listen(source)

    try:
        # Menggunakan Google Speech Recognition untuk mengenali suara
        command = recognizer.recognize_google(audio)
        print("Perintah yang didengar:", command)
        
        if "open browser" in command:
            print("Membuka browser...")
            # Buka browser atau aplikasi lainnya
        elif "play music" in command:
            print("Memutar musik...")
            # Kode untuk memutar musik
        else:
            print("Perintah tidak dikenali.")
    except Exception as e:
        print("Error:", e)
