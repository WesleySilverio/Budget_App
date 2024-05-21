import Budget_Process

def categories():
    n = int(input("Enter the number of categories: "))
    cat = [input("Add one category at a time: ") for _ in range(n)]
    return cat


def classes(categories):
    classe = []
    for x in range(len(categories)):
        cat_x = Budget_Process.Category(categories[x])
        classe.append(cat_x)
    return classe
    

def menu():
    cat = categories()
    classe = classes(cat)
    menu = ""
    print("Enter the initial balance for each category")
    for x in range(len(cat)):   
        inicial_value = float(input("Opening balance: "))
        inicial_description = input("Value description: ")
        classe[x].deposit(inicial_value,inicial_description)
        menu += str(x) + " = " + str(cat[x])+"\n"
    loop = True
    while loop == True:
        print("Choose which category to use: " )
        print(menu)
        choosed_cat = int(input("type it: "))
        print("Which tool do you want to use?\n" + "0 = deposit \n" + "1 = checking funds\n" + "2 = withdraw \n" 
              + "3 = transfer \n" + "4 = complete balance \n" + "5 = chart \n" + "6 = Exit the program")
        choosed_tool = int(input("Type it: "))
        if choosed_tool == 0:
            amount = float(input("Add deposit amount: "))
            description = input("Description: ")
            classe[choosed_cat].deposit(amount, description)
            print(classe[choosed_cat].ledger)
        elif choosed_tool == 1:
            amount = float(input("Add the amount to be transferred or withdrawn: "))
            fundos = classe[choosed_cat].check_funds(amount)
            if fundos == True:
                print("There is a balance available for transaction!")
            else:
                print("There is no balance for the transaction!")
        elif choosed_tool == 2:
            amount = float(input("Add withdrawal amount: "))
            description = input("Expense description: ")
            classe[choosed_cat].withdraw(amount,description)
        elif choosed_tool == 3:
            transfers_menu = ""
            amount = float(input("Add the transfer amount: "))
            for i in range(len(cat)):
                if i == choosed_cat:
                    continue
                else: transfers_menu += str(i) + " = " + str(cat[i])+"\n"
            print("Target category:")
            print(transfers_menu)
            new_cat = int(input("Type it: "))
            transfer_situation = classe[choosed_cat].transfer(amount, classe[new_cat])
            if transfer_situation == True:
                print("Transfer completed!")
            else:
                print("No balance for transfer!")
        elif choosed_tool == 4:
            print(classe[choosed_cat].__str__())
    
        elif choosed_tool == 5:
            print(Budget_Process.create_spend_chart(classe))
        else:
            break
    return "Program finished"
    
print(menu())