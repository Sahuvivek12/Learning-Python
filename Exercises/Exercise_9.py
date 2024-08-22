# Shoutouts to everyone

import win32com.client as w

speaker = w.Dispatch('SAPI.SpVoice')


l = ['vivek', 'harry', 'shubham']

for i in range (len(l)):
    speaker.Speak(f"Shoutout to {l[i]}")

# Done