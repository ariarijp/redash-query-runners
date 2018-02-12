# query-results-ex

query-results-ex executes a query to Query Results with Query Parameters.

## Installation

Copy `query_results_ex.py` to `/path/to/redash/redash/query_runner`.

```shell
$ git clone https://github.com/ariarijp/redash-query-runners.git
$ cd redash-query-runners
$ cp query-results-ex/query_results_ex.py /path/to/redash/redash/query_runner/
```

Then, add `redash.query_runner.redash_query` to `REDASH_ADDITIONAL_QUERY_RUNNERS` in `.env` file or something like that.

```
export REDASH_ADDITIONAL_QUERY_RUNNERS="redash.query_runner.query_results_ex"
```

Finally, restart Redash processes.

```
$ sudo service supervisor restart
```

## Usage

### Query format

Below is the query format.

```
SELECT * FROM query_123(foo=bar,baz=123)
```
