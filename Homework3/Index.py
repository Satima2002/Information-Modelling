from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
	 
dict = {}
myDocuments=["WebPage1.txt","WebPage2.txt","WebPage3.txt","WebPage4.txt"]
for i in range(4):
	file = open(myDocuments[i], encoding='utf8')
	read = file.read()
	file.seek(0)

	#create a list to store each line 
	array = []
	
	#define punctuations to remove from the text
	punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	for ele in read:
	    if ele in punc:  
	    	read = read.replace(ele,"")

	# make every word lower to be able to compare
	read=read.lower()
	array.append(read)

	#creating my bigram
	bigrams_list = [b for l in array for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]

	for item in bigrams_list:
	    if item not in dict:
	        dict[item] = [i+1]
	    else:
	    	if i+1 not in dict[item]:
	    		dict[item].append(i+1)

query=input("Please enter your query phrase: ")
words_list1 = query.split("AND")
words_list=[]

# as the key value i will convert my phrase to tuple
for word in words_list1:
	words_list.append(tuple(map(str, word.strip().split(' '))))
print(words_list)

word_found_doc=[]
try:
	#print out the docID's of each query key
	for word in words_list:
		if word in dict:
			word_found_doc.append(dict[word])
			print("The word "+str(word)+" is found in the document ID "+str(dict[word]))

	#I used intersection of sets for boolean model
	if (len(words_list)==2):
		both=list(set(word_found_doc[0]) & set(word_found_doc[1]))
		if(len(both)>0):
			print("Both words appear in "+str(both))
	if (len(words_list)==3):	
		all=str(list(set(word_found_doc[0]) & set(word_found_doc[1])) & set(word_found_doc[2]))
		if (len(all)>0):
			print("All words appear in "+ str(all))	
	if (len(words_list)==0):
		print("Your word is not found in any document")
	if (len(words_list)==1 and len(word_found_doc)==0):
		print("No document was found")
except:
	print("Something went wrong")



