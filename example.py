from tmplt import render

tmpl = '{{ foo }}, {{ baz.qux }}!'
data = {
  'foo': 'Hello',
  'bar': 'World',
  'baz': {
    'qux': lambda d: d['bar']
  }
}
print render(tmpl, data)
