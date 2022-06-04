from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
import math
nltk.download('stopwords')
	
#linked list (dictionary tp store our posting list) 
dict = {}
freq_doc={}
total_number_of_words=[]
#my documents names list
myDocuments=["WebPage1.txt","WebPage2.txt","WebPage3.txt"]

for i in range(len(myDocuments)):
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

	#we will create the frequency dictionary 

	for word in text_tokens:	
		if (word not in freq_doc):
			freq_doc[word]=[0,0,0,0]
			freq_doc[word][i]+=1
		else:

			freq_doc[word][i]+=1
		
	
	tokens_without_sw = [
	    word for word in text_tokens if not word in stopwords.words()]

	total_number_of_words.append(len(text_tokens))
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

# IDF: log(Total number of sentences (documents))/(Number of sentences (documents) containing the word)
def IDF(word):
	return math.log10((len(myDocuments)+1)/(len(dict[word])+1))+1

# tf=(count in which word will appear in the document/ count of all tokenized words)

def TF(word,frequency_dict):
	tf_list=[]	
	if (word in frequency_dict):
		for i in range(len(myDocuments)):
			tf_list.append(frequency_dict[word][i]/total_number_of_words[i])
	return tf_list


def TF_IDF(word):
	idf=IDF(word)
	list=[]
	for weight in TF(word,freq_doc):
		list.append(weight*idf)
	return list

#calculating TF-IDF
try: 
	if (len(words_list)==1):
		print("TF-IDF of the word "+str(words_list[0])+" is: ")
		print((TF_IDF(words_list[0])))
	elif (len(words_list)==2):
		print("TF-IDF of the word "+str(words_list[0])+" is: ")
		print((TF_IDF(words_list[0])))
		print("TF-IDF of the word "+str(words_list[1])+" is: ")
		print((TF_IDF(words_list[1])))
	elif (len(words_list)==3):
		print("TF-IDF of the word "+str(words_list[0])+" is: ")
		print((TF_IDF(words_list[0])))
		print("TF-IDF of the word "+str(words_list[1])+" is: ")
		print((TF_IDF(words_list[1])))
		print("TF-IDF of the word "+str(words_list[2])+" is: ")
		print((TF_IDF(words_list[2])))
except:
	print("Something went wrong")
