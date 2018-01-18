import csv as csv
import json

from redash.query_runner import BaseQueryRunner, register


class CsvParser(BaseQueryRunner):
    @classmethod
    def name(cls):
        return 'CSV Parser (Unofficial)'

    @classmethod
    def configuration_schema(cls):
        return {
            'type': 'object',
            'properties': {
                'delimiter': {
                    'type': 'string',
                    'title': 'Delimiter',
                    'default': ',',
                },
            },
        }

    @classmethod
    def annotate_query(cls):
        return False

    def __init__(self, configuration):
        super(CsvParser, self).__init__(configuration)

    def test_connection(self):
        pass

    def run_query(self, query, user):
        query = query.strip()
        delimiter = str(self.configuration.get('delimiter'))

        columns = []
        rows = []
        for row in csv.DictReader(query.splitlines(), delimiter=delimiter):
            if len(columns) == 0:
                for key in row.keys():
                    columns.append({'name': key, 'friendly_name': key})

            rows.append(row)

        return json.dumps({'columns': columns, 'rows': rows}), None


register(CsvParser)
