# yapy-arm64

![PyPI](https://img.shields.io/pypi/v/yapy-arm64)

🐍 Yet Another (ARM) Plagiarism, plagiarism detector for ARM64 source code with Lark

yapy is a tool used to detect and discourage the punishable copying of student exercise programs written in ARM64 (AArch64) for the Fundamentals of Computer Systems and Computer Architecture course units of the Bachelor in Informatics and Computing Engineering at Faculdade de Engenharia da Universidade do Porto.

## Installation with the PyPI package

```bash
pip install yapy-arm64
```

## Overview

yapy uses [Lark](https://lark-parser.readthedocs.io/en/latest/) to build an abstract syntax tree to ARM64 code.

The grammar built only provides the rules necessary for parsing code used with the instructions available for the two courses lectured.

After build the abstract syntax tree, the tree is transformed into a bag of tokens represented as an hash table with the key being each valuable token and the value the number of occurrences of that token.

Finally, the similarity between two files is calculated with Sørensen–Dice coefficient.

### What doest it prevent?

* Comments
* Label name changes
* Register allocation changes
* Adding of redundant instructions
* Switching the order of instructions
* Switching the order of whole block of instructions

## Usage

```python
from yapy import PlagiarismCompare
from yapy.score.similarity_score import sorensen_dice_coefficient

# You could either pass an argument path specifying the path to look for files or pass a list of files with files=[...]
# If no threshold is set the comparison will return the similarity between all files found
p_compare = PlagiarismCompare(path='test/resources/directory', threshold=0.965)
p_compare.compare(sorensen_dice_coefficient)

json_result = p_compare.json_formatter.format_suspicious()
html_result = p_compare.html_formatter.format_suspicious()
csv_result = p_compare.csv_formatter.format_suspicious()

print(json_result) # will actually print all pairs of files with similarity above 0.965
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
