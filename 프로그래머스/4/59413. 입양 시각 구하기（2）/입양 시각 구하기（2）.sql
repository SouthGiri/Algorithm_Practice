WITH RECURSIVE hours AS (
    SELECT  0 'hour'
    
    UNION ALL
    
    SELECT  hour + 1
      FROM  hours
     WHERE  hour < 23
), counts AS (
    SELECT    HOUR(datetime) 'hour'
            , COUNT(*) 'count'
      FROM  animal_outs
     GROUP
        BY  HOUR(datetime)
)
SELECT  h.hour
        , IFNULL(count, 0)
  FROM  hours h LEFT OUTER JOIN
        counts c ON
        h.hour = c.hour
;