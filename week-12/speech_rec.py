import re, speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as mic:
  r.adjust_for_ambient_noise(mic, duration=0.6)
  print("พูดว่า 'สวัสดี' เช่น 'หมุนมอเตอร์ไปที่ 90 องศา'")
  
  while True:
    try:
      audio = r.listen(mic, timeout=6, phrase_time_limit=10)
      text = r.recognize_google(audio, language="Th-TH")
      print("ได้ยิน :",text)
      
      if text.startswith("สวัสดี"):
        cmd = text.replace("สวัสดี","",1).strip()
        m = re.search(r"(\d+)", cmd)
        angle = int(m.group(1)) if m else None
        print("สวัสดี :", cmd, " | มุม : ", angle)
        
    except sr.WaitTimeoutError:
      print("ไม่มีเสียง พูดมาได้เลย")
      
    except sr.UnknownValueError:
      print("พูดมาได้เลย.....")