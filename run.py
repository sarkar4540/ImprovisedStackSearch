from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import input
from builtins import int

from future import standard_library
import json

standard_library.install_aliases()
import search

questionq = input("Enter the search string:")
k = input("Enter number of answers(max 50):")
res=json.loads(search.search(answer_limit=(50 if int(k) > 50 else int(k)), query=questionq))
print(json.dumps(res))
for elem in res:
    print(elem["question"]["title"])
    print(elem["answer"]["body"])
