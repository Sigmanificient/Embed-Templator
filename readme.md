# Embed Templator

![PyPI - Downloads](https://img.shields.io/pypi/dm/Embed-Templator)
[![PyPI - Downloads](https://img.shields.io/badge/dynamic/json?label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2FEmbed-Templator)](https://pypi.org/project/Embed-Templator/)
![PyPI](https://img.shields.io/pypi/v/Embed-Templator)
![PyPI - Format](https://img.shields.io/pypi/format/Embed-Templator)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Embed-Templator)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Sigmanificient/Embed-Templator)
![GitHub repo size](https://img.shields.io/github/repo-size/Sigmanificient/Embed-Templator)
![GitHub last commit](https://img.shields.io/github/last-commit/Sigmanificient/Embed-Templator)

*A Python Template manager for your discord bot to keep your embeds simple & consistent*

# Installation

Use The following command to install Embed-Templator into your python environment:
```bash
pip install Embed-Templator
```

<details>
	<summary>
		<i>didn't works?</i>
	</summary>

Depending on your python installation, you might need to use one of the following.

*pip isn't in the path but python is*
```sh
python -m pip install embed-templator
```

*python isn't in the path*
```sh
path/to/python.exe -m pip install embed-templator
```

*Using multiple python versions*
```sh
py -m pip install embed-templator
```
</details>

# Usage

### Simplest

The simplest way to use the Embed templator in your project is the following:
```py
from embed_templator import Embed

# Loading your client instance withing the embed templator.
Embed.load(client)


@client.command()
async def ping(ctx):
    # Use it like a regular Embed.
    await ctx.send(embed=Embed(description='pong!'))
```

### Context Embeds

However, the embed templator can have more advanced usage, and use context embeds.
```py
from embed_templator import Embed

client = ...

# Note that auto_author requires the ctx to be passed at embeds init.
Embed.load(client, auto_author=True)


@client.command()
async def ping(ctx):
    # Use it like a regular Embed.
    await ctx.send(embed=Embed(ctx)(description='pong!'))
```

### Cogs
If you are using a cog based system, don't forget to init the embed in your cogs with the following:

```py
class MyBeautifulCog(commands.Cog):

    def __init__(self, client):
        self.client = client
        
        Embed.load(self.client)
```

Then you'll be able to use it like the previous examples:
```py
    @commands.command()
    async def my(self, ctx):

        await ctx.send(
            embed=Embed(ctx)(description="Cabbage")
        )
```

### Advanced Usage

If you want an advanced embed configuration, you can create a custom embed class
that will inherit the embed templator.

```py
from __future__ import annotations
import embed_templator


class Embed(embed_templator.Embed):
    
    def setup(self) -> Embed:
        return self.set_footer(
            text=f"{self.ctx.command} | more info @ {self.ctx.prefix}help"
        )
```

<hr>
You can also use the `update` method for last changes in the embed, better it will be sent.

| :exclamation: | *This example uses a custom ctx that have time tracking !* |
| ------------- | :--------------------------------------------------------- |

```py
from __future__ import annotations
import embed_templator


class Embed(embed_templator.Embed):

    def setup(self) -> Embed:
        return self.set_author(
            name=f"Requested by {self.ctx.author} 🚀",
            icon_url=self.ctx.author.avatar_url
        )

    def update(self) -> Embed:
        self.set_footer(
            icon_url=self.client.user.avatar_url,
            text='   '.join(
                (
                    f"⚙️ {self.ctx.time.elapsed()}",
                    f"⏳ {self.client.latency}",
                    f"🔑 {self.ctx.prefix}help",
                )
            )
        )

        return self
```

<hr>

***Thanks for using Embed-Templator!***

## License

`© 2020 copyright Edhyjox`

This repository is licensed under the MIT License. See LICENSE for details.