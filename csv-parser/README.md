# csv-parser

csv-parser parses Character-Separated Values as Redash Results.

## Installation

At first, copy `csv_parser.py` to `/path/to/redash/redash/query_runner`.

```shell
$ git clone https://github.com/ariarijp/redash-query-runners.git
$ cd redash-query-runners
$ cp csv-parser/csv_parser.py /path/to/redash/redash/query_runner/
```

Then, add `redash.query_runner.csv_parser` to `REDASH_ADDITIONAL_QUERY_RUNNERS` in `.env` file or something like that.

```
export REDASH_ADDITIONAL_QUERY_RUNNERS="redash.query_runner.csv_parser"
```

Finally, restart Redash processes.

```
$ sudo service supervisor restart
```

## Usage

### Data Source options

All options are required.

* Delimiter
  * e.g. `,`

### Query format

Below is the query format.

```
SepalLength,SepalWidth,PetalLength,PetalWidth,Name
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3.0,1.4,0.2,Iris-setosa
4.7,3.2,1.3,0.2,Iris-setosa
4.6,3.1,1.5,0.2,Iris-setosa
5.0,3.6,1.4,0.2,Iris-setosa
5.4,3.9,1.7,0.4,Iris-setosa
4.6,3.4,1.4,0.3,Iris-setosa
5.0,3.4,1.5,0.2,Iris-setosa
4.4,2.9,1.4,0.2,Iris-setosa
4.9,3.1,1.5,0.1,Iris-setosa
5.4,3.7,1.5,0.2,Iris-setosa
4.8,3.4,1.6,0.2,Iris-setosa
4.8,3.0,1.4,0.1,Iris-setosa
4.3,3.0,1.1,0.1,Iris-setosa
```