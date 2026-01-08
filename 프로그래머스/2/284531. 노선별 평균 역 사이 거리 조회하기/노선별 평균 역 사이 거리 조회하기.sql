SELECT
      ROUTE
    , CONCAT(ROUND(SUM(d_between_dist), 1), 'km') AS TOTAL_DISTANCE
    , CONCAT(ROUND(AVG(d_between_dist), 2), 'km') AS AVERAGE_DISTANCE
FROM
    SUBWAY_DISTANCE
GROUP BY
    ROUTE
ORDER BY
    ROUND(SUM(d_between_dist), 1) DESC
;