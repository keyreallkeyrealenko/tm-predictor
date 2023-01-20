# Description

This repository allows you to predict **tm-index** of proteins written in .fasta file.
It works as parser of http://tm.life.nthu.edu.tw/index.htm web open tool (DOI: 10.1016/j.compbiolchem.2009.10.002).
As a result, you get 1) barplots of predicted categories 2) JSON-files describe each protein, groups. 

## Installation



1) Clone this repo:
```commandline
git clone https://github.com/keyreallkeyrealenko/tm-predictor.git
```

2) Open directory:

```commandline
cd tm-predictor
```

3) Create and activate new python environment:

```commandline
python3.9 -m venv venv
source venv/bin/activate
```

3) Install all required python libraries:
```commandline
pip install -r requirements.txt
```

4) Make **main.py** executable (optional):

```commandline
chmod +x main.py
```

###__NOTE__:
selenium webdriver must be installed on your machine. E.g. see here: https://selenium-python.readthedocs.io/installation.html#

## Usage and example:

Code below would parse file example.fasta from current directory and save all the results to ~/Desktop directory
```commandline
python3 main.py example.fasta ~/Desktop/
```

## Notes:

program was tested on macOS Monterey V 12.6. Should work on any UNIX-machine too 
