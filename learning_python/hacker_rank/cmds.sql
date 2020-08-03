select city, length(city) from station order by length(city) asc, city asc limit 1;
select city, length(city) from station order by length(city) desc, city asc limit 1;

-- city starting with "aieou"
select DISTINCT CITY from STATION where CITY RLIKE "^[aeiou].*"
SELECT DISTINCT CITY FROM STATION WHERE LEFT(CITY,1) IN ('a','e','i','o','u');

-- city ending with "aieou"
SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) IN ('a','e','i','o','u');

-- city starting and ending with "aieou"
select DISTINCT CITY from STATION WHERE LEFT(CITY,1) IN ('a','e','i','o','u')
and
RIGHT(CITY,1) IN ('a','e','i','o','u') ; 

SELECT DISTINCT city FROM station WHERE city RLIKE '^[aeiou].*[aeiou]$';

-- city not starting with "aieou"
select DISTINCT CITY from STATIOn where LEFT(CITY, 1) NOT IN ('a','e','i','o','u');

SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[^aeiou]';

-- city not starting or ending with "aieou"
select DISTINCT CITY from station where LEFT(CITY, 1) NOT IN ('A','E', 'I', 'O', 'U')
OR RIGHT(CITY, 1) NOT IN ('A','E', 'I', 'O', 'U');

SELECT DISTINCT city FROM station WHERE city RLIKE "^[^aieou]|.*[^aeiou]$";

-- Basic joins
-- Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.
-- inner join on 4 tables and counting/filtering o/p rows with having clause
select h.hacker_id, h.name
from submissions s
inner join challenges c
on s.challenge_id = c.challenge_id
inner join difficulty d
on c.difficulty_level = d.difficulty_level 
inner join hackers h
on s.hacker_id = h.hacker_id
where s.score = d.score and c.difficulty_level = d.difficulty_level
group by h.hacker_id, h.name
having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, s.hacker_id asc


-- Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.
-- Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.
-- join and self join to pick min values/satisfying conditions
select w.id, p.age, w.coins_needed, w.power
from Wands as w
join Wands_Property as p
on (w.code = p.code)
where p.is_evil = 0 and
w.coins_needed = (select min(coins_needed) from Wands as w1 
                join Wands_Property as p1
                on (w1.code = p1.code)
                where w1.power = w.power
                and p1.age = p.age)
order by w.power desc, p.age desc

-- Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by hacker_id. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.
/* these are the columns we want to output */
select c.hacker_id, h.name ,count(c.hacker_id) as c_count

/* this is the join we want to output them from */
from Hackers as h
    inner join Challenges as c on c.hacker_id = h.hacker_id

/* after they have been grouped by hacker */
group by c.hacker_id

/* but we want to be selective about which hackers we output */
/* having is required (instead of where) for filtering on groups */
having 

    /* output anyone with a count that is equal to... */
    c_count = 
        /* the max count that anyone has */
        (SELECT MAX(temp1.cnt)
        from (SELECT COUNT(hacker_id) as cnt
             from Challenges
             group by hacker_id
             order by hacker_id) temp1)

    /* or anyone who's count is in... */
    or c_count in 
        /* the set of counts... */
        (select t.cnt
         from (select count(*) as cnt 
               from challenges
               group by hacker_id) t
         /* who's group of counts... */
         group by t.cnt
         /* has only one element */
         having count(t.cnt) = 1)

/* finally, the order the rows should be output */
order by c_count DESC, c.hacker_id

/* ;) */
;

SELECT c.hacker_id, 
       h.NAME, 
       Count(c.hacker_id) AS main_cnt
FROM   hackers h 
       INNER JOIN challenges c 
               ON h.hacker_id = c.hacker_id 
GROUP  BY c.hacker_id, 
          h.NAME 
HAVING main_cnt = (SELECT Max(temp1.cnt) 
                             FROM   (SELECT Count(c.hacker_id) AS cnt 
                                     FROM   challenges c 
                                     GROUP  BY c.hacker_id) temp1) 
        OR main_cnt IN (SELECT temp2.cnt_temp
                                  FROM   (SELECT Count(c.hacker_id) AS cnt_temp
                                          FROM   challenges c 
                                          GROUP  BY c.hacker_id) temp2 
                                  GROUP  BY temp2.cnt_temp
                                  HAVING Count(temp2.cnt_temp) = 1) 
ORDER  BY Count(c.hacker_id) DESC, 
          c.hacker_id; 

--