SELECT
    count(*) as fish_count,
    fish_name
FROM
    fish_info as fi
    JOIN fish_name_info as fni
    ON fi.fish_type = fni.fish_type
GROUP BY
    fish_name
ORDER BY
    fish_count DESC