words={}
line="jingle bells jingle bells jingle all the way"
for w in line.lower().split():
    words[w]=words.get(w,0)+1
print(words)
