from __future__ import annotations

from typing import Union, Dict, Any, Iterable, Optional, Callable

import discord

from .exceptions import (
    NotInitializedError,
    AlreadyInitializedError,
    MissingContextError
)


class Embed(discord.Embed):
    """Embed wrapping of discord.Embed class."""

    client = None
    default_args = {'description': 'embedTemplator'}
    auto_author = False

    @classmethod
    def load(cls, client, auto_author=False, **kwargs):
        """Set the client instance.

        :param client
            The bot instance used.

        :param auto_author: bool
            Automatically set the author section with ctx.author.

        :param kwargs:
            Embed additional to set name, descriptions, color and more.

            if you set kwargs on the initialization,
                you will not be able to set the context.
        """
        cls.client = client
        cls.default_args.update(kwargs)
        cls.auto_author = auto_author

    def __init__(self, ctx=None, **kwargs):
        """Initialise discord embed, set default bot color and
            set dynamic footer if ctx is passed.

        :param ctx: the command context for higher embed customizations.

        :param kwargs:
            Embed additional to set name, descriptions, color and more.
        """

        if not self.client:
            raise RuntimeError("Embed hasn't been initialized yet.")

        self.initialized = False

        if len(kwargs):
            _kwargs = self.default_args.copy()
            _kwargs.update(kwargs)
            self.initialized = True

        self.ctx = ctx

    def __call__(self, **kwargs) -> Embed:
        """Initialise the embed with a command context.
            Should be used if you use ctx in the setup or update.

        :param kwargs:
            Embed additional to set name, descriptions, color and more.

        :return: the embed for chaining methods.
        """
        if self.initialized:
            raise AlreadyInitializedError()

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

    def setup(self) -> Embed:
        """A setup method for inheritance,
            will be called after the embed initialization (ctx mode).
        :return: the embed for chaining methods.
        """
        return self

    def to_dict(self):
        """Transforms the embed to a json-like python format.

        :return: the embed for chaining methods.
        """
        if not self.initialized:
            raise NotInitializedError()

        if self.auto_author:
            if self.ctx is None:
                raise MissingContextError()

            self.set_author(
                name=self.ctx.author,
                icon_url=self.ctx.author.avatar_url
            )

        self.update()
        return super().to_dict()

    def update(self) -> None:
        """A update method for inheritance,
            called before the embed a sent.
        """
        pass

    def add_fields(
            self,
            field_list: Union[Dict[Any, Any], Iterable[Iterable[Any, Any]]],
            checks: Optional[Callable[[Any], Any]] = bool,
            map_title: Optional[Callable[[Any], str]] = str,
            map_values: Optional[Callable[[Any], str]] = str,
            inline: bool = True
    ) -> Embed:
        """Add multiple fields from a list,
            dict or generator of fields with possible mapping.

            :param field_list:
                A iterable or generator of the fields to add.

            :param checks:
                A filter function to remove embed fields.

            :param map_title:
                A transform function to change the titles

            :param map_values:
                A transform function to change the values.

            :param inline:
                Whether to create grid or each field on a new line.

            :return: the embed for chaining methods.
            """
        if isinstance(field_list, dict):
            field_list: Iterable[Iterable[Any, Any]] = field_list.items()

        for field_name, field_value in field_list:
            val = (
                map_values(field_value)
                if not isinstance(field_value, tuple)
                else map_values(*field_value)
            )

            if checks(val):
                self.add_field(
                    name=map_title(field_name),
                    value=val,
                    inline=inline
                )

        return self
