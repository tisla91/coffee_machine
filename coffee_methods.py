from coffee_ingredients import MENU, resources

class CoffeeMachine:
    """Takes, and process coffee orders."""

    def __init__(self, user_order):
        # Constructor will take user(buyer) order as input.
        self.user_order = user_order
        self.resources = resources

    def enough_ingredients(self):
        """Checks if there is enough ingredient to make the coffee type user(buyer) ordered."""
        # self. added to coffee_ingredients_dict variable below to make it have a wider scope(beyond the method/function it was created).
        self.coffee_ingredients_dict = MENU[self.user_order]["ingredients"]
        for i in self.coffee_ingredients_dict:
            if self.resources[i] < self.coffee_ingredients_dict[i]:
                self.resources = self.resources
                print(f"Sorry, there are not sufficient ingredients to make your coffee: \n {self.resources}")
                return "ingredients deficit"


    def payment_check(self):
        """Processes user(buyer) payment."""
        print("Please insert your coins")
        quarters = float(input("Quarters: $")) * 0.25
        dimers = float(input("Dimers: $")) * 0.10
        nickles = float(input("Nickles: $")) * 0.05
        pennies = float(input("Pennies: $")) * 0.01
        total_payment = quarters + dimers + nickles + pennies
        # self. added to user_order_cost variable below to make it have a wider scope(beyond the method/function it was created).
        self.user_order_cost = MENU[self.user_order]["cost"]
        user_balance = total_payment - self.user_order_cost
        if total_payment < self.user_order_cost:
            print("Sorry that's not enough money... Money refunded.")
            return "Insufficient payment."
        elif total_payment > self.user_order_cost:
            print(f"Here is ${user_balance} in change.")
            return "Balance given."
        else:
            print(f"Making your {self.user_order}... ")
            return "Make coffee"


    def update_resources_and_make_coffee(self):
        """Uses output from enough_ingredients and payment_check above to update resources(ingredients, and money)."""
        if self.enough_ingredients() != "ingredients deficit":
            if self.payment_check() != "Insufficient payment.":
                # To update resources
                for i in self.coffee_ingredients_dict:
                    self.resources[i] -= self.coffee_ingredients_dict[i]
                # To update money
                self.resources["money"] += self.user_order_cost
                return f"Here is your {self.user_order}. Enjoy!"

