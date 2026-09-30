SELECT  E1.ID
  FROM  ECOLI_DATA E1
 WHERE  EXISTS (
            SELECT  1
              FROM  ECOLI_DATA E2
             WHERE  1=1
                    AND E2.ID = E1.PARENT_ID
                    AND EXISTS (
                        SELECT  1
                          FROM  ECOLI_DATA E3
                         WHERE  1=1
                                AND E3.PARENT_ID IS NULL
                                AND E3.ID = E2.PARENT_ID
             )
        )
 ORDER
    BY  E1.ID
;
