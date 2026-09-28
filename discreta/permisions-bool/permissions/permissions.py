from __future__ import annotations

from permissions.bitmask import I, O, Mask

class Permissions:
    Empty = O
    Full = I

    Create = Mask(1 << 0)
    Read = Mask(1 << 1)
    Update = Mask(1 << 2)
    Delete = Mask(1 << 3) 

    """Tipo de Dato Abstracto (ADT) que representa un elemento del Álgebra de Boole."""
    def __init__(self, *atomos: Mask):
        resultado = Mask(0)
        
        for atomo in atomos:
            resultado |= atomo

        self._mask = resultado

    def __add__(self, otro: Permissions) -> Permissions:
        """Suma lógica (Unión / OR)"""
        return Permissions(self._mask | otro._mask)

    def __mul__(self, otro: Permissions) -> Permissions:
        """Producto lógico (Intersección / AND)"""
        return Permissions(self._mask & otro._mask)

    def __invert__(self) -> Permissions:
        """Complemento absoluto (NOT) acotado al Universo"""
        return Permissions(~self._mask)


    def __eq__(self, otro: object) -> bool:
        """Identidad exacta entre dos conjuntos de la retícula"""
        if not isinstance(otro, Permissions):
            return False
        return self._mask.valor == otro._mask.valor

    def __sub__(self, otro: Permissions):
        return self * ~otro

    def __repr__(self) -> str:
        """Visualización del estado del elemento en 64 bits alineados"""
        return f"{self._mask.valor:064b}"