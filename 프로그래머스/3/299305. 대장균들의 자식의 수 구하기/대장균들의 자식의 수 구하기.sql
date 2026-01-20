SELECT    e1.id
        , IFNULL(
            (SELECT  COUNT(*)
               FROM   ecoli_data as e2
              WHERE  e1.id = e2.parent_id
              GROUP
                 BY  parent_id), 0) AS CHILD_COUNT
  FROM  ecoli_data as e1
 ORDER
    BY  id
;