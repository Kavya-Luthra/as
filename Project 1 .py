import pyttsx3 as tt

print("""                                                                                      HELLO USERS
                                                                                 I'm Khalkhanda AI Boat""")

engine = tt.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

engine.say(" Hello users. My name Khalkhanda, and I'm a AI boat. I am text reader for blind people. ")
engine.runAndWait()

engine.say('Please enter you name')
engine.runAndWait()

a = input("Enter you name : ")
print('')
print('Hello ',a)

engine.say('hello' + a)
engine.runAndWait()

print('')
engine.say('Please enter your text')
engine.runAndWait()
b = input('Please enter your text :')
print('')

print(a ,",are you blind? If not, then why are you using me? This is only for blind people.")
engine.say(a + ",are you blind? If not, then why are you using me? This is only for blind people.")
engine.runAndWait()