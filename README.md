# HS-Playoff-Deck-Export

A python script for converting Hearthstone deck codes from a csv to deck images.

## Requirements

* Python 3.6+
* [python-hearthstone](https://github.com/hearthsim/python-hearthstone)
* [Python Imaging Library](https://pillow.readthedocs.io)
* [backports.csv](https://pypi.python.org/pypi/backports.csv)
* [Requests](http://docs.python-requests.org)

## Setup

Clone this repository first, then clone the hs-card-tiles repo [https://github.com/HearthSim/hs-card-tiles](https://github.com/HearthSim/hs-card-tiles) within the `decktoimage/` directory.

After this is done, download cards.collectible.json and put it to your resources directory.

```
git clone https://github.com/rikumiyao/HS-Deck-to-Image.git
cd decktoimage
python setup.py
git clone https://github.com/HearthSim/hs-card-tiles
```
When you want to update the tiles, pull from the hs-card-tiles repo:
```
cd decktoimage/hs-card-tiles
git pull origin master
```
If you want to update cards.collectible.json, run the `setup.py` again.

## Usage

```
usage: decktoimage.py [-h] [--ordered] [--code-dest CODE_DEST]
                      [--locale {zhCN,enUS}]
                      {deckcsv,battlefy,smashgg} source destination

Create deck images from a csv file

positional arguments:
  {deckcsv,battlefy,smashgg}
                        The type of source the decklists are from
  source                Where to get the decklists from. For the deckcsv
                        option, specify a csv file in your path. For the other
                        2 options, specify the bracket url of their respective
                        websites
  destination           Where the images are generated

optional arguments:
  -h, --help            show this help message and exit
  --ordered             Set whether images should be grouped by the first
                        letter of the key
  --code-dest CODE_DEST
                        When set, output the deck codes to a csv file instead
  --locale {zhCN,enUS}  The image language
```

## CSV formatting

The first line in the CSV file will be the schema for the rest of the file. It will be a comma separated list of arguments with the same length as the rest of the rows of the file. Leave unused fields blank, and use "K" for keys (which will group the decklists and control what the image file is named as), and "D" for deck codes to be parsed by the script.

For example, a schema of `K,D,D,D,D` in the first line of the csv will indicate that the followings lines have the form "Name/Key, Deck Code #1, Deck Code #2, Deck Code #3, Deck Code #4", which a schema of "K,,D" will indicate the form of "Name/Key, \[Irrelevant\], Deck Code" and the program will group deck codes corresponding to the same key to the same deck image.

If the schema is not specified, a schema of `K,D,D,D,...` will be assumed.

## Example Usage

Example image generated using the following input:
```
K,D,D,D,D
Tredsred#1762,AAECAf0GBO0Fws4Cl9MCzfQCDYoB8gX7BrYH4Qf7B40I58sC8dAC/dACiNIC2OUC6uYCAA==,AAECAaoICCCZAvPCAsLOAqvnAvbsAqfuAs30Agu9AdMB2QfwB7EIkcECrMICm8sClugClO8CsPACAA==,AAECAQcC08MCn9MCDkuRBv8HsgibwgK+wwLKwwLJxwKbywLMzQLP5wKq7AKb8wLF8wIA,AAECAZICAv4BmdMCDkBf/QL3A+YFxAaFCOQIoM0Ch84CmNICntIChOYC1+8CAA==
```
![Tredsred deck image](https://i.imgur.com/PSSrg3f.jpg "Tredsred deck image")

