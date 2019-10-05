## Code Challenge 45 - TDD: Code FizzBuzz Writing Tests First!

![Python version][python-version]

I spent some time for this Code Challenge reviewing the #100daysofcode Pytest section and then set about writing my own fizzbuzz pytest code from scratch. 

I also invoked pytest-cov from the CLI and experimented proving to myself that this only gives test coverage of the methods used and not the unique input parametrised tests from integer inputs 1 through to 100. 

I use Mike Kennedy's design pattern of defining a main() under ``` 
if __name__ == '__main__':
``` and wondered if I should be testing this - how else can I get 100% test coverage, and is this important enough? (Feedback welcome!)


### Python Packages used:
pytest==5.2.0  
pytest-cov==2.8.0

[python-version]:https://img.shields.io/badge/python-3.7.3-brightgreen.svg

