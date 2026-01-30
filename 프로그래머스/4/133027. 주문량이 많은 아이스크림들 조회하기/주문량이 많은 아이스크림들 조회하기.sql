SELECT  j.flavor
  FROM  (
        SELECT  flavor, SUM(total_order) as total
          FROM  july
         GROUP
            BY  flavor
        ) AS j JOIN
        first_half AS f ON
        j.flavor = f.flavor
 ORDER
    BY  total + total_order DESC
 LIMIT  3
;