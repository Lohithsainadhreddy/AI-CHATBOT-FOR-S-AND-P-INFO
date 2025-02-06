-- Create Database
-- CREATE DATABASE InventoryDB;
-- USE InventoryDB;

-- Create Supplier Table
CREATE TABLE Supplier (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierName VARCHAR(100) NOT NULL,
    ContactPerson VARCHAR(100),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100) UNIQUE,
    Address TEXT,
    Country VARCHAR(50)
);

-- Insert Sample Data into Supplier Table
INSERT INTO Supplier (SupplierName, ContactPerson, PhoneNumber, Email, Address, Country) VALUES
('TechSupply Co.', 'John Doe', '9876543210', 'john@techsupply.com', '123 Street, NY', 'USA'),
('Global Parts', 'Alice Smith', '8765432109', 'alice@globalparts.com', '456 Avenue, CA', 'USA'),
('ElectroMart', 'David Brown', '7654321098', 'david@electromart.com', '789 Road, TX', 'USA'),
('Gadget World', 'Emma Wilson', '6543210987', 'emma@gadgetworld.com', '321 Blvd, FL', 'USA'),
('Innovate Supply', 'Michael Johnson', '5432109876', 'michael@innovatesupply.com', '555 Lane, IL', 'USA');

-- Create Product Table
CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    SupplierID INT,
    Price DECIMAL(10,2),
    StockQuantity INT,
    Category VARCHAR(50),
    WarrantyPeriod INT COMMENT 'Warranty in months',
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
);

-- Insert Sample Data into Product Table
INSERT INTO Product (ProductName, SupplierID, Price, StockQuantity, Category, WarrantyPeriod) VALUES
('Laptop', 1, 1200.50, 50, 'Electronics', 24),
('Smartphone', 2, 850.75, 100, 'Electronics', 12),
('Wireless Headphones', 3, 199.99, 150, 'Accessories', 18),
('Gaming Mouse', 4, 49.99, 200, 'Accessories', 12),
('4K Monitor', 5, 350.00, 75, 'Electronics', 36);
