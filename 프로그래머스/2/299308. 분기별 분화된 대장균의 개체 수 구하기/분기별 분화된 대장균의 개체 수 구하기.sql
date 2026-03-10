SELECT 
      Q AS QUARTER
    , COUNT(*) AS ECOLI_COUNT
FROM
    (SELECT 
        CASE FLOOR((MONTH(DIFFERENTIATION_DATE) - 1) / 3)
            WHEN 0 THEN '1Q'
            WHEN 1 THEN '2Q'
            WHEN 2 THEN '3Q'
            WHEN 3 THEN '4Q'
        END AS Q
     FROM ECOLI_DATA
    ) AS T
GROUP BY
    Q
ORDER BY
    Q