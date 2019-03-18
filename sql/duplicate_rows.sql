Select * 
from emp a 
where rowid <> ( select max(rowid) 
                from emp b 
                where a.empno = b.empno
                );
