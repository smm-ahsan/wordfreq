# WordFreq

A tiny command line tool that counts word frequency and keyword density in any text, for writers and SEO checks.

Keyword density is how often a word appears as a percentage of the total words in a text.

## Requirements

- Python 3
- Standard library only, nothing to install

## Usage

Analyse text directly:

```bash
python3 wordfreq.py --text "the cat sat on the mat the cat ran and the dog ran too" --top 3
```

Exclude common English stopwords like "the" and "and":

```bash
python3 wordfreq.py --text "the cat sat on the mat the cat ran and the dog ran too" --stopwords --top 3
```

Analyse a file instead, show the top 20 words, ignore one and two letter words:

```bash
python3 wordfreq.py --file article.txt --top 20 --min-length 3
```

Exactly one of `--text` or `--file` is required. Words are ranked by count, with ties broken alphabetically, and each line shows the count and its density percentage.

See [examples.md](examples.md) for real captured output.

## License

MIT - see [LICENSE](LICENSE).
