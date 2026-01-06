-- 코드를 입력하세요
SELECT animal_id, name,
    CASE
        WHEN sex_upon_intake LIKE '%Neutered%' THEN 'O'
        WHEN INSTR(sex_upon_intake, 'Spayed') > 0 THEN 'O'
        ELSE 'X'
    END as '중성화'
FROM animal_ins