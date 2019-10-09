# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/5 1:56
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : demo.py


# import win32com.client
#
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("一天什么时候最安全？中午，因为早晚会出事...")

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("明天你好，我叫干不倒！")
# engine.runAndWait()
#
import pyttsx3


def onStart(name):
    print('starting', name)


def onWord(name, location, length):
    print('word', name, location, length)


def onEnd(name, completed):
    print('finishing', name, completed)


engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.',123)
engine.runAndWait()


# import pyttsx3
# def onWord(name, location, length):
#    print('word', name, location, length)
#    if location > 10:
#       engine.stop()
# engine = pyttsx3.init()
# engine.connect('started-word', onWord)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
