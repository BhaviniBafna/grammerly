# import TextBlob
from textblob import TextBlob
correct_me=input("enter the string: ")

a = TextBlob(correct_me)

# using TextBlob.correct() method
a = a.correct()

print(a)
