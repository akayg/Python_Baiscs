from collections import OrderedDict

od = OrderedDict()
od["one"] = 1
od["two"] = 2
od["three"] = 3

od.move_to_end("one")  # moves 'one' to the end
print(od)

od.popitem(last=False)  # removes the first item ('two')
print(od)
