# Write your MySQL query statement below
SELECT name AS Employee
FROM Employee
WHERE salary > (
    SELECT salary
    FROM Employee AS m
    WHERE Employee.managerId = m.id
);
