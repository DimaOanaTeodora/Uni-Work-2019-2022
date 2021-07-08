--Dima Oana-Teodora 241 Tema 2: 5 nov 2020
--ex4
DECLARE 
  nume member.last_name%type := '&nume';
  numar number;
  id_membru member.member_id%type;
  total number;
  procent number;
BEGIN
     select member_id
     into id_membru
     from member
     where upper(last_name) = upper(nume);
 
     select count(distinct title_id)
     into numar
     from rental r join member m on(r.member_id = m.member_id)
     where upper(m.last_name) = upper(nume);
     
     select count(*)
     into total
     from title;
     
     procent:=numar *100 / total;
     
     if procent >75 then
        DBMS_OUTPUT.PUT_LINE('Membrul ' || Initcap(nume) || ' face parte din categoria 1 cu ' || round(procent,1) || '% imprumutat din titlurile existente');
     elsif procent >50 then
            DBMS_OUTPUT.PUT_LINE('Membrul ' || Initcap(nume) || ' face parte din categoria 2 cu ' || round(procent,1) || '% imprumutat din titlurile existente');
     elsif procent>25 then
     DBMS_OUTPUT.PUT_LINE('Membrul ' || Initcap(nume) || ' face parte din categoria 3 cu ' || round(procent,1) || '% imprumutat din titlurile existente');
     elsif procent =0 then
     DBMS_OUTPUT.PUT_LINE('Membrul ' || Initcap(nume) || ' face parte din categoria 4 si nu a imprumutat nimic ');
     else
     DBMS_OUTPUT.PUT_LINE('Membrul ' || Initcap(nume) || ' face parte din catgoria 4 cu ' || round(procent,1) || '% imprumutat din titlurile existente');
     end if;
 
exception
    when no_data_found then DBMS_OUTPUT.PUT_LINE('Nu exista acest membru.');
    when too_many_rows then DBMS_OUTPUT.PUT_LINE('Exista mai multi membrii cu numele '||nume ||'.');
 
end;
/
--ex5
create table member_odi as select * from member;
select * from member_odi;
alter table member_odi
add (discount number);

DECLARE 

  numar number;
  id_membru member.member_id%type;
  total number;
  procent number;
BEGIN
     for i in 101..110 loop
    
         select count(distinct title_id)
         into numar
         from rental 
         where member_id=id_membru;
         
         select count(*)
         into total
         from title;
         
         procent:=numar *100 / total;
         
         if procent >75 then
            update member_odi
                set discount =10
                where member_id=id_membru;
         elsif procent >50 then
                update member_odi
                set discount =5
                where member_id=id_membru;
         elsif procent>25 then
                 update member_odi
                set discount =3
                where member_id=id_membru;
         end if;
    
    end loop;
 
end;
/
DECLARE 
  
  numar number;
  id_membru member.member_id%type := '&id';
  total number;
  procent number;
BEGIN
   
 
     select count(distinct title_id)
     into numar
     from rental r 
     where member_id=id_membru;
     
     select count(*)
     into total
     from title;
     
     procent:=numar *100 / total;
     
     if procent >75 then
            DBMS_OUTPUT.PUT_LINE('Actulizarea s-a produs cu succes');
            update member_odi
                set discount =10
                where member_id=id_membru;
         elsif procent >50 then
         DBMS_OUTPUT.PUT_LINE('Actulizarea s-a produs cu succes');
                update member_odi
                set discount =5
                where member_id=id_membru;
         elsif procent>25 then
         DBMS_OUTPUT.PUT_LINE('Actulizarea s-a produs cu succes');
                 update member_odi
                set discount =3
               where member_id=id_membru;
         else
         DBMS_OUTPUT.PUT_LINE('Actulizarea nu s-a produs');
         end if;
exception
    when no_data_found then DBMS_OUTPUT.PUT_LINE('Nu exista acest id.Actualizarea nu s-a produs');    
end;
