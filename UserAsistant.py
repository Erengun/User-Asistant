import subprocess
import webbrowser
import os
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
Name , Surname = "Eren" , "Gün"
Username , Pass = "erengun" , 123
kilo , boy = 0 , 0
AsistantName = "Ezreal"
UserInfo = [Name , Surname , kilo , boy , os.name]
AsistantInfo = [AsistantName]
LoginCount = 3
Ans = 1
AnswersGood = {"İyi" , "Iyi" , "Harika" , "Mükemmel" , "iyi" , "Good" , "Eh" , "fena" , "Fena"}
while LoginCount > 0:
      print("Kalan deneme hakkı : " , LoginCount)
      Username0 = str(input("Kullanıcı adı : "))
      Pass0 = int(input("Sifre : "))
      print("Kontrol ediliyor...")
      print(" ")
      NameCheck = Username == Username0
      PassCheck = Pass == Pass0
      if NameCheck == True:
            if PassCheck == True:
                  def takeCommand():
                      r=sr.Recognizer()
                      with sr.Microphone() as source:
                          print("Listening...")
                          audio=r.listen(source)

                          try:
                              statement=r.recognize_google(audio,language='tr')
                              print(f"user said:{statement}\n")

                          except Exception as e:
                              speak("Pardon me, please say that again")
                              return "None"
                          return statement
                  print("Loading your AI personal assistant G-One")
                  speak("Loading your AI personal assistant Ero")
                  wishMe()
                  speak("Giriş başarılı hoşgeldin")
                  Userwant = str(input("Naber? : "))
                  if Userwant in AnswersGood:
                        print("Harika :)")
                  else:
                        if "Kötü" in Userwant or "Bad" in Userwant:
                              print("Aga B")
                        else:
                              print("Ne diyon aminyum iyi misin kötü mü?")
                  print("*"*10)
                  AsistantName = input("Benim adım ne sahip ? : ")
                  print(AsistantName , "demek anladım :)")
                  print(" "*50)
                  while Ans>0 and Ans<3:      
                        print("Şu özellikler kullanıma açık sahip :")
                        print("1-)Vize final notları ile geçti kaldı hesabı")
                        print("2-) Kilo endeksi hesaplama")
                        Ans = int(input("İstediğin seçenenin başındaki numaraya tuşla veya çıkış yapmak için rastgele bir sayıya basın : "))
                        if  Ans == 1:
                              Vize1 = int(input("İlk vize notun ne sahip : "))
                              Vize2 = int(input("İkinci vize notunu da yazar mısınız: "))
                              Final = int(input("Kardeşim bir de final notunu yazar mısın? : "))
                              Result = ((((Vize1+Vize2) / 2 )*60/100) + (Final*40/100))
                              print("Ortalaman: " , Result) 
                              if Result >= 50:
                                    print("Tebrikler" , Name , "geçtiniz")
                              else:
                                    print("Yaz okulu g.o")
                              print(" "*50)
                        if Ans == 2 :
                              kilo = float(input("Kilonu yaz sahip : "))
                              boy = float(input("Boy yaz sahip (metre) : "))
                              KullaniciInfo = ["isim" , kilo , boy ]
                              indeks = kilo / boy**2
                              if indeks > 0 and indeks < 18.4:
                                    print("Zayıfsınız")
                              if indeks > 18.5 and indeks < 24.9:
                                    print("Harikasınız sahip")
                              if indeks > 25 and indeks < 29.9:
                                    print("Kilo çok" , Name ,"az ye")
                              if indeks > 30 and indeks < 34.9:
                                    print("Üzgünüm ama obezsin sahip")
                              print("Boy kilo endeksiniz : " , indeks )
                              print("*"*20)
                  else :
                              print("Şimdilik bu kadar \n Hoşçakal" , Name ," :) ")
                              print("Çıkış yapılıyor" )
                              print("*"*20)
            else:

                  LoginCount -= 1 
                  print("Wrong Pass \n" , "\n" , "-" * 20)
      else:
            LoginCount -=1
            print("Wrong Username \n" , "\n ","-" * 20)
else:
      print("Deneme hakkınız dolmuştur.")
UserInfo = [Name , Surname , kilo , boy ]
AsistantInfo = [AsistantName]




