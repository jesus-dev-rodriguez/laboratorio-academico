class Mask:
    """Tipo especializado de 64 bits para aislar la representación numérica."""
    def __init__(self, valor: int):
        self.valor = valor & 0xFFFFFFFFFFFFFFFF

    def __or__(self, otro: Mask) -> Mask:
        return Mask(self.valor | otro.valor)

    def __and__(self, otro: Mask) -> Mask:
        return Mask(self.valor & otro.valor)

    def __invert__(self) -> Mask:
        return Mask(~self.valor)

I = Mask(0xFFFFFFFFFFFFFFFF)
O = Mask(0)