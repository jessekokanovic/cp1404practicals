class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a programming language instance."""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.upper() == "DYNAMIC":
            return True
        else:
            return False

    def __str__(self):
        """Return language details in a formatted string."""

        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)
