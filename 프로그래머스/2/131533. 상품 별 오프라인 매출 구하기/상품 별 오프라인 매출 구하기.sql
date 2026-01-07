-- 코드를 입력하세요
SELECT product_code, SUM(price * sales_amount) AS SALES
FROM
    PRODUCT p
    JOIN OFFLINE_SALE os
    ON p.product_id = os.product_id
GROUP BY
    product_code
ORDER BY
    SALES DESC, product_code