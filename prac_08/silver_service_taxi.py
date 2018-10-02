from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Like a taxi but fancier"""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
        super().__init__(name, fuel)

    def get_fare(self):
        """Return the price of the trip plus the flagfall"""
        return super().get_fare() + self.flagfall

    def __str__(self):
       return super().__str__() + " plus flagfall of ${:.2f}".format(self.flagfall)

