-- Products Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(100),
    Price DECIMAL(10,2)
);

INSERT INTO Products VALUES
(1, 'Notebook', 50.00),
(2, 'Pen', 10.00);

-- Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100),
    Phone VARCHAR(15)
);

INSERT INTO Customers VALUES
(1, 'Deepak Sharma', '9012345678'),
(2, 'Ritika Jain', '9123456789');

-- Sales Table
CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    CustomerID INT,
    Quantity INT
);

INSERT INTO Sales VALUES
(1, 1, 1, 5),
(2, 2, 2, 10);
