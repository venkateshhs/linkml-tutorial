from linkml_runtime.dumpers import json_dumper
# to dump or print everything as json
from personinfo_5 import Person

p1 = Person(id='ORCID:9876', full_name='Lex Luthor', aliases=["Bad Guy"])
print(json_dumper.dumps(p1))