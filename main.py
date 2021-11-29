import audible
import pandas as pd

# NOTE: Uncomment auth with .from_login() if you haven't created the login file,
# once it's created, use .from_file() from then on. I'll automate this later.

# Authorize and register in one step, you'll need this first to create the file
# auth = audible.Authenticator.from_login(
#     USERNAME,
#     PASSWORD,
#     locale=COUNTRY_CODE,
#     with_username=False
# )

# Save credentials to file
# auth.to_file("login")

auth = audible.Authenticator.from_file('login')
wishlist = []
total_wishlist_length = None
wishlist_pages = None

with audible.Client(auth=auth) as client:
    wishlist_returned = client.get(
        "1.0/wishlist",
        num_results=50,
        response_groups="product_desc, product_attrs",
        sort_by="-Rating"
    )
    if total_wishlist_length is None:
        total_wishlist_length = wishlist_returned['total_results']
        wishlist_pages = int(total_wishlist_length/50)+1

    for i in range(wishlist_pages):
        wishlist_returned = client.get(
            "1.0/wishlist",
            num_results=50,
            response_groups="product_desc, product_attrs",
            sort_by="-Rating",
            page=i
        )
        for book in wishlist_returned['products']:
            wishlist.append(book)

pd.DataFrame(wishlist)

