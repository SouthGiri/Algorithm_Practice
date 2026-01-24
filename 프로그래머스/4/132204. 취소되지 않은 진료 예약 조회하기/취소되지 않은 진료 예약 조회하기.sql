SELECT  apnt_no,
        p.pt_name,
        a.pt_no,
        a.mcdp_cd,
        d.dr_name,
        apnt_ymd
  FROM  appointment AS a JOIN
        patient AS p ON
        a.pt_no = p.pt_no JOIN
        doctor AS d ON
        a.mddr_id = d.dr_id
 WHERE  1=1
        AND LEFT(apnt_ymd, 10) = '2022-04-13'
        AND apnt_cncl_yn = 'N'
 ORDER
    BY  apnt_ymd
;