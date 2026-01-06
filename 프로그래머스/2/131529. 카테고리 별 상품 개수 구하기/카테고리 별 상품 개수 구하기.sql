-- 코드를 입력하세요
SELECT LEFT(product_code, 2) as category, count(product_id) as products
FROM product
GROUP BY LEFT(product_code, 2)