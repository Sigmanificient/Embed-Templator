from __future__ import annotations

import discord


class MissingContextError(Exception):

    def __init__(self):
        self.message = "ctx is a required argument you didn't passed."


class Embed(discord.Embed):
    """Embed wrapping of discord.Embed class."""

    client = None
    default_args = {'description': 'embedTemplator'}
    auto_author = False

    @classmethod
    def load(cls, client, auto_author=False, **kwargs):
        """Set the client instance."""
        cls.client = client
        cls.default_args.update(kwargs)
        cls.auto_author = auto_author

    def __init__(self, ctx=None):
        """Initialise discord embed, set default bot color and
            set dynamic footer if ctx is passed."""

        if not self.client:
            raise RuntimeError("Embed hasn't been initialized yet.")

        self.initialized = False
        self.ctx = ctx

    def __call__(self, **kwargs) -> Embed:
        self.initialized = True

        _kwargs = self.default_args.copy()
        _kwargs.update(kwargs)

        super().__init__(
            colour=getattr(
                self.client,
                'colour',
                self.client.user.colour
            ),
            **_kwargs,
        )

        return self.setup()

    def setup(self):
        return self

    def to_dict(self):
        if not self.initialized:
            super().__init__(**self.default_args)

        if self.auto_author:
            if self.ctx is None:
                raise MissingContextError()

            self.set_author(
                name=self.ctx.author,
                icon_url=self.ctx.author.avatar_url
            )

        self.update()
        return super().to_dict()

    def update(self):
        pass
