import re

import spacy
from daterangeparser import parse

nlp = spacy.load('en_core_web_sm')
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
    for sent in doc.sents:
        for ent in filter(lambda e: e.label_ == 'DATE', list(sent.ents)):
            try:
                (start, end) = parse(ent.text)
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
                events = events + [(start, ent.text, desc)]
    return events
