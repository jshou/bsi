bsi
===

Python module for reading/editing/writing .bsi files. See
[http://bitsquid.blogspot.com/2009/10/simplified-json-notation.html](http://bitsquid.blogspot.com/2009/10/simplified-json-notation.html) for
documentation on the format.

Setup
-----

1. Install requirements: `pip install -r requirements.txt
2. Run tests: `nosetests`

Installation
------------

1. To install, run `python setup.py install`


Example Usage
-------------

```python
import bsi

data = open("filename.bsi", 'r').read()
bsi_object = bsi.bsi_parse(data)

print bsi_object.get('zombie1')
```

Disclaimer
----------

This is not a polished product and will need some work in order to be easier to
work with. For example, the BsiArray class should implement an iterator. I'll
gladly accept pull requests!
