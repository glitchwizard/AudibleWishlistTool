import datetime
import util
import audible

# NOTE: Uncomment auth with .from_login() if you haven't created the login file,
# once it's created, use .from_file() from then on. I'll automate this later.
# I Needed OTP so I added the OTP callback

# def custom_otp_callback():
#     return input('OTP:')

# Authorize and register in one step, you'll need this first to create the file
# replace USERNAME, PASSWORD, and COUNTRY_CODE with your audible account info or
# auth = audible.Authenticator.from_login(
#     USERNAME,
#     PASSWORD,
#     locale=COUNTRY_CODE,
#     with_username=False,
#     otp_callback=custom_otp_callback
# )

# Save credentials to file
# auth.to_file("login")

auth = audible.Authenticator.from_file('login')


def get_wishlist():
    total_wishlist_length = None
    wishlist_pages = None
    wishlist = util.read_local_file('wishlist.dat')

    if wishlist is None:
        wishlist = []
        with audible.Client(auth=auth) as client:
            wishlist_returned = client.get(
                "1.0/wishlist",
                num_results=50,
                response_groups="product_desc, product_attrs",
                sort_by="-Rating"
            )

            if total_wishlist_length is None:
                total_wishlist_length = wishlist_returned['total_results']
                wishlist_pages = int(total_wishlist_length / 50) + 1

            for i in range(wishlist_pages):
                wishlist_returned = client.get(
                    "1.0/wishlist",
                    num_results=50,
                    response_groups="product_desc, product_attrs",
                    sort_by="-Rating",
                    page=i
                )
                for book in wishlist_returned['products']:
                    book2 = {}
                    for key in book:
                        if book[key] is not None:
                            book2.update({key: book[key]})
                    wishlist.append(book2)

            wishlist = {'DateCreated': datetime.datetime.now(),
                        'Wishlist': wishlist}
            util.write_local_file(wishlist, 'wishlist.dat')

    twentyfour_hours_ago = datetime.datetime.now() - datetime.timedelta(hours=24)

    if wishlist['DateCreated'] < twentyfour_hours_ago:
        wishlist = {'DateCreated': datetime.datetime.now(),
                    'Wishlist': wishlist}
        util.write_local_file(wishlist, 'wishlist.dat')

    return wishlist['Wishlist']
