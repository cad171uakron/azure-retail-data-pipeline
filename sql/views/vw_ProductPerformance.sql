CREATE OR ALTER VIEW vw_ProductPerformance AS
SELECT
    p.ProductID,
    p.CategoryID,
    SUM(oi.Qty) AS UnitsSold,
    SUM(oi.Qty * oi.Price) AS Revenue
FROM Products p
JOIN OrderItems oi
    ON p.ProductID = oi.ProductID
GROUP BY
    p.ProductID,
    p.CategoryID;