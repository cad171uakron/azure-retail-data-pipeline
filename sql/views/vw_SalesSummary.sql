CREATE OR ALTER VIEW vw_SalesSummary AS
SELECT
    o.OrderDate,
    s.StoreID,
    s.City,
    SUM(oi.Qty * oi.Price) AS Revenue,
    SUM(oi.Qty) AS UnitsSold,
    COUNT(DISTINCT o.OrderID) AS Orders
FROM Orders o
JOIN OrderItems oi
    ON o.OrderID = oi.OrderID
JOIN Stores s
    ON o.StoreID = s.StoreID
GROUP BY
    o.OrderDate,
    s.StoreID,
    s.City;