# Write your MySQL query statement below
Select MAX(salary) as SecondHighestSalary
from Employee
where salary <> (SELECT MAX(salary) FROM Employee );