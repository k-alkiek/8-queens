from abc import ABC, abstractmethod


class AbstractSolver(ABC):

    @abstractmethod
    def get_running_time(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_expanded_count(self):
        pass
