Automatic cashier (Ghost Shoppings) — Flask web API version.

This is part of a larger virtual future mall project that spans Python, HTML,
data analytics, machine learning, and an embedded system. This repo covers
part 1: the Python cashier logic, now exposed as a stateless Flask API so it
can run on Railway without needing an interactive terminal.

## Why a web API instead of a CLI?

The original version used `input()` in a loop, which works fine locally but
crashes on Railway with `EOFError: EOF when reading a line` because there is
no terminal attached to provide input. This version replaces the CLI loop
with Flask routes — every request is independent and returns JSON.

## Endpoints

- `GET /` — welcome message and available menu
- `GET /cart` — view current cart and total
- `POST /cart` — add a product to the cart, body: `{"product": "milk"}`
- `DELETE /cart` — clear the cart
- `POST /checkout` — finalize the order, apply the 10% discount if the total
  is over 500 EGP, and return a receipt

## Business logic

- Products: raw chicken (200), raw beef (225), ham (150), carrots (45),
  milk (30)
- 10% discount applied automatically when the cart total exceeds 500 EGP
- Receipt formatting is preserved from the original CLI version

## Running locally

```
pip install -r requirements.txt
python GhostShoppings.py
```

The app listens on the port defined by the `PORT` environment variable
(defaults to `5000`), which is how Railway assigns and exposes a public
domain for the service.
