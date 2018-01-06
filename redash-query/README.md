# redash-query

redash-query executes a query to Redash Query.

## Installation

At first, install `redash-dynamic-query` on your Redash server.

```shell
$ sudo pip install redash-dynamic-query
```

Then, copy `redash_query.py` to `/path/to/redash/redash/query_runner`.

```shell
$ git clone https://github.com/ariarijp/redash-query-runners.git
$ cd redash-query-runners
$ cp redash-query/redash_query.py /path/to/redash/redash/query_runner/
```

Then, add `redash.query_runner.redash_query` to `REDASH_ADDITIONAL_QUERY_RUNNERS` in `.env` file or something like that.

```
export REDASH_ADDITIONAL_QUERY_RUNNERS="redash.query_runner.redash_query"
```

Finally, restart Redash processes.

```
$ sudo service supervisor restart
```

## Usage

### Data Source options

All options are required.

* Redash URL
  * e.g. http://localhost
* Redash User API Key
  * e.g. abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN
* Data Source ID
  * e.g. 3

### Query format

Below is the query format.

```
query_id
```

Also, you can execute a query with parameters.

```
query_id?key1=value1&key2=value2...
```
