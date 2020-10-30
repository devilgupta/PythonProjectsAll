introString=input("Enter your introduction:")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
   # wordCount=wordCount+1
    if(i==' '):
        wordCount=wordCount+1
print("Number of Words in the string:-")
print(wordCount)
print("Number of Characters in the string:-")
print(characterCount)
