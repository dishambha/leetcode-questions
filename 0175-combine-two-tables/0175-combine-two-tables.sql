# Write your MySQL query statement below
SELECT 
Person.firstName,
Person.lastName,
Address.city,
Address.state
from Person
Left Join Address
ON Person.personId = Address.personId;
