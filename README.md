# russpelling

## About

* **Synopsis:** Converts prerevolutionary Russian orthography to modern.
* **Developers:** Ingo Boerner and David J. Birnbaum (djbpitt@gmail.com; http://www.obdurodon.org)
* **GitHub:** https://github.com/ingoboerner/russpelling.git

## To install

* Clone with `git clone https://github.com/ingoboerner/russpelling.git`
* Change into **russpelling** subdirectory of main project directory
* Run `python setup.py install`

## To use

	from russpelling import *
	normalize(input_string)
	create_token(input_string)

## Functions

### `normalize(input_string)`

Converts a single string (typically a word token) from old orthography to modern. Example:

	>>> from russpelling import *
	>>> normalize('свѣтъ')
	'свет'

The function is sensitive to string-final position, which is how it recognizes final hard sign and grammatical desinences. This means that in order to normalize a string of several words you need to tokenize the string into individual words (stripping final punctuation) and then normalize each word individually.

### `create_token(input_string)`

The `create_token()` function is intended for use with [CollateX](https://github.com/DiXiT-eu/collatex-tutorial). The argument must be a string, typically a word token, subject to the same pretokenization requirements as the `normalize()` function, described above.

	>>> from russpelling import *
	>>> create_token('свѣтъ')
	{'t': 'свѣтъ', 'n': 'свет'}

To create a list of token dictionary objects for input into CollateX:

	>>> import re
	>>> from russpelling import *
	>>> s = 'Всѣ счастливыя семьи похожи другъ на друга, каждая несчастливая семья несчастлива по-своему.'
	>>> [create_token(word) for word in re.findall('\w+\s*|\W+',s)]
	[{'n': 'Все', 't': 'Всѣ '}, {'n': 'счастливые', 't': 'счастливыя '}, {'n': 'семьи', 't': 'семьи '}, {'n': 'похожи', 't': 'похожи '}, {'n': 'друг', 't': 'другъ '}, {'n': 'на', 't': 'на '}, {'n': 'друга', 't': 'друга'}, {'n': ',', 't': ', '}, {'n': 'каждая', 't': 'каждая '}, {'n': 'несчастливая', 't': 'несчастливая '}, {'n': 'семья', 't': 'семья '}, {'n': 'несчастлива', 't': 'несчастлива '}, {'n': 'по', 't': 'по'}, {'n': '-', 't': '-'}, {'n': 'своему', 't': 'своему'}, {'n': '.', 't': '.'}]
