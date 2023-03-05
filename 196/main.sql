DELETE from Person out_table
where email in (
    SELECT email from (
    SELECT email
    from Person
    group by email
    having count(email) > 1) t)
and id > (
    SELECT min_id from (
    SELECT min(id) as min_id
    from Person in_table
    where out_table.email = in_table.email) t);
