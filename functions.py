def print_menu(MENU):
    count=1
    for key in MENU:
        print(f"{count} ->{key} : ${MENU[key]['cost']}")
        count +=1

def resource_check(resources,water,coffee,milk=0):        
    if (resources['water'] -water) <0:
        return True
    elif (resources['coffee'] - coffee) <0:
        return True
    elif milk > 0 and (resources['milk'] - milk <0):
        return True 
    else:
        return False

def resource_updater(resources,water,coffee,money,milk=0):
    resources['water']-=water
    resources['coffee']-=coffee
    resources['milk']-=milk
    resources['money']+=money
    return resources

def transaction_reduce(cost):
    QUARTER,DIME,NICKEL,CENT =0.25,0.10,0.05,0.01
    quarter = float (input('How many quarters you wanna give ? :'))
    dime =  float(input('How many dimes you wanna give ? :'))
    nickel = float(input('How many nickels you wanna give ? :'))
    cent = float(input('How many cents you wanna give ? :'))
    total = quarter*QUARTER + DIME*dime + NICKEL*nickel + CENT*cent

    if(total >=cost):
        print(f'You have paid {total}  and your change is {total-cost}')
        return True
    else:
        print(f'Insufficient funds for transaction')
        return False