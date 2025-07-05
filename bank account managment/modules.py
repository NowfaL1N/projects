accounts = {}
balances = {}

def create_account(acc_num, name, age, mobile, password):
    if acc_num in accounts:
        return False, "Account number already exists."
    accounts[acc_num] = {
        'name': name,
        'age': age,
        'mobile': mobile,
        'password': password,
        'id': str(len(accounts) + 1000)
    }
    balances[acc_num] = 0
    return True, accounts[acc_num]['id']

def authenticate(acc_id, password):
    for acc_num, info in accounts.items():
        if info['id'] == acc_id and info['password'] == password:
            return acc_num
    return None

def add_money(acc_num, amount):
    balances[acc_num] += amount
    return balances[acc_num]

def withdraw_money(acc_num, amount):
    if balances[acc_num] >= amount:
        balances[acc_num] -= amount
        return True, balances[acc_num]
    else:
        return False, balances[acc_num]

def show_balance(acc_num):
    return balances[acc_num]

def find_id(mobile):
    for info in accounts.values():
        if info['mobile'] == mobile:
            return info['id']
    return None
