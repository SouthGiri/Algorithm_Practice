SELECT  p.product_id,
        product_name,
        price * amount AS TOTAL_SALES
  FROM  food_product AS p JOIN        
        (
            SELECT  product_id,
                    SUM(amount) AS amount
              FROM  food_order
             WHERE  LEFT(produce_date, 7) = '2022-05'
             GROUP
                BY  product_id
        ) AS o ON
        p.product_id = o.product_id
 ORDER
    BY  total_sales DESC,
        product_id
;