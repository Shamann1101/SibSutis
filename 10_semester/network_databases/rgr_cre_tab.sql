create database if not exists rgr;

create table if not exists rgr.agency
(
    id      int not null auto_increment,
    title   varchar(30),
    city    varchar(30),
    capital int,
    primary key (id)
);

create table if not exists rgr.service
(
    id     int not null auto_increment,
    title  varchar(30),
    cost   int,
    agency int,
    primary key (id),
    foreign key (agency) references rgr.agency (id) on update cascade on delete cascade
);

create view rgr.`short` as
select se.id, se.title, se.cost, ag.title as agency
from rgr.agency ag
         join rgr.service se on ag.id = se.agency
order by se.cost;

create procedure rgr.clear_tables()
begin
    delete
    from rgr.agency;
    delete
    from rgr.service;
end;

create procedure rgr.drop_schema()
begin
    drop schema if exists rgr;
end;

create procedure rgr.get_more_than(in value int)
begin
    SELECT a.title, SUM(cost) as cost_sum
    FROM service
             join agency a on service.agency = a.id
    GROUP BY agency
    having cost_sum > value;
end;