SELECT  APNT_NO,
        PT_NAME,
        A.PT_NO,
        A.MCDP_CD,
        DR_NAME,
        APNT_YMD
  FROM  APPOINTMENT A
        JOIN DOCTOR D
        ON A.MDDR_ID = D.DR_ID
        JOIN PATIENT P
        ON A.PT_NO = P.PT_NO
 WHERE  LEFT(APNT_YMD, 10) = '2022-04-13'
        AND APNT_CNCL_YN = 'N'
 ORDER
    BY  APNT_YMD
;