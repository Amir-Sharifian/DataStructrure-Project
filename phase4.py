def faze4(people, people_calls, defendants, smuggler):
    res = []
    for person in defendants:
        find = False
        for i in people_calls[person.ssn]:
            if people[i] in smuggler:
                res.append(person)
                find = True
                break
        if find:
            continue
        for i in smuggler:
            for j in people_calls[i.ssn]:
                if person == people[j]:
                    res.append(person)
                    find = True
                    break
            if find:
                break

    return set(res)
