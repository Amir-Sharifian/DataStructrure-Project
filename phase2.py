from datetime import date as dates


def check_is_two_years_ago_or_earlier(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    current_date = dates.today()
    if current_date.year - year > 2:
        return False
    elif current_date.year - year == 2:
        if current_date.month > month:
            return False
        elif current_date.month == month:
            if current_date.day > day:
                return False
    return True


def faze2(people):
    res = []
    for i in people.values():
        iss = False
        if i.workplace == 'گمرک' or i.workplace == 'سازمان بنادر':
            for j in i.owned_cars:
                if check_is_two_years_ago_or_earlier(j.date):
                    res.append(i)
                    iss = True
                    break
            for j in i.owned_houses:
                if check_is_two_years_ago_or_earlier(j.date):
                    iss = True
                    res.append(i)
                    break
            if not iss:
                for j in i.exiting_relations:
                    person = people[j.to_node_key]
                    for k in person.owned_cars:
                        if check_is_two_years_ago_or_earlier(k.date):
                            res.append(i)
                            iss = True
                            break
                    for k in person.owned_houses:
                        if check_is_two_years_ago_or_earlier(k.date):
                            res.append(i)
                            iss = True
                            break
                    if iss:
                        break

    return set(res)
