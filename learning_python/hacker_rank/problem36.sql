-- Print Prime Numbers


-- option 1

SELECT GROUP_CONCAT(NUMB SEPARATOR '&')
FROM (
    SELECT @num:=@num+1 as NUMB FROM
    information_schema.tables t1,
    information_schema.tables t2,
    (SELECT @num:=1) tmp
) tempNum
WHERE NUMB<=1000 AND NOT EXISTS(
		SELECT * FROM (
			SELECT @nu:=@nu+1 as NUMA FROM
			    information_schema.tables t1,
			    information_schema.tables t2,
			    (SELECT @nu:=1) tmp1
			    LIMIT 1000
			) tatata
		WHERE FLOOR(NUMB/NUMA)=(NUMB/NUMA) AND NUMA<NUMB AND NUMA>1
	)

-- option 2

SET @potential_prime = 1;
SET @divisor = 1;

SELECT GROUP_CONCAT(POTENTIAL_PRIME SEPARATOR '&') FROM
    (SELECT @potential_prime := @potential_prime + 1 AS POTENTIAL_PRIME FROM
    information_schema.tables t1,
    information_schema.tables t2
    LIMIT 1000) list_of_potential_primes
WHERE NOT EXISTS(
	SELECT * FROM
        (SELECT @divisor := @divisor + 1 AS DIVISOR FROM
	    information_schema.tables t4,
        information_schema.tables t5
	    LIMIT 1000) list_of_divisors
	WHERE MOD(POTENTIAL_PRIME, DIVISOR) = 0 AND POTENTIAL_PRIME <> DIVISOR);

-- Explanation:

-- 1) The two inner SELECTs (SELECT @potential_prime and SELECT @divisor) create two lists. Both of them contain numbers from 1 to 1000. The first list is list_of_potential_primes and the second is list_of_divisors.

-- 2) Then, we iterate over the list of the potential primes (the outer SELECT) and for each number from this list we look for divisors (SELECT * FROM clause) that can divide the number without a reminder and are not equal to the number (WHERE MOD... clause). If at least one such divisor exists, the number is not prime and is not selected (WHERE NOT EXISTS... clause).