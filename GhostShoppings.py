Productnames = ["raw chicken", "raw beef", "ham", "carrots", "milk"]
Prices = [200, 225, 150, 45, 30]

print("Welcome to Ghost Shoppings")
print("Here is our available menu:")
for i in range(5):
    print(f"{Productnames[i]}: {Prices[i]}")

receipt_total = 0
decor1 = "_" * 15
decor2 = "=" * 20
discount_rate = 0.10


def generate_receipt(total_amount):
    print(decor2)
    print("Ghost Shoppings")
    print(decor1)
    if total_amount > 500:
        final_total = total_amount - (total_amount * discount_rate)
        print("Discount = 10%")
        print(f"Final Total = {final_total} EGP")
    else:
        print("Discount = 0%")
        print(f"Final Total = {total_amount} EGP")
    print("Thank you for shopping with us!\n")


while True:
    product = input("\nPlease, enter the product name (or 'finish' to receive receipt):\n").lower().strip()

    if product == 'finish':
        generate_receipt(receipt_total)
        break

    elif product in Productnames:
        receipt_total += Prices[Productnames.index(product)]
        print(f"{product} added! Current total: {receipt_total} EGP")

    else:
        print("Product not found. Please check the spelling and try again.")