import unittest

from fast_arrow import Option
from tests.test_util import gen_vcr, gen_client


class TestOption(unittest.TestCase):

    def test_fetch_fields(self):
        client = gen_client()
        option_id = "e03e7414-527d-4b44-a081-c61aeb474060"
        with gen_vcr().use_cassette("option_fetch.yaml"):
            option = Option.fetch(client, option_id)

            expected_fields = [
                'issue_date', 'tradability', 'strike_price', 'state', 'url',
                'expiration_date', 'created_at', 'chain_id', 'updated_at',
                'rhs_tradability', 'type', 'chain_symbol', 'min_ticks', 'id']

            actual_fields = list(option.keys())

            assert(set(expected_fields) == set(actual_fields))
