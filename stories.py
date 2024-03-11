"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.madlib_template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.madlib_template

        for (k, v) in answers.items(): #.items returns each item in a dict as tuples in a list
            text = text.replace("{" + k + "}", v)

        return text


# Here's a story to get you started



story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, long-ago in a placed called {place}, there lived a
       {adjective} {noun}. It loved to {verb}."""
)


