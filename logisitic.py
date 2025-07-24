-- Shipments Table
CREATE TABLE Shipments (
    ShipmentID INT PRIMARY KEY,
    Origin VARCHAR(100),
    Destination VARCHAR(100),
    Status VARCHAR(50)
);

INSERT INTO Shipments VALUES
(101, 'Chennai', 'Delhi', 'In Transit'),
(102, 'Mumbai', 'Kolkata', 'Delivered');

-- Vehicles Table
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY,
    VehicleNumber VARCHAR(20),
    Capacity INT
);

INSERT INTO Vehicles VALUES
(1, 'TN01AB1234', 500),
(2, 'MH02XY5678', 1000);

-- Drivers Table
CREATE TABLE Drivers (
    DriverID INT PRIMARY KEY,
    Name VARCHAR(100),
    Contact VARCHAR(15)
);

INSERT INTO Drivers VALUES
(1, 'Suresh Kumar', '9999999999'),
(2, 'Rajiv Sharma', '8888888888');
