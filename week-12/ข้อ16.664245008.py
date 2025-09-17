import speech_recognition as sr

# เมนูช่วยเหลือนักศึกษา
student_help_menu_th = (
    "ระบบช่วยเหลือนักศึกษา\n"
    "1. 📚 ลงทะเบียนเรียน\n"
    "2. 💰 ทุนการศึกษา\n"
    "3. 🏠 หอพักนักศึกษา\n"
    "4. 🩺 บริการด้านสุขภาพ\n"
    "5. 💻 ระบบออนไลน์ E-Learning\n"
    "6. 📖 ห้องสมุดกลาง\n"
    "7. 📅 ตารางสอบ\n"
    "8. 📞 ติดต่อเจ้าหน้าที่\n"
)

student_help_menu_en = (
    "Student Help System\n"
    "1. 📚 Course Registration\n"
    "2. 💰 Scholarships\n"
    "3. 🏠 Student Dormitory\n"
    "4. 🩺 Health Services\n"
    "5. 💻 Online Learning System\n"
    "6. 📖 Central Library\n"
    "7. 📅 Exam Schedule\n"
    "8. 📞 Contact Staff\n"
)

r = sr.Recognizer()
with sr.Microphone() as mic:
    r.adjust_for_ambient_noise(mic, duration=0.6)
    print("พูดคำสั่ง เช่น 'สวัสดี ช่วยเหลือ' / 'สวัสดี help me'")

    while True:
        try:
            audio = r.listen(mic, timeout=6, phrase_time_limit=10)
            text = r.recognize_google(audio, language="th-TH")  # ฟังหลักเป็นภาษาไทย
            print("ได้ยิน :", text)

            if text.startswith("สวัสดี"):
                cmd = text.replace("สวัสดี", "", 1).strip()

                # --- ถ้าในคำพูดมี 'ช่วยเหลือ' (ไทย) ---
                if "ช่วยเหลือ" in cmd:
                    print(student_help_menu_th)

                # --- ถ้าในคำพูดมี 'help me' (อังกฤษ) ---
                elif "help me" in cmd.lower():
                    print(student_help_menu_en)

                # --- ถ้าแค่พูดสวัสดีอย่างเดียว ---
                else:
                    print("สวัสดี! คุณสามารถพูด 'ช่วยเหลือ' หรือ 'help me' เพื่อดูเมนูช่วยเหลือ")

        except sr.WaitTimeoutError:
            print("⏳ ไม่มีเสียง พูดมาได้เลย")

        except sr.UnknownValueError:
            print("❓ พูดมาได้เลย.....")
