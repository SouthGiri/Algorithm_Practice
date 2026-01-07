SELECT
    LEFT(sales_date, 10) as sales_date,
    product_id,
    user_id,
    sales_amount
FROM
    online_sale as ons 
WHERE
    LEFT(sales_date, 7) = '2022-03'
UNION
SELECT
    LEFT(sales_date, 10) as sales_date,
    product_id,
    NULL as user_id,
    sales_amount
FROM
    offline_sale as ofs
WHERE
    LEFT(sales_date, 7) = '2022-03'

ORDER BY
    sales_date,
    product_id,
    user_id