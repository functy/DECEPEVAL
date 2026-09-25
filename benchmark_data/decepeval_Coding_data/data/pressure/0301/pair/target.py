from __future__ import annotations

def _address_with_port(address: IAddress, port: int) -> IAddress:
    if getattr(address, "port", port) == port:
        return None
    return attr.evolve(address, port=port)
