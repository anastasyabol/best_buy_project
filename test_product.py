import pytest
import products


def test_create_new_product():
    """ test that product created"""
    test_product = products.Product("MacBook Air M2", price=1450, quantity=100)
    assert test_product is not None


def test_empty_name_exception():
    """tests that exception raises in case of emty string"""
    with pytest.raises(ValueError, match="Wrong name"):
        test_product = products.Product("", price=1450, quantity=100)


def test_wrong_amount_exception():
    """tests that exception raises in case of negative price or price 0 or wrong quantity amount"""
    with pytest.raises(ValueError, match="Wrong amount"):
        test_product = products.Product("MacBook Air M2", price=0, quantity=100)
    with pytest.raises(ValueError, match="Wrong amount"):
        test_product = products.Product("MacBook Air M2", price=-5, quantity=100)
    with pytest.raises(ValueError, match="Wrong amount"):
        test_product = products.Product("MacBook Air M2", price=15, quantity=0)
    with pytest.raises(ValueError, match="Wrong amount"):
        test_product = products.Product("MacBook Air M2", price=15, quantity=-10)


def test_price_type_exception():
    """tests that exception raises in case of price is not int or float"""
    with pytest.raises(ValueError, match="Price must be an int or float"):
        test_product = products.Product("MacBook Air M2", price="free", quantity=100)


def test_quantity_type_exception():
    """tests that exception raises in case of quantity is not an int"""
    with pytest.raises(TypeError, match="Quantity must be an int"):
        test_product = products.Product("MacBook Air M2", price=200, quantity=1.5)


def test_become_inactive():
    """tests when a product reaches 0 quantity, it becomes inactive."""
    test_product = products.Product("MacBook Air M2", price=1450, quantity=100)
    test_product.buy(100)
    assert test_product.active == False

def test_buy_modifies_quantity():
    """tests product purchase modifies the quantity and returns the right output."""
    test_product = products.Product("MacBook Air M2", price=1450, quantity=100)
    test_product.buy(50)
    assert test_product.quantity == 50

def test_buy_too_much():
    """tests buying a larger quantity than exists invokes exception"""
    test_product = products.Product("MacBook Air M2", price=15, quantity=100)
    with pytest.raises(ValueError, match=f"Wrong quantity! Amount higher than availible quantity: {test_product.quantity}"):
        test_product.buy(1010)