# coffeemachine
Simple coffee machine script.

## main.py
This is where the magic happens. The menu is displayed here.
First, the user is asked whether they even want to place an order or not.
Then the menu option is checked and then  resource is checked.
If there are sufficient resources the person is asked to pay.

Now the machine is coin operated and coins have to be inserted.
The slot can check the appropriate price of the drink, take only
the appropriate price and give the correct change.

The operations continue till we have enough resources and 
whether sufficient change has been given.

## functions.py
The following functions are here
1) print_menu : Prints the menu items with price. Along with an index num
2) resource_check : Checks if suitable resources are available to process order
3) resource_updater : Updates the resources post transaction
4) transaction_reduce : Manages the transactions and returns true to signal correct payment.

## resources.py
Contains the dictionary of menu items
Contains the dictionary resource available. 


## FUTURE WORK
1) Scalable options selection.
2) Instead of cancelling transaction, it should give person the ability to add remaining sum
3) Make it object oriented
4) During running, relaod the resources to continue.
