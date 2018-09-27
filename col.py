from collections import defaultdict, OrderedDict, namedtuple
import pdb

# defaultdict

a = defaultdict(lambda: 'kjfhgjk afdighsjh kslhk,s h')

print(a['value'])

print(a['new'])

# d = OrderedDict()
d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 1
d['e'] = 2
d['f'] = 3
d['h'] = 1
d['i'] = 2
d['j'] = 3

for k, v in d.items():
    pdb.set_trace()
    print(k, v)

Dog = namedtuple('Dog', 'age name breed owner')

Dog(age=3,name="Sam",breed="Poodle",owner="Me")