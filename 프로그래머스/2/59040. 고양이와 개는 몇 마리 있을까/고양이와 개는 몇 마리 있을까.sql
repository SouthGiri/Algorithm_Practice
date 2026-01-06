-- 코드를 입력하세요
SELECT animal_type, count(*)
FROM animal_ins
WHERE animal_type = 'cat' or animal_type = 'dog'
GROUP BY animal_type
ORDER BY animal_type