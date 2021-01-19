import pandas as pd


class Node:
    key = None


class Edge:
    key = None
    from_node_key = None
    to_node_key = None


class PeopleNode(Node):

    def __init__(self, first_name, last_name, ssn, birthday, birthplace, workplace):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.birthday = birthday
        self.birthplace = birthplace
        self.workplace = workplace
        self.key = self.ssn

        self.owned_cars = []
        self.owned_houses = []
        self.owned_bank_accounts = []
        self.owned_phone_numbers = []

        self.coming_relations = []
        self.exiting_relations = []

        all_people[self.key] = self


class BankAccountNode(Node):
    def __init__(self, ssn_of_owner, bank_name, sheba_number, account_number):
        self.ssn_of_owner = ssn_of_owner
        self.bank_name = bank_name
        self.sheba_number = sheba_number
        self.account_number = account_number
        self.key = self.account_number

        self.coming_transactions = []
        self.exiting_transactions = []

        all_bank_accounts[self.key] = self
        all_people[ssn_of_owner].owned_bank_accounts.append(self)


class HouseNode(Node):
    def __init__(self, ssn_of_owner, price, postal_code, size, address):
        self.ssn_of_owner = ssn_of_owner
        self.price = price
        self.postal_code = postal_code
        self.size = size
        self.address = address
        self.key = self.postal_code

        self.owner = None

        all_houses[self.key] = self


class CarNode(Node):
    def __init__(self, plate_number, ssn_of_owner, model, color):
        self.plate_number = plate_number
        self.ssn_of_owner = ssn_of_owner
        self.model = model
        self.color = color
        self.key = self.plate_number

        self.owner = None

        all_cars[self.key] = self


class PhoneNumberNode(Node):
    def __init__(self, ssn_of_owner, phone_number, operator):
        self.ssn_of_owner = ssn_of_owner
        self.phone_number = phone_number
        self.operator = operator
        self.key = phone_number

        self.coming_calls = []
        self.exiting_calls = []

        all_phone_numbers[self.key] = self
        all_people[ssn_of_owner].owned_phone_numbers.append(self)


class OwnershipEdge(Edge):
    def __init__(self, from_node_key, to_node_key, ownership_id, date, paid_money):
        self.from_node_key = from_node_key
        self.to_node_key = to_node_key
        self.ownership_id = ownership_id
        self.date = date
        self.paid_money = paid_money
        self.key = self.ownership_id

        all_ownerships[self.key] = self

        if ord(to_node_key[2]) > 1000:
            all_people[from_node_key].owned_cars.append(self)
            all_cars[to_node_key].owner = self
        else:
            all_people[from_node_key].owned_houses.append(self)
            all_houses[int(to_node_key)].owner = self


class TransactionEdge(Edge):
    def __init__(self, from_node_key, to_node_key, transaction_id, date, price):
        self.from_node_key = from_node_key
        self.to_node_key = to_node_key
        self.transaction_id = transaction_id
        self.date = date
        self.price = price
        self.key = self.transaction_id

        all_transactions[self.key] = self

        all_bank_accounts[from_node_key].exiting_transactions.append(self)
        all_bank_accounts[to_node_key].coming_transactions.append(self)


class CallEdge(Edge):
    def __init__(self, from_node_key, to_node_key, call_id, date, duration):
        self.from_node_key = from_node_key
        self.to_node_key = to_node_key
        self.call_id = call_id
        self.date = date
        self.duration = duration
        self.key = self.call_id

        all_calls[self.key] = self

        all_phone_numbers[from_node_key].exiting_calls.append(self)
        all_phone_numbers[to_node_key].coming_calls.append(self)


class RelationshipEdge(Edge):
    def __init__(self, from_node_key, to_node_key, relation, date):
        self.from_node_key = from_node_key
        self.to_node_key = to_node_key
        self.relation = relation
        self.date = date
        self.key = str(from_node_key) + str(to_node_key)

        all_relationships[self.key] = self

        all_people[from_node_key].exiting_relations.append(self)
        all_people[to_node_key].coming_relations.append(self)


def read_inputs(path):
    people = pd.read_csv(path['people'])
    accounts = pd.read_csv(path['bank_accounts'])
    cars = pd.read_csv(path['cars'])
    homes = pd.read_csv(path['houses'])
    phones = pd.read_csv(path['phone_numbers'])

    calls = pd.read_csv(path['calls'])
    ownerships = pd.read_csv(path['ownerships'])
    relationships = pd.read_csv(path['relationships'])
    transactions = pd.read_csv(path['transactions'])

    for i in range(people.shape[0]):
        x = people.iloc[i]
        PeopleNode(x['first_name'], x['last_name'], x['ssn'], x['birthday'], x['city'], x['work'])

    for i in range(accounts.shape[0]):
        x = accounts.iloc[i]
        BankAccountNode(x['ssn'], x['bank_name'], x['IBAN'], x['account_id'])

    for i in range(cars.shape[0]):
        x = cars.iloc[i]
        CarNode(x['plate'], x['ssn'], x['model'], x['color'])

    for i in range(homes.shape[0]):
        x = homes.iloc[i]
        HouseNode(x['ssn'], x['price'], x['postal_code'], x['size'], x['address'])

    for i in range(phones.shape[0]):
        x = phones.iloc[i]
        PhoneNumberNode(x['ssn'], x['number'], x['operator'])

    for i in range(calls.shape[0]):
        x = calls.iloc[i]
        CallEdge(x['from'], x['to'], x['call_id'], x['date'], x['duration'])

    for i in range(ownerships.shape[0]):
        x = ownerships.iloc[i]
        OwnershipEdge(x['from'], x['to'], x['ownership_id'], x['date'], x['amount'])

    for i in range(relationships.shape[0]):
        x = relationships.iloc[i]
        RelationshipEdge(x['from'], x['to'], x['relation'], x['date'])

    for i in range(transactions.shape[0]):
        x = transactions.iloc[i]
        TransactionEdge(x['from'], x['to'], x['transaction_id'], x['date'], x['amount'])


all_people = {}
all_bank_accounts = {}
all_houses = {}
all_cars = {}
all_phone_numbers = {}

all_calls = {}
all_ownerships = {}
all_relationships = {}
all_transactions = {}

all_data = {
    'all_people': all_people,
    'all_bank_accounts': all_bank_accounts,
    'all_houses': all_houses,
    'all_cars': all_cars,
    'all_phone_numbers': all_phone_numbers,
    'all_calls': all_calls,
    'all_ownerships': all_ownerships,
    'all_relationships': all_relationships,
    'all_transactions': all_transactions,
}
