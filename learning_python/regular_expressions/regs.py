
import pandas as pd
import re


def normalise(text):
    text = re.sub('.[{}]'format(re.escape('",$!@#$%^&*()')), ' ', text.strip())  # Remove special characters
    text = re.sub(r'\s+', ' ', text)        # Convert multiple whitespace into a single space
    return text

fieldnames = ['title', 'abstract', 'keywords', 'general_terms', 'acm_classification']
df = pd.read_csv('xa.tsv', delimiter='\t', usecols=fieldnames, dtype='object', na_filter=False)
df = df.applymap(normalise)
print(df)
