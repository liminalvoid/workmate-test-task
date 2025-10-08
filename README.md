# workmate-test-task

Generates reports based on data provided in CSV files.

![Executed script](1.png)

## Installation

Create and enter virtual environment

```bash
# macOS
python3 -m venv env && source ./env/bin/activate
```

Install required dependencies

```bash
pip install -r requirements.txt
```

Run script

```bash
python3 main.py -f ../data/products1.csv ../data/products2.csv -r average-rating average-price
```

## Usage

```bash
usage: products-parser [-h] [-f FILES [FILES ...]] [-r REPORT [REPORT ...]]

Parses CSV and produces reports about some products

options:
  -h, --help            show this help message and exit
  -f, --files FILES [FILES ...]
                        path to files
  -r, --report REPORT [REPORT ...]
                        report type
```
