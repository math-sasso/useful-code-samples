import pytest
from somewhere import MyClass

@pytest.fixture
def mock_class(
    mock_arg
):
    """This fixture can be used in any test

    """

    obj  = MyClass(mock_arg)
    return obj