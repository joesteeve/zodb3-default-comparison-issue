#
#

from BTrees.OOBTree import OOTreeSet
from persistent import Persistent

class Mock(Persistent):
    def __init__(self):
        super(Persistent, self).__init__()

def main():
    m = Mock()
    oset = OOTreeSet()
    oset.add(m)

if __name__ == "__main__":
    main ()
