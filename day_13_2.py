import data_getter
import functools

data = data_getter.get_data(13).splitlines()

pairs = []

for i in range(len(data)):
    if i % 3 == 0:
        pairs.append({})
        pairs[-1]['left'] = eval(data[i])
    elif i % 3 == 1:
        pairs[-1]['right'] = eval(data[i])
    else:
        continue

pairs.append(
    {
        'left': [[2]],
        'right': [[6]]
    }
)
    
def compare(left, right):
    decision_made = False
    answer = False
    results = [decision_made, answer]

    i = 0
    while not decision_made:
        # First, we check for out of bounds
        if i >= len(right) and i >= len(left):
            # In this case, both ran out at the same time
            decision_made = False
            answer = True
            return [decision_made, answer]
        elif i >= len(left) and i < len(right):
            # In this case, left ran out and right didn't, so we have our result!
            decision_made = True
            answer = True
            return [decision_made, answer]
        elif i >= len(right) and i < len(left):
            # In this case, the right side ran out of length first. THat means it fails!
            decision_made = True
            answer = False
            return [decision_made, answer]

        # next, we check for type mismatch
        elif type(left[i]) != type(right[i]):
            # Next we check which is a list
            if type(left[i]) == list:
                right[i] = [right[i]]
            else:
                left[i] = [left[i]]
            # now we call the function again, stepping into the lists
            # the types should match, so that's good
            results = compare(left[i], right[i])
            if results[0] == True:
                return results

        # Now we check if they're both lists
        elif type(left[i]) == list and type(right[i]) == list:
            # and if they are, we recursively call the function 
            results = compare(left[i], right[i])
            if results[0] == True:
                return results
        
        # Now we can assume they're both ints
        else:
            # Now we're in the comparing digits area:
            # print(f"Comparing {left[i]} and {right[i]}...")
            if left[i] < right[i]:
                decision_made = True
                answer = True
                return [decision_made, answer]
            elif left[i] == right[i]:
                decision_made = False
            elif left[i] > right[i]:
                decision_made = True
                answer = False
                return [decision_made, answer]
        # Can't forget to iterate!
        i += 1 

    return results

def calling_compare(left, right):
    r_bool = compare(left, right)[1]
    if r_bool:
        return -1
    else:
        return 1

array_pairs = []

for pair in pairs:
    array_pairs.append(pair['left'])
    array_pairs.append(pair['right'])

# for line in array_pairs:
#     print(line)

print("Sorting...")

sorted_list = sorted(array_pairs, key=functools.cmp_to_key(calling_compare))

# for line in answer:
#     print(line)

# Now I've got to hack a way to find the divider packets...
indeces = []
for i in range(len(sorted_list)):
    line = sorted_list[i]
    while type(line) == list:
        if len(line) == 1:
            line = line[0]
            continue
        else:
            break
    if line == 2 or line == 6:
        indeces.append(i)

# print(f"Product of indeces of [[2]] and [[6]] is {functools.reduce((lambda x,y: (x+1)*(y+1)),indeces)}")
print(f"Product of indeces of [[2]] and [[6]] is {(indeces[0] + 1) * (indeces[1] + 1)}")