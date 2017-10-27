# NLP

raw_data_source: [cornell movie-dialogs corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)

## json file format:
### prenlp_{i}.json

* ```i = 0-30```
* Parsed from ```movie_lines.txt```

 format of movie_lines.txt:
 fields: 
 ```lineID, characterID, movieID, character name, text of the utterance```
```
 # each json file contain 10000 lines, ttl 304713 lines
 'lineID':{
 	'cname':character name,
	'uid: characterID,
	'mid': movieID,
	'lid': lineID,
	'sentences': [sentences_list]
		each element in [sentences_list]:{
			'tokens': [tokens_list],
				each element in [tokens_list]:{
					'after': the character right after this word,
					'before': the character right before this word,
					'characterOffsetBegin': num of starting  offset in this sentence,
					'characterOffsetEnd': num of ending offset in this sentence,
					'index': sequence num of this text in this sentence (start with 1),
					'originalText': original text in the line,
					'pos': part of speech,
					'word': #looks like the same as original text
				}
			'index': element index for sentence_list,
			'parse': parse_tree,
			'basicDependencies': [basicDependencies_list],
				each element in basicDependencies_list:{
					'dep': ?,
					'dependent':seems the sequence num of this word,
					'dependentGloss': the word,
					'governor': ?,
					'governorGloss': relate to word
				}
			'enhancedDependencies': same as basic one,
			'enhancedPlusPlusDependencies': same as basic one
		}
}
```
### word_bank.json
```
#ttl 55382 words
'word':{
	'dfi': num of line_id contains this word,
	'pos': part of speech,
	'word': the word\
}
```
