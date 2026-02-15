WITH front AS (
    SELECT  SUM(code) AS 'code'
      FROM  skillcodes
     WHERE  category = 'Front End'
), python AS (
    SELECT  code
      FROM  skillcodes
     WHERE  name = 'Python'
), c AS (
    SELECT  code
      FROM  skillcodes
     WHERE  name = 'C#'
)

SELECT  CASE
            WHEN (d.skill_code & front.code) > 0 AND (d.skill_code & python.code) > 0
            THEN 'A'
            WHEN (d.skill_code & c.code) > 0
            THEN 'B'
            WHEN (d.skill_code & front.code) > 0
            THEN 'C'
        END AS GRADE,
        ID,
        email
  FROM  developers AS d,
        front,
        python,
        c
 WHERE  (d.skill_code & front.code) > 0
        OR (d.skill_code & c.code) > 0
 ORDER
    BY  grade,
        id 
;