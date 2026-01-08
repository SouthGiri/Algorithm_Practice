SELECT
    COUNT(*) as fish_count
FROM
    fish_info as fi JOIN
    fish_name_info as fni
    ON fi.fish_type = fni.fish_type
WHERE
    fish_name IN ('BASS', 'SNAPPER')
;