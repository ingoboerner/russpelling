from russpelling import *
from collatex import *
import re
collation = Collation()
with open('texts/ak_old.txt','r') as stuff:
    old = stuff.read()
with open('texts/ak_new.txt', 'r') as stuff:
    new = stuff.read()
collation = Collation()
tokens_old = [create_token(word) for word in re.findall('\w+\s*|\W+',old)]
tokens_new = [create_token(word) for word in re.findall('\w+\s*|\W+',new)]
witness_old = {'id': 'old', 'tokens': tokens_old}
witness_new = {'id': 'new', 'tokens': tokens_new}
witnesses = [ witness_old, witness_new]
collation_input = {'witnesses' : witnesses}
collate(collation_input, output="html2", segmentation=False)
