--database.sql
-- create Payment_Type table
CREATE TABLE Payment_Type (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);

-- insert payment types A, B, C as cash, credit card, coupon respectively
INSERT INTO Payment_Type (id, name) VALUES 
(1, 'cash'), 
(2, 'credit card'), 
(3, 'coupon');

-- create Transaction table
CREATE TABLE "Transaction" (
    id INT PRIMARY KEY,
    date DATE,
    price INT,
    payment_id VARCHAR(5) -- stores A, B, C as per problem statement
);

-- insert mock data into Transaction table
INSERT INTO "Transaction" (id, date, price, payment_id) VALUES 
(1, '2020-01-01', 1000, 'A'), -- year 2020 (should be excluded)
(2, '2020-02-01', 500, 'B'),  -- year 2020 (should be excluded)
(3, '2021-01-31', 2000, 'A'), -- year 2021 + A (Cash) -> include
(4, '2021-03-15', 600, 'A'),  -- year 2021 + A (Cash) -> include
(5, '2021-06-10', 1000, 'B'), -- year 2021 + B (Credit Card) -> include
(6, '2021-08-20', 100, 'C');  -- year 2021 + C (Coupon) -> exclude