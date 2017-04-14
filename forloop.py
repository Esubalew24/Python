'''
list1 = ['a', 'b', 'c']

for list in list1:
    print list

list2 = {"abc":3, "efg": 4, "xyz":5}
for number in list2:
    print list2[number]

list3 = {"Abebe": "Demissie", "Asabneh": "Shitahun", "Esubalew": "Workineh"}
for first_names in list3:
    print list3[first_names]
    if first_names == "Abebe":
        print first_names

name = "Esubalew is Guines"

for letter in name:
    if letter == "is":
        print name

prices = {"banana": 4,"apple": 2,"orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
for key in prices:
    print key
    print "prices: %s" % prices[key]
    print "Stock: %s" % stock[key]

once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
    print "Once: %s" % once[key]
    print "Twice: %s" % twice[key]

    '''

prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    total = 0
    for key in prices:
       y = prices[key] * stock[key]
       total = total + y

    print total