SELECT
    SUM(score) as SCORE,
    e.emp_no,
    emp_name,
    position,
    email
FROM
    hr_employees as e JOIN
    hr_grade as g
    ON e.emp_no = g.emp_no
WHERE
    year = 2022
GROUP BY
    e.emp_no
ORDER BY
    SCORE DESC
LIMIT 1
;