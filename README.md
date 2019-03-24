# topx
Python code to return top N occurences of a string in a dictionary. Uses a heap to be faster than Counter in some cases.


## Installation
```
pip install -r requirements.txt
```

## Execution
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
