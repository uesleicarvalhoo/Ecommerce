import pytest
from passlib.context import CryptContext

from backend.application.contracts import Client, Order, Product, Repository, Streamer
from backend.application.services import (
    AuthenticationService,
    ClientService,
    EmailService,
    OrderService,
    PaymentService,
    ProductService,
)
from backend.infrastructure.contracts import QueryClient, QueryOrder, QueryProduct
from backend.infrastructure.controller.payment import FakePaymentController
from backend.infrastructure.controller.storage import NoneStorage
from backend.infrastructure.controller.streamer import NoneStreamer
from backend.infrastructure.repository.mock import MockClientRepository, MockOrderRepository, MockProductRepository


@pytest.fixture()
def storage():
    return NoneStorage()


@pytest.fixture()
def streamer():
    return NoneStreamer()


@pytest.fixture()
def password_context() -> CryptContext:
    return CryptContext(schemes=["bcrypt"], deprecated="auto")


# Infra services
@pytest.fixture()
def payment_controller() -> FakePaymentController:
    return FakePaymentController()


# Repositories
@pytest.fixture()
def client_repository():
    return MockClientRepository()


@pytest.fixture()
def product_repository():
    return MockProductRepository()


@pytest.fixture()
def order_repository():
    return MockOrderRepository()


# Services
@pytest.fixture()
def authentication_service(password_context: CryptContext) -> AuthenticationService:
    return AuthenticationService(password_context, secret_key="I'm a super test secret key!")


@pytest.fixture()
def client_service(client_repository: Repository[Client, QueryClient], authentication_service: AuthenticationService):
    return ClientService(client_repository, authentication_service)


@pytest.fixture()
def product_service(product_repository: Repository[Product, QueryProduct]):
    return ProductService(product_repository)


@pytest.fixture()
def order_service(order_repository: Repository[Order, QueryOrder], product_repository: Repository[Order, QueryProduct]):
    return OrderService(order_repository, product_repository)


@pytest.fixture()
def email_service(streamer: Streamer):
    return EmailService(streamer=streamer)


@pytest.fixture()
def payment_service(payment_controller: FakePaymentController):
    return PaymentService(payment_controller)
