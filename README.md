# Attrify
**Access python dict keys as attributes**

## Installation

- Install using pip: `pip install attrify`


## Examples

-  Convert normal dict
```python
from attrify import Attrify

normal_dict = {'name': 'Cool'}
attrified_dict = Attrify(normal_dict)
# or
attrified_dict = Attrify(**normal_dict)

assert attrified_dict['name'] == attrified_dict.name
```
-  Convert complex nested dict
```python
complex_nested_normal_dict = {"data": {"results": [{"name": "something"}, {"name": "anything"}]}}
complex_nested_attrified_dict = Attrify(complex_nested_normal_dict)
# or
complex_nested_attrified_dict = Attrify(**complex_nested_normal_dict)

assert complex_nested_attrified_dict.data.results[0].name == complex_nested_normal_dict['data']['results'][0]['name']
```
-  Convert back to dict
```python
normal_dict = {'name': 'Cool'}
attrified_dict = Attrify(normal_dict)
assert type(attrified_dict.to_dict()) == type(normal_dict)
```
-  Keys inside dir: **Will only contain with alphabetic keys, To see which keys are considered alphabetic see `help(str.isalpha)`**
```python
attrified_dict = Attrify({'name': 'Cool'})
print(dir(attrified_dict)) # List return will contain the key 'name'.
```
-  There is also a shortcut method to prettify dict, Just calls json.dumps with some args set.
```python
print(complex_nested_attrified_dict.prettify())
```
