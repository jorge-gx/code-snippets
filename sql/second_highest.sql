
SELECT min(salary)
FROM ( SELECT DISTINCT salary 
        FROM emp 
        ORDER BY salary DESC
      )
WHERE rownum<=2;

/* another example */

SELECT Salary 
FROM ( SELECT e.Salary
        , ROW_NUMBER() OVER (ORDER BY salary DESC) rn 
      FROM Employee e 
      ) 
WHERE rn = 2;
