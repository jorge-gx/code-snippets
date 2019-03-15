/*
Extracting date from term description, uses regex. 
Term tables from PeopleSoft Campus Solutions
*/

/* using PS_TERM_VAL_TBL */
SELECT distinct PS_TERM_VAL_TBL.STRM
		,PS_TERM_VAL_TBL.DESCR
		,regexp_instr(PS_TERM_VAL_TBL.DESCR,'[[:digit:]]') as First_Digit_Pos  -- gets the position of the first Digit from left to right
		,substr(PS_TERM_VAL_TBL.DESCR , regexp_instr(PS_TERM_VAL_TBL.DESCR,'[[:digit:]]')) as Year_Data -- extracting year data starting from first digit position
FROM PS_SSR_TSRSLT_TRM, PS_TERM_VAL_TBL
WHERE  PS_TERM_VAL_TBL.STRM = PS_SSR_TSRSLT_TRM.STRM
AND PS_SSR_TSRSLT_TRM.STRM in ('3090', '3091', '3093', '3095')
order by PS_TERM_VAL_TBL.STRM;

/* using PS_TERM_TBL */
SELECT distinct STRM
		,DESCR
		,regexp_instr(DESCR,'[[:digit:]]') as First_Digit_Pos  -- gets the position of the first Digit from left to right
		,substr(DESCR , regexp_instr(DESCR,'[[:digit:]]')) as Year_Data -- extracting year data starting from first digit position
FROM PS_TERM_TBL
order by STRM;
