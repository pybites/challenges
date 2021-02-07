import pytest
from marvel import get_api_endpoint

@pytest.mark.parametrize('endpoint, id, extra, expected_output',
                         [('comics', 45, 'books',
                           'Invalid value for endpoint or extra'),
                          ('fruit', 23, 'events',
                           'Invalid value for endpoint or extra')])
def test_get_api_endpoint_invalid_pararms(endpoint, id, extra, expected_output, capfd):
    with pytest.raises(ValueError):
        get_api_endpoint(endpoint, id, extra)
