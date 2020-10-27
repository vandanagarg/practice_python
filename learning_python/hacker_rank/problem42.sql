-- Comparing two columns of same table for symmetry 


select x,y from functions
where concat(x,y) in (select concat(y,x) from functions) and x<y
union all 
select x,y from functions group by x,y having count(*)>1
order by x


SELECT f1.X, f1.Y FROM Functions f1
INNER JOIN Functions f2 ON f1.X=f2.Y AND f1.Y=f2.X
GROUP BY f1.X, f1.Y
HAVING COUNT(f1.X)>1 or f1.X<f1.Y
ORDER BY f1.X


select x, y from functions f1 
    where exists(select * from functions f2 where f2.y=f1.x 
    and f2.x=f1.y and f2.x>f1.x) and (x!=y) 
union 
select x, y from functions f1 where x=y and 
    ((select count(*) from functions where x=f1.x and y=f1.x)>1)    
        order by x;

-- The first condition in that line makes sure pairs with the same X and Y values don't get to count themselves as their symmetric pair. (e.g. if 10 10 appears one time it's not counted as a symmetric pair, but as 13 13 appears twice, that is a symmetric pair)

-- The second condition ensures that only one of a pair is displayed. (e.g. if 3 24 and 24 3 form a symmetric pair, it will only display 3 24, not 24 3 as well.)