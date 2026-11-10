# Examples

Real output from WordFreq, captured from actual runs.

## Top 3 words in a short text

Command:

```bash
python3 wordfreq.py --text "the cat sat on the mat the cat ran and the dog ran too" --top 3
```

Output:

```
Total words: 14
Unique words: 9
1. the - 4 (28.6%)
2. cat - 2 (14.3%)
3. ran - 2 (14.3%)
```

## Same text with stopwords excluded

Common words like "the", "on" and "and" are dropped before counting, so the content words stand out:

Command:

```bash
python3 wordfreq.py --text "the cat sat on the mat the cat ran and the dog ran too" --stopwords --top 3
```

Output:

```
Total words: 8
Unique words: 6
1. cat - 2 (25.0%)
2. ran - 2 (25.0%)
3. dog - 1 (12.5%)
```
