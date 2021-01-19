def check(count, person, people_transactions, smugglers, people):
    count += 1
    if count > 5:
        return False
    for i in people_transactions[person.ssn]:
        if people[i] in smugglers:
            return True
        else:
            if check(count, people[i], people_transactions, smugglers, people):
                return True
    return False


def faze3(people, people_transactions, defendants, smuggler):
    res = []
    for i in defendants:
        if check(0, i, people_transactions, smuggler, people):
            res.append(i)
    return set(res)
