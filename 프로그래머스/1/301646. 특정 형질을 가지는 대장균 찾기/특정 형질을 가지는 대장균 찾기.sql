-- 코드를 작성해주세요
SELECT COUNT(*) as COUNT
FROM ECOLI_DATA
WHERE (genotype & 5) > 0
    and (genotype & 2) = 0