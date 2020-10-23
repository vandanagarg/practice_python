/*
 given two tables: Students and Grades. Students contains three columns ID, Name and Marks.
Find grades
*/

/*Variant 1*/

SELECT Students.Name, Grades.Grade, Students.Marks 
FROM Students INNER JOIN Grades
ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark 
WHERE Grades.Grade > 7
ORDER BY Grades.Grade DESC,
Students.Name ASC;

SELECT null, Grades.Grade, Students.Marks
FROM Students INNER JOIN Grades
ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark
WHERE Grades.Grade <= 7 ORDER BY Grades.Grade DESC, Students.Marks ASC;

/*Variant 2*/

SELECT
IF (Grades.Grade > 7, Students.Name, NULL) AS Sname,
Grades.Grade, Students.Marks
FROM Students 
INNER JOIN Grades
ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark
ORDER BY Grades.Grade DESC, Sname ASC, Students.Marks ASC;


/* Variant 3*/
SELECT 
    CASE
        WHEN Grades.Grade > 7
        THEN Students.Name
        WHEN Grades.Grade <= 7
        THEN NULL
    END,
    Grades.Grade, Students.Marks
    FROM Students INNER JOIN Grades
    ON Students.Marks BETWEEN Grades.Min_Mark AND Max_Mark
    ORDER BY Grades.Grade DESC, Students.Name ASC, Students.Marks ASC;



/* Variant 4*/
SELECT IF(GRADE < 8, NULL, NAME), GRADE, MARKS
FROM STUDENTS JOIN GRADES
WHERE MARKS BETWEEN MIN_MARK AND MAX_MARK
ORDER BY GRADE DESC, NAME, MARKS