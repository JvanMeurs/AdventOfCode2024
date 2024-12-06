def parse_input(file_name):
    with open(file_name,'r') as file:
         lines =  file.readlines()
    
    rules = {}
    updates = []
    isRule=True

    for line in lines:
        if '' == line.strip():
            isRule = False
            continue

        if isRule:
            key = int(line.strip().split("|")[0])
            value = int(line.strip().split("|")[1])
            if not key in rules.keys():
                rules[key] = [value] if key not in rules.keys() else rules[key].append(value)
                continue
            rules[key].append(value)

        else:
            updates.append([int(i) for i in line.strip().split(",")])

    return rules,updates    

def is_correct_order(rules,update):
    for i in range(len(update)):
        key = update[-(1+i)]
        if key in rules.keys():
           if any(j in rules[key] for  j in update[:-(1+i)]):
               return 0
    return 1

def change_order(rules,update):
    for i in range(len(update)):
        key = update[-(1+i)]
        if key in rules.keys():
            for j in update[:-(1+i)]:
                if (j in rules[key] ):
                    update[update.index(j)], update[-(1+i)] = update[-(1+i)], update[update.index(j)]
    
    return update

def sum_middle_page(rules,updates):
    correct_sum = 0
    incorrect_sum = 0
    for update in updates:
        if is_correct_order(rules,update):
            correct_sum += update[len(update)//2]
        else:
            while not is_correct_order(rules,update):
                update = change_order(rules,update)
            incorrect_sum += update[len(update)//2]
    
    return correct_sum,incorrect_sum
if __name__ == ("__main__"):
    rules,updates = parse_input("sample_input.txt")
    print(sum_middle_page(rules,updates))

    rules,updates = parse_input("input.txt")
    print(sum_middle_page(rules,updates))
