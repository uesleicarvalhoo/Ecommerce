from enum import Enum, unique


@unique
class OrderStatus(str, Enum):
    PENDING: int = "Pendente"
    COMPLETED: int = "Concluido"
    CANCELED: int = "Cancelado"


@unique
class SaleType(str, Enum):
    SALE_IN_PIX: str = "Venda via PIX"
    SALE_IN_DEBT: str = "Venda no débito"
    SALE_IN_CREDIT: str = "Venda no crédito"
    SALE_IN_MONEY: str = "Venda em dinheiro"
    SALE_IN_TRANSFER: str = "Venda por transferencia bancaria"
    SALE_IN_BILLET: str = "Venda por boleto"
    SALE_OTHERS: str = "Outra tipo de venda"


@unique
class PaymentStatus(str, Enum):
    PENDING: str = "Pendente"
    SUCCESS: str = "Sucesso"
    CANCELED: str = "Cancelado"
    REFUSED: str = "Recusado"
