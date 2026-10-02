WITH F AS (
    SELECT  SUM(CASE WHEN CATEGORY = 'Front End' THEN CODE END) AS FRONT,
            SUM(CASE WHEN NAME = 'Python' THEN CODE END) AS PYTHON,
            SUM(CASE WHEN NAME = 'C#' THEN CODE END) AS C
      FROM  SKILLCODES
)
SELECT  CASE
            WHEN (SKILL_CODE & FRONT) > 0 AND (SKILL_CODE & PYTHON) > 0
                THEN 'A'
            WHEN (SKILL_CODE & C) > 0
                THEN 'B'
            WHEN (SKILL_CODE & FRONT) > 0
                THEN 'C'
        END AS GRADE,
        ID,
        EMAIL
  FROM  DEVELOPERS
        CROSS JOIN F
 WHERE  (SKILL_CODE & FRONT) > 0
        OR (SKILL_CODE & C) > 0
 ORDER
    BY  GRADE, ID
;