SELECT
    COUNT(*) as FISH_COUNT,
    MONTH(time) as MONTH
FROM
    fish_info
GROUP BY
    MONTH(time)
ORDER BY
    MONTH
;