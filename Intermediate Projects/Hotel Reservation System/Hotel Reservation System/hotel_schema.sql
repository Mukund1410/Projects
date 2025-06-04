CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'customer') NOT NULL
);

CREATE TABLE IF NOT EXISTS rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_type ENUM('single', 'double', 'suite') NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    price DECIMAL(10, 2) NOT NULL DEFAULT 1000.00
);

CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    user_name VARCHAR(100),
    room_type VARCHAR(20),
    check_in DATE,
    check_out DATE DEFAULT NULL,
    room_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE IF NOT EXISTS payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT UNIQUE,
    user_id INT,
    amount DECIMAL(10, 2),
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'paid') DEFAULT 'paid',
    FOREIGN KEY (booking_id) REFERENCES bookings(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Sample admin insert
INSERT INTO users (name, email, password, role)
VALUES ("Mukund Mohan", "mukundmohan67@gmail.com", "mukund123", "admin");
