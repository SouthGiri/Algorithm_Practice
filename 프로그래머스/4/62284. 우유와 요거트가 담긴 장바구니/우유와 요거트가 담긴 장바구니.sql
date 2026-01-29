SELECT  m.cart_id
  FROM  (
        SELECT  DISTINCT cart_id
          FROM  cart_products
         WHERE  name = 'Milk'
        ) AS m JOIN
        (
        SELECT  DISTINCT cart_id
          FROM  cart_products
         WHERE  name = 'Yogurt'
        ) AS y ON
        m.cart_id = y.cart_id
 ORDER
    BY  cart_id
;