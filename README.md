# Audible Wishlist Tool

---

## -- Info --
I just wanted a tool that could sort through my audible wishlist, 
and give me info in my Audible wishlist as to which titles have the
highest ratings, with the most reviews. 

For some dumb reason, Audible's main website doesn't allow users to
sort their wishlist by rating or anything like it, so time to make my
own tool. :-) 

---

## -- Getting started -- 
So using the python package [`audible`](https://audible.readthedocs.io/en/latest/index.html) was a bit tricky to get started
Basically I had to make some edits to the code because from whenever
that package was written to now, Audible changed their auth process or something

Anyhoo, you may need to do these two changes after doing `pip install -r requirements.txt`
on this repo. 

Change 1: update get_next_action_from_soup() in `/audible/login.py`
https://github.com/mkb79/Audible/pull/74/files

Change 2: update `/audible/login.py` to handle `follow_redirects=True`
https://github.com/mkb79/Audible/pull/70/files

At the time of writing this file, the author of `audible` python package hadn't completed 
the merge requests linked in the two changes there, so I just changed that code to the package
after downloading it with `pip install audible`

Hopefully it'll get updated soon and we'll just need to install the latest `pip` package of `audible`

----

### ~~ Auth ~~ 
Auth can be a bit of a pain in the butt, but eventually I was able to get it to work after making
Change 1 and Change 2 listed above. 

In this package, uncomment the auth code to get the `auth` object then save it to a file.

Once it's saved to a file, you can keep using that, which is found later in the code with
` auth = audible.Authenticator.from_file('login')`

After auth is sorted out, it will give you your audible wishlist as `wishlist`

---

### -- Running the tool --

To keep it simple, I really just wanted to plot it in a way where I could 
browse the plot for things that look interesting. As I think of more features
I'll add them in, but this is enough for now to make a decision based on
rating and number of people who rated it.

One thing I ran into was an issue relating to pandasgui spitting out the error["no module named win32api"](https://stackoverflow.com/questions/3580855/where-to-find-the-win32api-module-for-python)
If you run into this, make sure you're in the `venv` and do `pip install pywin32` and that resolved the issue for me.

#### How it works ----------

Once `auth` is all sorted out, it will generate the `wishlist` and save it locally in
a file called `wishlist.dat`, it's also encrypted because... why not. 

Once `wishlist.dat` is created, it's used in `main.py` to generate the plot.

If you want to dig around in the details of your wishlist, uncomment the `show(df)` to
give you a nifty interface to browse around the data, thanks to `pandasgui`

