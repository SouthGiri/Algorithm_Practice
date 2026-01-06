-- 코드를 입력하세요
SELECT mcdp_cd as '진료과 코드', count(apnt_no) as '5월예약건수'
FROM appointment
WHERE LEFT(apnt_ymd, 7) = '2022-05'
GROUP BY mcdp_cd
ORDER BY count(apnt_no), mcdp_cd