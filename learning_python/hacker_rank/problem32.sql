-- You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

SELECT N,
IF(P IS NULL,'Root',
IF((SELECT COUNT(*) FROM BST WHERE P=B.N)>0,'Inner','Leaf'))
FROM BST AS B
ORDER BY N;

SELECT CASE
	WHEN P IS NULL THEN CONCAT(N, ' Root')
	WHEN N IN (SELECT DISTINCT P FROM BST) THEN CONCAT(N, ' Inner')
	ELSE CONCAT(N, ' Leaf')
	END
FROM BST
ORDER BY N ASC

SELECT N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN N IN (SELECT P FROM BST) THEN 'Inner'
        ELSE 'Leaf'
    END
FROM BST
ORDER BY N;

