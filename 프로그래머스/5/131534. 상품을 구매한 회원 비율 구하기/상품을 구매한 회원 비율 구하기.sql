WITH user AS (
    SELECT  user_id
      FROM  user_info
     WHERE  LEFT(joined, 4) = 2021
)
SELECT  YEAR(sales_date),
        MONTH(sales_date),
        COUNT(DISTINCT sale.user_id) AS PURCHASED_USERS,
        ROUND(COUNT(DISTINCT sale.user_id) / (SELECT COUNT(*) FROM user), 1) AS PUCHASED_RATIO
  FROM  user JOIN
        online_sale AS sale ON
        user.user_id = sale.user_id
 GROUP
    BY  YEAR(sales_date),
        MONTH(sales_date)
 ORDER
    BY  YEAR(sales_date),
        MONTH(sales_date)
;