# Tmplt.py [![PyPI Version](http://img.shields.io/pypi/v/tmplt.svg?style=flat)](https://pypi.python.org/pypi/tmplt) [![Build Status](https://img.shields.io/travis/yuanqing/tmplt.py.svg?style=flat)](https://travis-ci.org/yuanqing/tmplt.py) [![Coverage Status](https://img.shields.io/coveralls/yuanqing/tmplt.py.svg?style=flat)](https://coveralls.io/r/yuanqing/tmplt.py)

> Minimal templating for Python.

Straight-up substitution, nothing more. Here&rsquo;s a slightly contrived example:

```py
from tmplt import render

tmpl = '{{ foo }}, {{ baz.qux }}!'
data = {
  'foo': 'Hello',
  'bar': 'World',
  'baz': {
    'qux': lambda d: d['bar']
  }
}
print render(tmpl, data) #=> 'Hello, World!'
```

More usage examples are in [the tests](https://github.com/yuanqing/tmplt.py/blob/master/test/test_tmplt.py).

## API

### tmplt.render(tmpl, data)

Interpolates values from the `data` object into the `tmpl` string.

- `tmpl` is a `string` with tags enclosed in double braces. Use a dot-delimited tag to reference nested values in `data`.

- `data` can be a `dict`, `list`, or `tuple`, with arbitrary nesting. If a lambda or function in `data` is referenced in `tmpl`, it will be invoked, and its return value will be substituted into `tmpl`. The lambda or function takes a single argument, namely the `data` object itself.

## Installation

Install via [pip](https://pypi.python.org/pypi/tmplt):

```bash
$ pip install tmplt
```

## License

[MIT license](https://github.com/yuanqing/tmplt.py/blob/master/LICENSE)
