import pyttsx

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-60)
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

# Voices

#voices = engine.getProperty('voices')
#i = 0
#for voice in voices:
#    i = i + 1
#    print "Voice %i de %i" % (i, len(voices) )
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')

engine.runAndWait()
   