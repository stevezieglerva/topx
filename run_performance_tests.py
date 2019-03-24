import nltk
from nltk.corpus import brown
from TopX import *
from collections import Counter
from TimerCollection import *

timer = TimerCollection()

brown_text_words = brown.words()
print("NLTK Brown corpus word count: {}".format(len(brown_text_words)))

timer.start_timer("Counter")
counter = Counter(brown_text_words)
timer.end_timer("Counter")
print("Counter most common: {}".format(counter.most_common(10)))

timer.start_timer("TopX")
word_counts = {}
for word in brown_text_words:
	if word in word_counts:
		word_counts[word] =  word_counts[word]  + 1
	else:
		word_counts[word] = 1

top = TopX(10)
for word in word_counts:
	pair = (word_counts[word], word)
	top.add(pair)
timer.end_timer("TopX")

reverse_result = ""	
for pair in top.values:
	reverse = "('{}', {}), ".format(pair[1], pair[0])
	reverse_result = reverse_result + reverse 
print("TopX               : {}".format(counter.most_common(10)))



timer.print_results()
