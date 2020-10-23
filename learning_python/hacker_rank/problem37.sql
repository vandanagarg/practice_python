-- Finding Median value of a column in a table


-- For ODD number of records

Select round(S.LAT_N,4) mediam
from station S
where
(select count(Lat_N) from station where Lat_N < S.LAT_N ) = (select count(Lat_N) from station where Lat_N > S.LAT_N)