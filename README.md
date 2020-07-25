Pyro
----

Pyro is a [Discord](https://discord.com/) bot that allows controlling of the indie game, [Pixel Fireplace](https://hammertail.itch.io/pixel-fireplace) via text commands.

Usage
-----

To run this, you need to provide a .env file with an authenticated bot toke (with appropriate permisions). See [this tutorial](https://realpython.com/how-to-make-a-discord-bot-python/) for more details on how to set up and invite the Bot to your server.


```bash
# .env
DISCORD_TOKEN={your token}
```

To install the requirements using pip:

```bash
$ pip install -r requirements.txt
```

Finally, run the script:

```bash
$ python pyro.py
```

Then launch the Pixel Fireplace and give the Window focus. Now on any Discord server with the Bot present you can type:

```
!fireplace
```

And have the command typed in on the machine that the Bot is running on.

Todo
----

- [ ] Some sanity checking on the size of the input
- [ ] Support for arrow keys for moving the marshmallow

Thanks
------

Obvious huge thanks to Ted Martens for making Pixel Fireplace in the first place.

This tutorial was very useful for getting a basic bot working:
https://realpython.com/how-to-make-a-discord-bot-python/