# Copyright (c) 2021 DragSama
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import json

from typing import Tuple, List, Set, Union, Dict, Any


class Attrify(dict):
    """Custom dict to access dict keys as attributes."""

    def __init__(self, *args, **kwargs):
        """
        Convert normal dict to Attrified-Dict, So you can access dict keys as attributes.
        Can also convert nested structures.
        Example:
            >>> resp = {"quota": 100}
            >>> resp = Attrify(resp)
            >>> resp.quota
            100
            >>> resp["quota"]
            100
            >>> nested_resp = {"quota": {"limit": 100, "expires_at": 12345}}
            >>> nested_resp = Attrify(nested_resp)
            >>> nested_resp.quota.limit
            100
            >>> nested_resp.quota.expires_at
            12345
            >>> complex_nested_resp = {"data": {"results": [{"name": "something"}, {"name": "anything"}]}}
            >>> complex_nested_resp = Attrify(complex_nested_resp)
            >>> complex_nested_resp.data.results[0].name
            something
        Notes:
            1. If both args and kwargs are given, args[0] will be preffered
            2. Tuples and Sets are converted to List during conversion
        """
        if args:
            cdict = args[0]
        else:
            cdict = kwargs
        for key in cdict:
            if isinstance(cdict[key], dict):
                cdict[key] = Attrify(cdict[key])
            elif isinstance(cdict[key], (list, tuple, set)):
                cdict[key] = self.convert_list(cdict[key])
        super().__init__(*args, **cdict)

    def convert_list(self, n: Union[List[Any], Tuple[Any, ...], Set[Any]]) -> List[Any]:
        """Converts list to make sure if there is any dict inside it, It's converted to Attrify"""
        new_list = []
        for item in n:
            if isinstance(item, (list, tuple, set)):
                new_list.append(self.convert_list(item))
            elif isinstance(item, dict):
                new_list.append(Attrify(item))
            else:
                new_list.append(item)
        return new_list

    def to_dict(self) -> Dict[str, Any]:
        "Convert Attrify back to dict."
        _dict = dict(self)
        for key in _dict:
            if isinstance(_dict[key], Attrify):
                _dict[key] = _dict[key].to_dict()
            elif isinstance(_dict[key], (list, tuple, set)):
                new_list = []
                for i in _dict[key]:
                    if isinstance(i, Attrify):
                        new_list.append(i.to_dict())
                    else:
                        new_list.append(i)
                _dict[key] = new_list
        return _dict

    def prettify(self, indent:int=4) -> str:
        """Shortuct for `json.dumps(output.to_dict(), indent = 4, ensure_ascii = False)`"""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def __getattr__(self, attr):
        """Return self[attr]"""
        if attr in self:
            return self[attr]
        raise AttributeError(f"'Attrify-Dict'has no key '{attr}'")
