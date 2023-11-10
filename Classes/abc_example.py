from abc import ABC, abstractmethod


class Phone(ABC):
    def __init__(self, model: str) -> None:
        self.model = model

    @property
    @abstractmethod
    def power(self):
        pass

    @abstractmethod
    def call_target(self, name: str):
        pass


class iBanana(Phone):
    def __init__(self, model: str) -> None:
        super().__init__(model)

    @property
    def power(self):
        return f"Phone model {self.model} 50% battery remaining..."

    def call_target(self, name: str):
        raise NotImplementedError("Code missing..")


ibanana = iBanana("iBanana")

print(ibanana.power)

# phone = Phone('ibanana')
