from resources import MENU,resources
from functions import resource_updater,transaction_reduce,print_menu,resource_check
        
while input('Wanna order ? : ') =='y':
    print_menu(MENU)
    opt = int(input('What you wanna order 1 2 or 3 :'))
    
    if opt == 1:
        if resource_check(resources,MENU['espresso']['ingredients']['water'],MENU['espresso']['ingredients']['coffee']):
            print('Can not process this order due to insufficient resources')
        else:
            if transaction_reduce(MENU['espresso']['cost']) == True:
                resources = resource_updater(resources,MENU['espresso']['ingredients']['water'],MENU['espresso']['ingredients']['coffee'],MENU['espresso']['cost'])
                print(resources)

    elif opt == 2:
        if resource_check(resources,MENU['latte']['ingredients']['water'],MENU['latte']['ingredients']['coffee'],MENU['latte']['ingredients']['milk']):
            print('Can not process this order due to insufficient resources')
        else:
            if transaction_reduce(MENU['latte']['cost']) == True:
                resources = resource_updater(resources,MENU['latte']['ingredients']['water'],MENU['latte']['ingredients']['coffee'],MENU['latte']['cost'],MENU['latte']['ingredients']['milk'])
                print(resources)

    elif opt == 3:
        if resource_check(resources,MENU['cappuccino']['ingredients']['water'],MENU['cappuccino']['ingredients']['coffee'],MENU['cappuccino']['ingredients']['milk']):
            print('Can not process this order')
        else:
            if transaction_reduce(MENU['cappuccino']['cost']) == True:
                resources = resource_updater(resources,MENU['cappuccino']['ingredients']['water'],MENU['cappuccino']['ingredients']['coffee'],MENU['cappuccino']['cost'],MENU['cappuccino']['ingredients']['milk'])
                print(resources)
    else:
        print('Bad option')
        
print('Good Bye, Have a great Time :)')        