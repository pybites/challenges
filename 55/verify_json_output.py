import json
import sys

if len(sys.argv) < 2:
    print(f'Usage: $ python {sys.argv[0]} YOUR_JSON_OUTPUT_FILE')
    sys.exit(1)

json_output_file = sys.argv[1]

with open(json_output_file) as f:
    resp = json.loads(f.read())

    for attr in 'github_repo tasks title version'.split():
        assert attr in resp, f'Attribute {attr} not in JSON output'

    assert len(resp['tasks']) == 100, 'Not 100 tasks in JSON output'

    first_task = resp['tasks'][0]
    last_task = resp['tasks'][-1]
    for attr in 'day activity done'.split():
        assert attr in first_task, f'Attribute {attr} not in first task dict'
        assert attr in last_task, f'Attribute {attr} not in last task dict'

    print('JSON validation done, all good')
