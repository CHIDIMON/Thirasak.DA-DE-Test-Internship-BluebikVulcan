--solution.sql 
-- find total price of transactions in the most recent year where payment type is 'cash' or 'credit card'
-- use PostgreSQL syntax
SELECT 
    SUM(t.price) AS total_price -- sum price from Transaction table
FROM 
    "Transaction" t -- define alias t for Transaction table
JOIN 
    "Payment_Type" p ON ( -- join Payment_Type(p) to get payment type name
        CASE 
            WHEN t.payment_id = 'A' THEN 1 -- convert 'A' to 1 to match id in Payment_Type table
            WHEN t.payment_id = 'B' THEN 2
            WHEN t.payment_id = 'C' THEN 3
        END
    ) = p.id -- join condition between Transaction and Payment_Type using the converted id
WHERE 
    -- filter only data in the most recent year in the table
    EXTRACT(YEAR FROM t."date") = (
        SELECT MAX(EXTRACT(YEAR FROM "date")) 
        FROM "Transaction" -- use Subquery to find the latest year dynamically from data (year 2021)
    )
    -- select only items that are 'cash' or 'credit card' as specified in the problem
    AND p.name IN ('cash', 'credit card');