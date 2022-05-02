from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
	
#linked list (dictionary tp store our posting list) 
dict = {}
#my documents names list
myDocuments=["WebPage1.txt","WebPage2.txt","WebPage3.txt","WebPage4.txt"]

for i in range(4):
	file = open(myDocuments[i], encoding='utf8')
	read = file.read()
	file.seek(0)

	#define punctuations to remove from the text
	punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
	for item in read:  
	    if item in punc:  
	        read = read.replace(item, " ") 
	         	  
	# make every word lower to be able to compare
	read=read.lower()

	#my tokenization process(using nltk library)
	#i also remove all stopwords from the text

	text_tokens = word_tokenize(read)
	  
	tokens_without_sw = [
	    word for word in text_tokens if not word in stopwords.words()]

	# create a linked list from my tokenzed text
	# list will be done like that {"term1":[docID1, docID2], "term2":[docID]}
	for item in tokens_without_sw:
	    if item not in dict:
	        dict[item] = [i+1]
	    else:
	    	if i+1 not in dict[item]:
	    		dict[item].append(i+1)

# main query creation
query=input("Please enter your query ('AND' between keys): ")

words_list1 = query.split("AND")
words_list=[]
for word in words_list1:
	words_list.append(word.strip())

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
except:
	print("Something went wrong")


