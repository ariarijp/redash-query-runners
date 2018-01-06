import urlparse

import requests

from redash.query_runner import BaseQueryRunner, register
from redash.utils import json_dumps

try:
    from redash_dynamic_query import RedashDynamicQuery

    enabled = True
except ImportError:
    enabled = False


class RedashQuery(BaseQueryRunner):
    @classmethod
    def name(cls):
        return 'Redash Query (Unofficial)'

    @classmethod
    def enabled(cls):
        return enabled

    @classmethod
    def annotate_query(cls):
        return False

    def test_connection(self):
        pass

    @classmethod
    def configuration_schema(cls):
        return {
            'type': 'object',
            'properties': {
                'base_url': {
                    'type': 'string',
                    'title': 'Redash URL',
                },
                'api_key': {
                    'type': 'string',
                    'title': 'Redash User API Key',
                },
                'data_source_id': {
                    'type': 'number',
                    'title': 'Data Source ID',
                },
            },
            'required': [
                'base_url',
                'api_key',
                'data_source_id',
            ],
            'order': [
                'base_url',
                'api_key',
                'data_source_id',
            ],
            'secret': ['api_key'],
        }

    def run_query(self, query, user):
        base_url = self.configuration.get('base_url', None)
        api_key = self.configuration.get('api_key', None)
        data_source_id = self.configuration.get('data_source_id', None)
        query = query.strip()

        parsed_query = urlparse.urlparse(query)
        query_id = parsed_query.path
        params = {k: v[0] for k, v in urlparse.parse_qs(parsed_query.query).items()}

        try:
            client = RedashDynamicQuery(endpoint=base_url,
                                        apikey=api_key,
                                        data_source_id=data_source_id)
            results = client.query(query_id, params)

            return json_dumps(results['query_result']['data']), None
        except requests.RequestException as e:
            return None, str(e)
        except KeyboardInterrupt:
            return None, 'Query cancelled by user.'


register(RedashQuery)
