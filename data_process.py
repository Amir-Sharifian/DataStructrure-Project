from data import all_people, all_phone_numbers, all_bank_accounts, all_data

from phase1 import faze1
from phase2 import faze2
from phase3 import faze3
from phase4 import faze4
from helper_methods import *


def run():
    smugglers = find_smuggler(all_people)
    all_people_transactions = find_people_transactions(all_people, all_bank_accounts)
    all_people_calls = find_people_calls(all_people, all_phone_numbers)

    defendants_faze1 = faze1(all_people)
    res1 = print_defendants(defendants_faze1)
    res1 = (res1, print_defendants(smugglers), print_all_data(all_data))

    defendants_faze2 = faze2(all_people)
    res2 = print_defendants(defendants_faze2)

    defendants_faze3 = faze3(all_people, all_people_transactions, defendants_faze2, smugglers)
    res3 = print_defendants(defendants_faze3)

    defendants_faze4 = faze4(all_people, all_people_calls, defendants_faze3, smugglers)
    res4 = print_defendants(defendants_faze4)

    return [res1, res2, res3, res4]
