import os

from flask import Flask, jsonify, request

app = Flask(__name__)

Productnames = ["raw chicken", "raw beef", "ham", "carrots", "milk"]
Prices = [200, 225, 150, 45, 30]

decor1 = "_" * 15
decor2 = "=" * 20
discount_rate = 0.10

# In-memory cart. Since this is a stateless-per-process demo API,
# the cart persists for the lifetime of the running process/instance.
cart = []


def get_menu():
    return {Productnames[i]: Prices[i] for i in range(len(Productnames))}


def get_total():
    return sum(Prices[Productnames.index(product)] for product in cart)


def generate_receipt(total_amount):
    lines = [decor2, "Ghost Shoppings", decor1]

    if total_amount > 500:
        final_total = total_amount - (total_amount * discount_rate)
        discount_applied = True
        discount_percent = 10
        lines.append("Discount = 10%")
        lines.append(f"Final Total = {final_total} EGP")
    else:
        final_total = total_amount
        discount_applied = False
        discount_percent = 0
        lines.append("Discount = 0%")
        lines.append(f"Final Total = {total_amount} EGP")

    lines.append("Thank you for shopping with us!")

    return {
        "receipt": "\n".join(lines),
        "subtotal": total_amount,
        "discount_applied": discount_applied,
        "discount_percent": discount_percent,
        "final_total": final_total,
        "currency": "EGP",
    }


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Welcome to Ghost Shoppings",
        "menu": get_menu(),
        "endpoints": {
            "GET /": "Welcome message and menu",
            "GET /cart": "View current cart and total",
            "POST /cart": "Add a product to the cart (JSON body: {\"product\": \"<name>\"})",
            "DELETE /cart": "Clear the cart",
            "POST /checkout": "Finalize the order and receive a receipt",
        },
    })


@app.route("/cart", methods=["GET"])
def view_cart():
    return jsonify({
        "cart": cart,
        "total": get_total(),
        "currency": "EGP",
    })


@app.route("/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json(silent=True) or {}
    product = str(data.get("product", "")).lower().strip()

    if not product:
        return jsonify({"error": "Missing 'product' field in request body."}), 400

    if product not in Productnames:
        return jsonify({"error": "Product not found. Please check the spelling and try again."}), 404

    cart.append(product)
    total = get_total()

    return jsonify({
        "message": f"{product} added! Current total: {total} EGP",
        "cart": cart,
        "total": total,
        "currency": "EGP",
    }), 201


@app.route("/cart", methods=["DELETE"])
def clear_cart():
    cart.clear()
    return jsonify({"message": "Cart cleared.", "cart": cart, "total": 0})


@app.route("/checkout", methods=["POST"])
def checkout():
    total = get_total()
    receipt = generate_receipt(total)
    cart.clear()
    return jsonify(receipt)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
