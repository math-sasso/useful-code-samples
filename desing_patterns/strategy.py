from enum import Enum

class LastYearStrategy():
    def __init__(
        self,
        arg1: float,
        arg2: int,

    ):
        pass

    def do_this():
        pass

class CurrentYearStrategy():
    def __init__(
        self,
        arg1: float,
        arg2: int,

    ):
        pass

    def do_that():
        pass

class Strategies(Enum):
    ly = LastYearStrategy
    cy = CurrentYearStrategy

if __name__ == "__main__":
    laster_year_strategy = Strategies["ly"]
    current_year_strategy = Strategies["cy"]
