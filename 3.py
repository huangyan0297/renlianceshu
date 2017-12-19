# -*- coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import pyttsx

for line in open("out.txt"):
    print line

engine = pyttsx.init()
engine.say(line)
engine.runAndWait()
# 朗读一次
engine.endLoop()
