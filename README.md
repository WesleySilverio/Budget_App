# What is Budget App ?
Budget App is a program that stores your financial movements, since deposits, fund checking, withdrawls, transfers and in the end it provides a balance of all transactions accomplished and makes a graph of spent comparison. This type of tool is very useful for everyone that needs a more precise accompaniment of their account, in this way facillitating future plannings and business balance.

## Usage Rules  
All functioning of this program is using the methodology of orientation objects , therefore, the users will have the liberty to add any of methods bellow :
Observation: Create a variable to ease the use of the class *Category* and add a name to be used as internal parameter of the class, for example *food = Category("Food")*.

1) *deposit* - Adds a value deposit and one description, for example *food.deposit(amount,"description")*
2) *check_funds* - Check if it is possible to make any expenses or transfers according to the available balance, the True return shows that the operation is possible, while False means that you don't have funds for the operation, *food.check_funds(amount)*
3) *withdraw* - Adds a spent and one description, *food.withdraw(amount, "description")*
4) *transfer* - Transfers an amount of money between previously created categories, noting a cash outflow for the current category and adding a deposit for the other one, *food.transfer(amount, target category)*
5) *str* - Creates the balance and lists each description and it's respective value, also showing the final balance amount, *food.__ str__()*

## Create Spend Chart Function
This function is responsible for creating the comparison chart between categories. To use it, simply provide the function with a list of all the categories used. For example *print(create_spend_chart([food,cloth,auto]))*
