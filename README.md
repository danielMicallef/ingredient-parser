# Ingredient Parser

## Description

Ingredient Parser is a simple utility to parse ingredients and return their name and measure. It currently supports swedish and english language ingredients.

## Installation

If you already have [Python](http://www.python.org/) and [pip](http://www.pip-installer.org/) on your system you can install the library simply by running:

    pip install ingredient_parser

## Usage

### For English Language
```python
from ingredient_parser.en import parse
print(parse('2 liters of milk'))
```

### For Swedish Language
```python
from ingredient_parser.sw import parse
print(parse('4 Port fisk'))
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


