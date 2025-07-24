-- Items Table
CREATE TABLE Items (
    ItemID INT PRIMARY KEY,
    ItemName VARCHAR(100),
    Price DECIMAL(10,2)
);

INSERT INTO Items VALUES
(1, 'Hard Disk', 3500.00),
(2, 'RAM 8GB', 2800.00);

-- Suppliers Table
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY,
    Name VARCHAR(100),
    Contact VARCHAR(15)
);

INSERT INTO Suppliers VALUES
(1, 'Tech Supplies Ltd', '9812345678'),
(2, 'Delta Components', '9823456789');

-- Purchase Table
CREATE TABLE Purchases (
    PurchaseID INT PRIMARY KEY,
    ItemID INT,
    SupplierID INT,
    Quantity INT
);

INSERT INTO Purchases VALUES
(1, 1, 1, 20),
(2, 2, 2, 50);
