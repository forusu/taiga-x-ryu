import twitter
from TwitterApi import api
import threading
import string
import random

quotes = ["“Stop ogling her, you sick mutt” - Taiga Aisaka",
         "“Trespassing. And imposed cleaning. This better not be your attempt to mark your territory, stupid dog.” - Taiga Aisaka",
         "“Crying is a nosebleed of the heart.” – Minori Kushieda",
         "“If you trip while running down a hallway, you’ll get a nosebleed. If you trip in life, you’ll cry.” – Minori Kushieda",
         "“Even when the sky’s so dark you can’t see a thing, there are still stars shining out there. So if she can learn to shine brighter, we’ll be able to see her.” – Minori Kushieda",
         "“I don’t want to get so caught up in searching for what I can’t see, that I lose sight of what I can.” – Minori Kushieda",
         "“Adoration never leads to a balanced relationship.” – Ami Kowashima",
         "“As long as there is at least one person who understands me, I’ll be okay.” – Ami Kowashima",
         "“It’s difficult to like me when I’m being myself.” – Ami Kowashima",
         "“I’ll make it so you can stand in front of Kitamura…with your chest puffed out.” – Ryuuji Takasu",
         "“Since ancient times, the dragon has been the only beast to equal the tiger. Even if you’re not by my side right now, I will leap through space and time and always be by your side. These feelings will never change.” – Ryuuji Takasu",
         "“Aisaka! Let me…please let me clean your kitchen!” – Ryuuji Takasu",
         "“Don’t worry. You won’t be completely alone. You’ve got me.” – Kitamura Yusaku",
         "“It doesn’t matter if you grew up without parents, and it doesn’t matter if you don’t believe in God. There’s someone out there watching over you.” – Taiga Aisaka",
         "“It’s not about being right or being wrong. There are more important things than that. That’s why apologies and forgiveness become necessary.” – Taiga Aisaka",
         "“Having someone saying you’re okay as you are and being needed by that person… It was nice to have someone like that.” – Taiga Aisaka",
         "“Entire civilizations were built and destroyed between now and the last time you said “we’ll go soon.” I’ll have rotted and turned to ash by the time this “soon” of yours comes.” – Taiga Aisaka",
         "“Those stars look like they’re close to each other, but they’re actually very far away, aren’t they? It’s like Kitamura-kun and I. The things you see aren’t always real. How hard must I try in order to understand the unseen truth?” – Taiga Aisaka",
         "“Stop living in the past like an old man.” – Taiga Aisaka",
         "“The thing you wished for the most, is something you’ll never get.” – Taiga Aisaka",
         "“I hate waiting, but if waiting means being able to be with you, I’ll wait for as long as forever.” – Taiga Aisaka",
         "“Trespassing. And imposed cleaning. This better not be your attempt to mark your territory, stupid dog.” – Taiga Aisaka",
         "“The lovely angel of romance, Taiga, will lend you her aid.” – Taiga Aisaka",
         "“A dog’s happiness is measured by how useful he is to his master.” – Taiga Aisaka"]
      

old = []
def checklist():
    picked = random.choice(quotes)
    while picked in old:
        picked = random.choice(quotes)
    old.append(picked)
    return picked

def printit():
  threading.Timer(7200.0, printit).start()
  status = api.PostUpdate(checklist() + " #Toradora")
  print(status.text)

printit()
