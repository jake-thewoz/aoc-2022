import data_getter

data = data_getter.get_data(11).splitlines()
monkeys = []
master_mod = 1

# I thought this would be easiest to implement with a monkey class
class Monkey:
    def __init__(self, name, items, op, cond, c_true, c_false):
        self.name = name
        self.items = items
        self.op = op
        self.cond = cond
        self.c_true = c_true
        self.c_false = c_false
        self.inspect_count = 0
    
    def __repr__(self) -> str:
        return f"Monkey {self.name} is holding {self.items} and has performed {self.inspect_count} insepctions"
    
    def inspect(self, old):
        self.inspect_count += 1
        # print(f"Monkey inspects an item with a worry level of {old}.")
        # print(f"Worry level becomes {eval(self.op)}.")
        return eval(self.op)

    def apply_relief(self, value):
        # print(f"Applying relief brings worry level down to {value}")
        return value % master_mod


    def add_item(self, value):
        # print(f"Item with worry level {value} is thrown to monkey {self.name}.")
        self.items.append(value)
    
    def test(self, value):
        if value % self.cond == 0:
            # print(f"Current worry level is divisible by {self.cond}.")
            monkeys[self.c_true].add_item(value)
        else:
            # print(f"Current worry level is not divisible by {self.cond}.")
            monkeys[self.c_false].add_item(value)

        # This will be handled elsewhere
        # self.items.remove(value)
    
    def take_turn(self):
        # print(f"Monkey {self.name}:")
        # print(f"Monkey {self.name} is staring their turn with {self.items}")
        for i in range(len(self.items)):
            value = self.inspect(self.items[i])
            value = self.apply_relief(value)
            self.test(value)
        self.items.clear()


# Here we create our list of monkeys

for i in range(0, len(data), 7):
    name = data[i].split(' ')[1][0]
    items = data[i+1].split(' ')[4:]
    items = [num.strip(',') for num in items]
    items = [eval(num) for num in items]
    op = data[i+2].split(' ')[5:]
    op = ' '.join(op)
    cond = int(data[i+3].split(' ')[5])
    print(cond)
    c_true = int(data[i+4].split(' ')[9])
    c_false = int(data[i+5].split(' ')[9])

    monkeys.append(
        Monkey(
            name, items, op, cond, c_true, c_false
        )
    )

# Here we create the master modulus:
for monkey in monkeys:
    master_mod *= monkey.cond

key_rounds = [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

# Now we perform the game, and 'r' is for round
for r in range(10000):
    for monkey in monkeys:
        monkey.take_turn()
        
    if (r+1) in key_rounds:
        print(f"Current state of monkeys after round {r+1}")
        for monkey in monkeys:
            print(monkey)
    

# Tallying up the inspections:
inspections = []
for monkey in monkeys:
    inspections.append(monkey.inspect_count)

inspections.sort()

print(f"The product of the two busiest monkeys' inspections is {inspections[-1] * inspections[-2]}")