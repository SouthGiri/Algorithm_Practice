-- 코드를 입력하세요
SELECT
    TRUNCATE(price, -4) as price_group,
    COUNT(*) as products
FROM
    product
GROUP BY
    TRUNCATE(price, -4)
ORDER BY
    TRUNCATE(price, -4)