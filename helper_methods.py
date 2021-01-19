def find_smuggler(people):
    res = []
    for i in people.values():
        if i.workplace == 'قاچاقچی':
            res.append(i)
    return res


def find_people_transactions(people, bank_accounts):
    people_transactions = {}
    for i in people.values():
        res = {}
        for j in i.owned_bank_accounts:
            for k in j.coming_transactions:
                res[bank_accounts[k.from_node_key].ssn_of_owner] = 1
        people_transactions[i.ssn] = res
    return people_transactions


def find_people_calls(people, phone_numbers):
    people_calls = {}
    for i in people.values():
        res = {}
        for j in i.owned_phone_numbers:
            for k in j.exiting_calls:
                res[phone_numbers[k.to_node_key].ssn_of_owner] = 1
        people_calls[i.ssn] = res
    return people_calls


def print_defendants(defendants):
    defendants = list(defendants)
    c = 0
    for j in range(len(defendants)):
        c += 1
        i = defendants[j]
        temp = [c, i.first_name, i.last_name, str(i.ssn), i.birthday, i.birthplace, i.workplace]
        defendants[j] = temp
    defendants.insert(0, ['ردیف', 'نام', 'نام خانوادگی', 'کد ملی', 'تاریخ تولد', 'محل تولد', 'شغل'])
    return defendants


def print_all_data(data):
    res = {}

    c = 0
    temp = []
    for i in data['all_people'].values():
        c += 1
        temp.append([c, i.first_name, i.last_name, str(i.ssn), i.birthday, i.birthplace, i.workplace])

    temp.insert(0, ['ردیف', 'نام', 'نام خانوادگی', 'کد ملی', 'تاریخ تولد', 'محل تولد', 'شغل'])
    res['people'] = temp

    c = 0
    temp = []
    for i in data['all_bank_accounts'].values():
        c += 1
        temp.append([c, i.ssn_of_owner, i.bank_name, i.sheba_number, i.account_number])

    temp.insert(0, ['ردیف', 'کد ملی دارنده حساب', 'نام بانک', 'شماره شبا', 'شماره حساب'])
    res['bank_accounts'] = temp

    c = 0
    temp = []
    for i in data['all_houses'].values():
        c += 1
        temp.append([c, i.ssn_of_owner, i.price, i.postal_code, i.size, i.address])

    temp.insert(0, ['ردیف', 'کد ملی صاحب خانه', 'قیمت', 'کد پستی', 'متراژ', 'آدرس'])
    res['houses'] = temp

    c = 0
    temp = []
    for i in data['all_cars'].values():
        c += 1
        temp.append([c, i.plate_number, i.ssn_of_owner, i.model, i.color])

    temp.insert(0, ['ردیف', 'شماره پلاک', 'کد ملی صاحب ماشین', 'مدل', 'رنگ'])
    res['cars'] = temp

    c = 0
    temp = []
    for i in data['all_phone_numbers'].values():
        c += 1
        temp.append([c, i.ssn_of_owner, i.phone_number, i.operator])

    temp.insert(0, ['ردیف', 'کد ملی صاحب موبایل', 'شماره تلفن', 'اپراتور'])
    res['phone_numbers'] = temp

    c = 0
    temp = []
    for i in data['all_calls'].values():
        c += 1
        temp.append([c, i.from_node_key, i.to_node_key, i.call_id, i.date, i.duration])

    temp.insert(0, ['ردیف', 'از شماره تلفن', 'به شماره تلفن', 'آیدی تماس', 'تاریخ تماس', 'مدت زمان تماس'])
    res['calls'] = temp

    c = 0
    temp = []
    for i in data['all_ownerships'].values():
        c += 1
        temp.append([c, i.from_node_key, i.to_node_key, i.ownership_id, i.date, i.paid_money])

    temp.insert(0, ['ردیف', 'کد ملی مالک', 'پلاک ماشین/کد پستی', 'شماره سند ثبت احوال', 'زمان تملک', 'مبلغ پرداختی'])
    res['ownerships'] = temp

    c = 0
    temp = []
    for i in data['all_relationships'].values():
        c += 1
        temp.append([c, i.from_node_key, i.to_node_key, i.relation, i.date])

    temp.insert(0, ['ردیف', 'از شخص', 'به شخص', 'نسبت', 'زمان شروع نسبت'])
    res['relationships'] = temp

    c = 0
    temp = []
    for i in data['all_transactions'].values():
        c += 1
        temp.append([c, i.from_node_key, i.to_node_key, i.transaction_id, i.date, i.price])

    temp.insert(0, ['ردیف', 'از شماره حساب', 'به شماره حساب', 'شماره تراکنش', 'تاریخ تراکنش', 'مبلغ تراکنش'])
    res['transactions'] = temp

    return res
