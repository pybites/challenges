## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Usage](#usage)

## General info
This is twitter api which is implemented in Flask, a python framework.
Case study, Code Challenge #41, taken from @python_tip, pybites community. (http://pybit.es/codechallenge41.html)
This api has a basic page in order to use crud operations

## Technologies
Created with:
* Python, Flask Framework

## Notes
- To find similarity between tips SequenceMatcher lib is used to match

## Usage
Optional - To run in a virtual environment run to create an environment: virtualenv <env_name>
         - Copy files into environment directory

1. cd into project directory
2. run "pip install -r requirements.txt" in the same directory of src folder
3. set api keys (consumer_key, consumer_secret, access_token, access_token_secret) in environment
4. run "python src/tip_manager.py"

```python
    python src/tip_manager.py
```