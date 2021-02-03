import random
import re

import spacy
from daterangeparser import parse

nlp = spacy.load('en_core_web_md')
p = re.compile(r'\[\d+\]')


def dep_subtree(token, dep):
    child = next(filter(lambda c: c.dep_ == dep, token.children), None)
    if child != None:
        return ' '.join([c.text for c in child.subtree])
    else:
        return ''


def extract_events(text):
    line = p.sub('', text)
    line = line.replace(',', '').replace('.', '').replace('\n', '').replace('\\', '').replace('/', '').replace('\'', '')
    events = []
    doc = nlp(line)
    last_year = None
    for sent in doc.sents:
        for ent in filter(lambda e: e.label_ == 'DATE', list(sent.ents)):
            try:
                (start, end) = parse(ent.text)
                match = re.match(r'.*([1-3][0-9]{3})', ent.text)
                if match is not None:
                    last_year = match.group(1)
                else:
                    if last_year is not None:
                        start = start.replace(year=int(last_year))
            except:
                continue
            current = ent.root
            while current.dep_ != 'ROOT':
                current = current.head
            desc = " ".join(filter(None, [
                dep_subtree(current, "nsubj"),
                dep_subtree(current, "nsubjpass"),
                dep_subtree(current, "auxpass"),
                dep_subtree(current, "amod"),
                dep_subtree(current, "det"),
                current.text,
                dep_subtree(current, "acl"),
                dep_subtree(current, "dobj"),
                dep_subtree(current, "attr"),
                dep_subtree(current, "advmod")]))
            if len(desc.split(' ')) > 4:
                events = events + [(start, ent.text, desc, random.randint(0, 1000000000), random.randint(0, 1000000),
                                    random.randint(0, 10000))]
    return events
