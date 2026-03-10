WITH RECURSIVE generation AS (
    SELECT  id,
            parent_id,
            1 AS gen
      FROM  ecoli_data
     WHERE  parent_id IS NULL
    
    UNION ALL
    
    SELECT  e.id,
            e.parent_id,
            gen + 1 AS gen
      FROM  generation g JOIN
            ecoli_data e ON
            g.id = e.parent_id
)
SELECT  
COUNT(*) AS COUNT,
        gen AS GENERATION
  FROM  generation g
 WHERE  NOT EXISTS (
    SELECT  1
      FROM  generation g1
     WHERE  g.id = g1.parent_id
 )
 GROUP
    BY  gen
 ORDER
    BY  generation