with open("story.txt","r") as f:
    story=f.read()
print(story)

words=set()

target_start='<'
target_end='>'
start_of_word=-1

for i,char in enumerate(story):
    if char==target_start:
        start_of_word=i
    if char==target_end and start_of_word!=1:
        word=story[start_of_word:i+1]
        words.add(word)
        start_of_word=-1
# print(words)
answers={}

for word in words:
    new_word=input("Enter the new word for "+word+" : ")
    answers[word]=new_word
# print(answers)

for word in words:
    story=story.replace(word,answers[word])


    
print(story)
