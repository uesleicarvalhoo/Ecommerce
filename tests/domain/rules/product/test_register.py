import pytest
from pytest_mock import MockerFixture

from backend.application.services import ProductService
from backend.domain.contracts import Storage
from backend.domain.exceptions import DuplicatedDataError, NotFoundError
from backend.domain.rules.product import RegisterProduct
from tests.factories.product import NewProductFactory


@pytest.fixture()
def sut(product_service: ProductService, storage: Storage) -> RegisterProduct:
    return RegisterProduct(product_service, storage)


def test__check_if_code_is_already_used_return_false_when_service_raise_not_found_error(
    sut: RegisterProduct, mocker: MockerFixture
):
    def raise_not_found_error(self: RegisterProduct):
        raise NotFoundError("Code not found")

    # Prepare
    code = "fakecode"
    sut.service.get_by_code = mocker.Mock(side_effect=raise_not_found_error)

    # Arrange
    code_is_already_used = sut._check_if_product_code_already_used(code)

    # Action/Assert
    assert code_is_already_used is False


def test__check_if_code_is_already_used_return_true_when_service_does_not_raise_not_found_error(
    sut: RegisterProduct, mocker: MockerFixture
):
    # Prepare
    code = "fakecode"
    sut.service.get_by_code = mocker.Mock(return_value=None)

    # Arrange
    code_is_already_used = sut._check_if_product_code_already_used(code)

    # Action/Assert
    assert code_is_already_used is True


def test__check_if_name_is_already_used_return_false_when_service_raise_not_found_error(
    sut: RegisterProduct, mocker: MockerFixture
):
    def raise_not_found_error(self: RegisterProduct):
        raise NotFoundError("name not found")

    # Prepare
    name = "fakename"
    sut.service.get_by_name = mocker.Mock(side_effect=raise_not_found_error)

    # Arrange
    name_is_already_used = sut._check_if_product_name_already_used(name)

    # Action/Assert
    assert name_is_already_used is False


def test__check_if_name_is_already_used_return_true_when_service_does_not_raise_not_found_error(
    sut: RegisterProduct, mocker: MockerFixture
):
    # Prepare
    name = "fakename"
    sut.service.get_by_name = mocker.Mock(return_value=None)

    # Arrange
    name_is_already_used = sut._check_if_product_name_already_used(name)

    # Action/Assert
    assert name_is_already_used is True


def test_handle_raises_duplicated_data_error_when_product_code_is_already_used(
    sut: RegisterProduct, mocker: MockerFixture
):
    # Prepare
    spy = sut._check_if_product_code_already_used = mocker.Mock(
        sut._check_if_product_code_already_used, return_value=True
    )
    sut._check_if_product_name_already_used = mocker.Mock(sut._check_if_product_name_already_used, return_value=False)

    # Arrange
    schema = NewProductFactory()

    # Action/Assert
    with pytest.raises(DuplicatedDataError):
        sut.handle(schema, b"")

    spy.assert_called()


def test_handle_raises_duplicated_data_error_when_product_name_is_already_used(
    sut: RegisterProduct, mocker: MockerFixture
):
    # Prepare
    sut._check_if_product_code_already_used = mocker.Mock(sut._check_if_product_code_already_used, return_value=False)
    spy = sut._check_if_product_name_already_used = mocker.Mock(
        sut._check_if_product_name_already_used, return_value=True
    )

    # Arrange
    schema = NewProductFactory()

    # Action/Assert
    with pytest.raises(DuplicatedDataError):
        sut.handle(schema, b"")

    spy.assert_called()


def test_handle_call_service_create_when_phone_and_name_does_not_used(sut: RegisterProduct, mocker: MockerFixture):
    # Prepare
    sut._check_if_product_code_already_used = mocker.Mock(sut._check_if_product_code_already_used, return_value=False)
    sut._check_if_product_name_already_used = mocker.Mock(sut._check_if_product_name_already_used, return_value=False)
    spy = mocker.spy(sut.service, "create")

    # Arrange
    schema = NewProductFactory()

    # Action
    sut.handle(schema, b"")

    # Assert
    [called_schema, file_key], _ = spy.call_args
    assert file_key
    assert called_schema == schema


def test_handle_call_service_upload_file(sut: RegisterProduct, mocker: MockerFixture):
    # Prepare
    sut._check_if_product_code_already_used = mocker.Mock(sut._check_if_product_code_already_used, return_value=False)
    sut._check_if_product_name_already_used = mocker.Mock(sut._check_if_product_name_already_used, return_value=False)
    spy = mocker.spy(sut.storage, "upload")

    # Arrange
    schema = NewProductFactory()

    # Action
    sut.handle(schema, b"")

    # Assert
    spy.assert_called()
