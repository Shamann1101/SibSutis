create procedure rgr.fill_tables()
begin
    insert into rgr.agency (id, title, city, capital)
    values (1, 'Agency#1', 'Novosibirsk', 1000),
           (2, 'Agency#2', 'Novosibirsk', 2000),
           (3, 'Agency#3', 'Moscow', 1000),
           (4, 'Agency#4', 'Omsk', 3000),
           (5, 'Agency#5', 'Tomsk', 2000)
    on duplicate key update id=id;

    insert into rgr.service (title, cost, agency)
    values ('Shield 3*6', 1000, 1),
           ('Stretching', 500, 1),
           ('Flip chart', 300, 1),
           ('Prizm', 300, 1),
           ('Stretching', 500, 2),
           ('Flip chart', 300, 4),
           ('Prizm', 300, 4),
           ('Stretching', 500, 4),
           ('Flip chart', 300, 2),
           ('Prizm', 300, 2),
           ('Pointer', 100, 3),
           ('Prizm', 300, 3),
           ('Stretching', 500, 5),
           ('Flip chart', 300, 5),
           ('Prizm', 300, 5),
           ('Pointer', 100, 5),
           ('Prizm', 300, 5),
           ('Pointer', 100, 5);
end;

call rgr.fill_tables();

create procedure rgr.delete_service(in se_title varchar(30))
begin
    delete from rgr.service where title = se_title;
end;