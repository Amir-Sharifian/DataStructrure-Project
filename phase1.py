def faze1(people):
    res = []
    for i in people.values():
        if i.workplace == 'گمرک' or i.workplace == 'سازمان بنادر':
            res.append(i)

    return set(res)
