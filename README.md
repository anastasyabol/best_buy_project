# Store System

## Introduction
This Python project represents a simple store system that manages products, inventory, and promotions. The system is designed with modularity, allowing the addition of various types of products and promotions.

## Project Structure
The project consists of three main modules:

1. **products.py**: Defines the Product class and its subclasses (NonStockedProduct, LimitedProduct). Each product has attributes such as name, price, quantity, and a promotion if applicable.

2. **promotions.py**: Contains an abstract class Promotion and its concrete implementations (SecondHalfPrice, ThirdOneFree, PercentDiscount). These promotions modify the behavior of the product's buy method.

3. **store.py**: Implements the Store class, which acts as a container for managing products. The store allows adding, removing, and ordering products.

4. **main.py**: Contains the main logic of the program. It initializes products, promotions, and the store. Users can interact with the system through a simple command-line menu.

## How to Use
1. **Product Initialization**: In the `main.py` file, a list of initial products is created, including regular products, non-stocked products, and limited products. Prices, quantities, and promotions are set accordingly.

2. **Promotions**: Various promotions are created in the `main.py` file and assigned to specific products.

3. **Store Initialization**: A store is created using the `Store` class and initialized with the list of products.

4. **User Interaction**: The program provides a simple command-line menu through the `menu()` and `func_dict` functions in the `main.py` file. Users can list products, check the total quantity in the store, make orders, and quit the program.

5. **Product Classes**: The `Product` class in `products.py` is the base class, with subclasses for non-stocked and limited products. Each product class has methods for buying, getting promotions, and setting promotions.

6. **Promotion Classes**: The `Promotion` abstract class in `promotions.py` is inherited by concrete promotion classes. These classes modify the buying behavior of products based on specific rules.

## Running the Program
To run the program, execute the `main.py` file. Follow the on-screen prompts to interact with the store system.

## Tests
The project includes a set of unit tests in the `test_products.py` file using the pytest framework. These tests cover various aspects of product creation, exception handling, and product behavior.

To run the tests, execute the following command:
```bash
pytest test_products.py
