#import libraries
from textblob import TextBlob
import nltk
from newspaper import Article

#Get the article
url='https://nmit.ac.in'
article=Article(url)

#do some proceesing
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

#get the summary
text=article.summary
print(text)

#create a textblob object 
obj=TextBlob(text)

#this returns a value between 1 and -1
sentiment=obj.sentiment.polarity
print(sentiment)

if sentiment==0:
	print("NEUTRAL")
elif sentiment > 0:
	print("POSITIVE")
else:
	print("NEGATIVE")
