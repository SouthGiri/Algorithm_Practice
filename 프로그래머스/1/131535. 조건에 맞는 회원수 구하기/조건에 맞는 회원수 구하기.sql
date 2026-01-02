-- 코드를 입력하세요
SELECT COUNT(*) as USERS
FROM user_info
WHERE AGE BETWEEN 20 AND 29
    and YEAR(joined) = '2021'