SELECT  i.animal_id,
        animal_type,
        name
  FROM  (
        SELECT  animal_id, animal_type, name
          FROM  animal_ins
         WHERE  INSTR(sex_upon_intake, 'Intact') > 0
        ) AS i JOIN
        (
        SELECT  animal_id
          FROM  animal_outs
         WHERE  sex_upon_outcome RLIKE 'Spayed|Neutered'
        ) AS o ON
        i.animal_id = o.animal_id
 ORDER
    BY  animal_id
;