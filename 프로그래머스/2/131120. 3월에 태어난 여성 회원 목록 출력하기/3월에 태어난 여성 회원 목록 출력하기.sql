-- 코드를 입력하세요
SELECT
    member_id,
    member_name,
    gender,
    LEFT(date_of_birth, 10) as date_of_birth
FROM
    member_profile
WHERE
        MID(date_of_birth, 6, 2) = 03 
    AND gender = 'W'
    AND TLNO IS NOT NULL
ORDER BY
    member_id