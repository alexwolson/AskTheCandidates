import nltk, os, markovify, re
from random import randint

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

def full_corpus_Trump():
	models = []
	for file in os.listdir("./Trump/"):
		if file.endswith(".speech"):
			with open("./Trump/" + file) as f:
				text = f.read()
			models.append(markovify.Text(text))
	model_combo = markovify.combine(models)
	sentence = model_combo.make_sentence()
	#print 'TRUMP: ' + sentence
	return sentence

def full_corpus_Clinton():
	models = []
	for file in os.listdir("./Clinton/"):
		if file.endswith(".speech"):
			with open("./Clinton/" + file) as f:
				text = f.read()
			models.append(markovify.Text(text))
	model_combo = markovify.combine(models)
	sentence = model_combo.make_sentence()
	#print 'CLINTON: ' + sentence
	return sentence


def debate():
	output = ""
	sentence = full_corpus_Trump()
	for x in range(randint(5,10)):
		for y in range(randint(1,3)):
			tw = nltk.word_tokenize(sentence)
			tt = nltk.pos_tag(tw)
			nouns = [item[0] for item in tt if item[1][0] == 'N']
			if nouns == []:
				sentence = full_corpus_Clinton()
			else:
				#idx = nltk.text.ContextIndex([word.lower() for word in 	nltk.corpus.brown.words()])
				save = []
				for word in nouns:
					save.append(word)
					#similar = 	idx.similar_words(word)	
					#for item in similar:
					#	save.append(str(item))
				lines = []
				for file in os.listdir("./Clinton/"):
					if file.endswith(".speech"):
						with open("./Clinton/" + file) as f:
							text = f.readlines()
					for i, line in enumerate(text):
						if any(q in line for q in save):
							lines.append(line)
				if lines == []:
					sentence = full_corpus_Clinton()
				else:
					models = []
					for line in lines:
						models.append(markovify.Text(line))
					model_combo = markovify.combine(models)
					sentence = model_combo.make_sentence()
					try:
						output_t = "CLINTON: " + sentence + '\n'
					except:
						return output
					output += output_t
		for y in range(randint(1,3)):
			tw = nltk.word_tokenize(sentence)
			tt = nltk.pos_tag(tw)
			nouns = [item[0] for item in tt if item[1][0] == 'N']
			if nouns == []:
				sentence = full_corpus_Trump()
			else:
				#idx = nltk.text.ContextIndex([word.lower() for word in 	nltk.corpus.brown.words()])
				save = []
				for word in nouns:
					save.append(word)
				#	similar = idx.similar_words(word)
				#	for item in similar:
				#		save.append(str(item))
				lines = []
				for file in os.listdir("./Trump/"):
					if file.endswith(".speech"):
						with open("./Trump/" + file) as f:
							text = f.readlines()
					for i, line in enumerate(text):
						if any(q in line for q in save):
							lines.append(line)
				if lines == []:
					sentence = full_corpus_Trump()
				else:
					models = []
					for line in lines:
						models.append(markovify.Text(line))
					model_combo = markovify.combine(models)
					sentence = model_combo.make_sentence()
					try:
						output_t = "TRUMP: " + sentence + '\n'
					except:
						return output
					output += output_t
	
