SELECT  COUNT(*) AS FISH_COUNT,
        MONTH(time) AS MONTH
  FROM  fish_info
 GROUP
    BY  MONTH(time)
 ORDER
    BY  MONTH
;
  