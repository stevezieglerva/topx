# topx
Python code to return top N occurences of a string in a dictionary. Uses a heap to be faster than Counter in some cases.

Based on the analysis from [Simple Counters in Python (with Benchmarks)](http://evanmuehlhausen.com/simple-counters-in-python-with-benchmarks/) that showed that Counters can be slower than pure dictionary objects.


## Installation
```
pip install -r requirements.txt
```

## Usage
```
>>> from TopX import *
>>> top_three_values = TopX(2)
>>> top_three_values.add((100, "hello"))
>>> top_three_values.add((50, "goodbye"))
>>> top_three_values.add((90, "world"))
>>> top_three_values.add((75, "appler"))
>>> print(top_three_values.values)
[(100, 'hello'), (90, 'world')]
```

print(top_three_values.values)

## Performance tests 
```
python run_performance_tests.py
```



## Results
```
NLTK Brown corpus word count: 1161192
Counter most common: [('the', 62713), (',', 58334), ('.', 49346), ('of', 36080), ('and', 27915), ('to', 25732), ('a', 21881), ('in', 19536), ('that', 10237), ('is', 10011)]
TopX               : [('the', 62713), (',', 58334), ('.', 49346), ('of', 36080), ('and', 27915), ('to', 25732), ('a', 21881), ('in', 19536), ('that', 10237), ('is', 10011)]
______________________________
TopX                            - 4.548
Counter                         - 4.457
```
