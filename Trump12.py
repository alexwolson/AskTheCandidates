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

def gen_sentences(sen, model):
    result = ""
    for i in range(sen):
        result += (model.make_sentence()) + '\n'
    return result

def full_corpus_trump():
	models = []
	for file in os.listdir("./Trump/"):
		if file.endswith(".speech"):
			with open("./Trump/" + file) as f:
				text = f.read()
			models.append(markovify.Text(text))
	model_combo = markovify.combine(models)
	return gen_sentences(randint(1,3), model_combo)

def full_corpus_clinton():
	models = []
	for file in os.listdir("./Clinton"):
		if file.endswith(".speech"):
			with open ("./Clinton/" + file) as f:
				text = f.read()
			models.append(markovify.Text(text))
	model_combo = markovify.combine(models)
	return gen_sentences(randint(1,3), model_combo)

def trump_respond(text):
        output = ""
	tw = nltk.word_tokenize(text)
	tt = nltk.pos_tag(tw)
	nouns = [item[0] for item in tt if item[1][0] == 'N']
	if nouns == []:
		output = full_corpus_trump()
	else:
		#idx = nltk.text.ContextIndex([word.lower() for word in 	nltk.corpus.brown.words()])
		save = []
		for word in nouns:
			save.append(unicode(word))
			#similar = idx.similar_words(word)
			#for item in similar:
			#	save.append(item)
		lines = []
		for file in os.listdir("./Trump/"):
			if file.endswith(".speech"):
				with open("./Trump/" + file) as f:
					text = f.readlines()
			for i, line in enumerate(text):
				#if any(q in line for q in save):
				if set(line).intersection(save) != set([]):
					lines.append(line)
		if lines == []:
			output = full_corpus_trump()
		else:
			models = []
			for line in lines:
				models.append(markovify.Text(line))
			model_combo = markovify.combine(models)
			output = gen_sentences(randint(1,3), model_combo)
	return output.decode('utf-8', 'ignore')

def clinton_respond(text):
        output = ""
	tw = nltk.word_tokenize(text)
	tt = nltk.pos_tag(tw)
	nouns = [item[0] for item in tt if item[1][0] == 'N']
	if nouns == []:
		output = full_corpus_clinton()
	else:
		#idx = nltk.text.ContextIndex([word.lower() for word in nltk.corpus.brown.words()])
		save = []
		for word in nouns:
			save.append(unicode(word))
			#similar = idx.similar_words(word)
			#for item in similar:
			#	save.append(item)
		lines = []
		for file in os.listdir("./Clinton/"):
			if file.endswith(".speech"):
				with open("./Clinton/" + file) as f:
					text = f.readlines()
			for i, line in enumerate(text):
				if set(line).intersection(save) != set([]):
					lines.append(line)
		if lines == []:
			output = full_corpus_clinton()
		else:
			models = []
			for line in lines:
				models.append(markovify.Text(line))
			model_combo = markovify.combine(models)
			output = gen_sentences(randint(1,3), model_combo)
	return output.decode('utf-8', 'ignore')

