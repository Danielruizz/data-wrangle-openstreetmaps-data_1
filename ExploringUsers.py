"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    if 'uid' in element.attrib:
        if element.attrib['uid']:
            return element.attrib['uid']


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        user = get_user(element)
        if user:
            users.add(user)
        pass

    return users


def test():

    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()
