from coffee_methods import *

coffee_machine_on = True
while coffee_machine_on:
    #Buyer is prompted for type of coffee input.
    available = ["espresso", "latte", "cappuccino", "off", "report"]
    coffee_type = input("What would you like? (espresso/latte/cappuccino):\n")
    prompt_test = CoffeeMachine(coffee_type)
    if coffee_type not in available:
        print("Please make type an available order!")
    elif coffee_type == "off":
        coffee_machine_on = False
    elif coffee_type == "report":      ## Continuusly update resources after each coffe is made because of the while loop above.
        print(prompt_test.resources)
    else:
        print(prompt_test.update_resources_and_make_coffee())


print(5 -10)