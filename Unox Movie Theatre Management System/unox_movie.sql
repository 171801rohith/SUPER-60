-- CREATE DATABASE unox_movie_theatre_management_system;
USE unox_movie_theatre_management_system;

-- Create Users Table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phoneNumber VARCHAR(15) UNIQUE
);

-- Create Movie Status Table
CREATE TABLE movieStatus (
    id INT PRIMARY KEY AUTO_INCREMENT,
    statusName VARCHAR(50),
    description TEXT
);

-- Create Movies Table
CREATE TABLE movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    duration INT,  -- Duration in minutes
    rating VARCHAR(10),
    movieStatusId INT,
    language VARCHAR(50),
    FOREIGN KEY (movieStatusId) REFERENCES movieStatus(id)
);

-- Create Movie Posters Table
CREATE TABLE moviePosters (
    id INT PRIMARY KEY AUTO_INCREMENT,
    movieId INT,
    imageUrl VARCHAR(255), -- Store URL of image
    uploadedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (movieId) REFERENCES movies(id)
);

-- Create Movie Format Table
CREATE TABLE movieFormat (
    id INT PRIMARY KEY AUTO_INCREMENT,
    formatName VARCHAR(50),
    description TEXT
);

-- Create Movie Format Link Table (Composite Primary Key)
CREATE TABLE movieFormatLink (
    movieId INT,
    movieFormatId INT,
    PRIMARY KEY (movieId, movieFormatId),
    FOREIGN KEY (movieId) REFERENCES movies(id),
    FOREIGN KEY (movieFormatId) REFERENCES movieFormat(id)
);

-- Create Movie Genre Table
CREATE TABLE movieGenre (
    id INT PRIMARY KEY AUTO_INCREMENT,
    genreName VARCHAR(50),
    description TEXT
);

-- Create Movie Genre Link Table (Composite Primary Key)
CREATE TABLE movieGenreLink (
    movieId INT,
    movieGenreId INT,
    PRIMARY KEY (movieId, movieGenreId),
    FOREIGN KEY (movieId) REFERENCES movies(id),
    FOREIGN KEY (movieGenreId) REFERENCES movieGenre(id)
);

-- Create Actors Table
CREATE TABLE actors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

-- Create Star Cast Table (Composite Primary Key)
CREATE TABLE starCast (
    movieId INT,
    actorId INT,
    role VARCHAR(100),
    PRIMARY KEY (movieId, actorId),
    FOREIGN KEY (movieId) REFERENCES movies(id),
    FOREIGN KEY (actorId) REFERENCES actors(id)
);

-- Create Reviews Table
CREATE TABLE reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    movieId INT,
    reviewerName VARCHAR(100),
    reviewText TEXT,
    dateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (movieId) REFERENCES movies(id)
);

-- Create Multiplex Table
CREATE TABLE multiplex (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    location VARCHAR(255),
    contactNumber VARCHAR(20)
);

-- Create Screens Table
CREATE TABLE screens (
    id INT PRIMARY KEY AUTO_INCREMENT,
    multiplexId INT,
    screenName VARCHAR(50),
    capacity INT,
    classType VARCHAR(50),
    FOREIGN KEY (multiplexId) REFERENCES multiplex(id)
);

-- Create Shows Table
CREATE TABLE shows (
    id INT PRIMARY KEY AUTO_INCREMENT,
    movieId INT,
    screenId INT,
    showTime TIMESTAMP,
    date DATE,
    FOREIGN KEY (movieId) REFERENCES movies(id),
    FOREIGN KEY (screenId) REFERENCES screens(id)
);

-- Create Seat Rows Table
CREATE TABLE seatRows (
    id INT PRIMARY KEY AUTO_INCREMENT,
    screenId INT,
    seatRow VARCHAR(10),
    FOREIGN KEY (screenId) REFERENCES screens(id)
);

-- Create Seats Table (Composite Primary Key)
CREATE TABLE seats (
    rowId INT,
    seatNumber INT,
    PRIMARY KEY (rowId, seatNumber),
    FOREIGN KEY (rowId) REFERENCES seatRows(id)
);

-- Create Bookings Table
CREATE TABLE bookings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    userId INT,
    showId INT,
    noOfTickets INT,
    bookingStatus VARCHAR(50),
    totalCost FLOAT,
    FOREIGN KEY (userId) REFERENCES users(id),
    FOREIGN KEY (showId) REFERENCES shows(id)
);

-- Create Ticket Cancellation Table
CREATE TABLE ticketCancellation (
    id INT PRIMARY KEY AUTO_INCREMENT,
    bookingId INT,
    reason TEXT,
    refundAmount FLOAT,
    date DATE,
    status VARCHAR(50),
    FOREIGN KEY (bookingId) REFERENCES bookings(id)
);

-- Create Payment Gateways Table
CREATE TABLE paymentGateways (
    id INT PRIMARY KEY AUTO_INCREMENT,
    gatewayName VARCHAR(50)
);

-- Create Payment Methods Table
CREATE TABLE paymentMethods (
    id INT PRIMARY KEY AUTO_INCREMENT,
    paymentGatewayId INT,
    paymentType VARCHAR(50),
    FOREIGN KEY (paymentGatewayId) REFERENCES paymentGateways(id)
);

-- Create Payments Table
CREATE TABLE payments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    bookingId INT,
    paymentMethodId INT,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bookingId) REFERENCES bookings(id),
    FOREIGN KEY (paymentMethodId) REFERENCES paymentMethods(id)
);

-- Create Credit Card Details Table
CREATE TABLE creditCardDetails (
    id INT PRIMARY KEY AUTO_INCREMENT,
    userId INT,
    cardHolderName VARCHAR(100),
    cardNumber VARCHAR(255), -- Should be encrypted in application
    expiryDate DATE,
    cvv INT, -- Should be encrypted in application
    FOREIGN KEY (userId) REFERENCES users(id)
);

-- Create Food Orders Table
CREATE TABLE foodOrders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    bookingId INT,
    userId INT,
    totalAmount FLOAT,
    FOREIGN KEY (bookingId) REFERENCES bookings(id),
    FOREIGN KEY (userId) REFERENCES users(id)
);

-- Create Food Items Table
CREATE TABLE foodItems (
    id INT PRIMARY KEY AUTO_INCREMENT,
    foodOrderId INT,
    itemName VARCHAR(100),
    size VARCHAR(50),
    price FLOAT,
    FOREIGN KEY (foodOrderId) REFERENCES foodOrders(id)
);

-- Create Deliveries Table
CREATE TABLE deliveries (
    id INT PRIMARY KEY AUTO_INCREMENT,
    foodOrderId INT,
    seatRowId INT,
    seatNumber INT,
    status VARCHAR(50),
    FOREIGN KEY (foodOrderId) REFERENCES foodOrders(id),
    FOREIGN KEY (seatRowId, seatNumber) REFERENCES seats(rowId, seatNumber)
);

-- Create Membership Table
CREATE TABLE membership (
    id INT PRIMARY KEY AUTO_INCREMENT,
    userId INT,
    pointsEarned INT,
    pointsRedeemed INT,
    balancePoints INT,
    FOREIGN KEY (userId) REFERENCES users(id)
);

-- Create Transaction Table
CREATE TABLE transaction (
    id INT PRIMARY KEY AUTO_INCREMENT,
    bookingId INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transactionAmount FLOAT,
    status VARCHAR(50),
    FOREIGN KEY (bookingId) REFERENCES bookings(id)
);

-- Create QR Code Table
CREATE TABLE qrcode (
    id INT PRIMARY KEY AUTO_INCREMENT,
    bookingId INT,
    generatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bookingId) REFERENCES bookings(id)
);

-- Create QR Code Tracking Table
CREATE TABLE qrcodeTracking (
    id INT PRIMARY KEY AUTO_INCREMENT,
    qrCodeId INT,
    scanSource VARCHAR(50),
    scanned VARCHAR(50),
    scanTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (qrCodeId) REFERENCES qrcode(id)
);

-- Create Feedback Table
CREATE TABLE feedBack (
    id INT PRIMARY KEY AUTO_INCREMENT,
    userId INT,
    bookingId INT,
    comments TEXT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    date DATE,
    FOREIGN KEY (userId) REFERENCES users(id),
    FOREIGN KEY (bookingId) REFERENCES bookings(id)
);

-- Create Employee Role Table
CREATE TABLE employeeRole (
    id INT PRIMARY KEY AUTO_INCREMENT,
    multiplexId INT,
    roleName VARCHAR(100),
    description TEXT,
    FOREIGN KEY (multiplexId) REFERENCES multiplex(id)
);

-- Create Employees Table
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    roleId INT,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phoneNumber VARCHAR(15),
    gender VARCHAR(10),
    joinDate DATE,
    FOREIGN KEY (roleId) REFERENCES employeeRole(id)
);

-- Create Employee Salary Table
CREATE TABLE employeeSalary (
    id INT PRIMARY KEY AUTO_INCREMENT,
    roleId INT,
    baseSalary FLOAT,
    FOREIGN KEY (roleId) REFERENCES employeeRole(id)
);
