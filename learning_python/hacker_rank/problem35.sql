-- creating patterns

-- MS SQL SERVER
DECLARE @i INT = 20
WHILE (@i > 0) 
BEGIN
   PRINT REPLICATE('* ', @i) 
   SET @i = @i - 1
END
;

declare @row int = 1
while (@row < 21)
begin
    print replicate('* ', @row)
    set @row = @row + 1
end;



-- MySQL
set @number = 21;
select repeat('* ', @number := @number - 1) from information_schema.tables;

-- reverse pattern
set @row := 0;
select repeat('* ', @row := @row + 1) from information_schema.tables where @row < 20;