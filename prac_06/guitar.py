CURRENT_YEAR = 2018


class Guitar:
    """Represent a guitar object"""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string containing guitar details."""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Returns the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
