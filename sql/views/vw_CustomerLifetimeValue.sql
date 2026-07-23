CREATE OR ALTER VIEW vw_CustomerLifetimeValue AS
SELECT
    c.CustomerID,
    COUNT(DISTINCT o.OrderID) AS Orders,
    SUM(oi.Qty * oi.Price) AS LifetimeRevenue
FROM Customers c
JOIN Orders o
    ON c.CustomerID = o.CustomerID
JOIN OrderItems oi
    ON o.OrderID = oi.OrderID
GROUP BY
    c.CustomerID;