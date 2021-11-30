import pandas as pd
import AudibleAPI
import plotly.express as px
from pandasgui import show

wishlist = AudibleAPI.get_wishlist()

df = pd.json_normalize(wishlist)

fig = px.scatter(data_frame=df,
                 x='rating.num_reviews',
                 y='rating.overall_distribution.average_rating',
                 color=None,
                 symbol=None,
                 size=None,
                 trendline=None,
                 marginal_x=None,
                 marginal_y=None,
                 facet_row=None,
                 facet_col=None,
                 render_mode='auto',
                 hover_name='title',
                 template='presentation',
                 log_x=True
                 )
fig.update()

# show(fig) - This plots the books from the wishlist, and
# and when you hover over the top of them, it
# shows the title of the book.
show(fig)

# show(df) - This can get all the DF info into
# Excel simply by selecting all and copying into MS Excel
# Uncomment to use once the GUI pops up
# show(df)

