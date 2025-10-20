from transformers import pipeline, __version__ as tfv
print("transformers:", tfv)  # should be >= 4.11

ner = pipeline(
    task="token-classification",              # "ner" also ok
    model="dslim/bert-base-NER",
    aggregation_strategy="simple",            # forces merging of ##pieces
    device=-1                                 # CPU
)

text = "JLau the young goat is a machine learning engineer skilled in Python and NLP."
ents = ner(text)
for e in ents:
    e["score"] = float(e["score"])
print(ents)