--	создание таблиц учебной БД
--
-- 	создание таблицы туристических агентств AGEN
create table if not exists nd.agen
(
    aid    int(4),
    aname  varchar(30),
    city   varchar(30),
    rating int,
    primary key (aid)
);
-- 	создание таблицы туров - TOUR
create table if not exists nd.tour
(
    tid     int(4),
    tname   varchar(30),
    country varchar(30),
    tclass  int(2),
    aid     int(4),
    primary key (tid)
);
-- 	создание таблицы доходов - BUS
create table if not exists nd.bus
(
    bid   int(4),
    bdate date,
    amt   int,
    aid   int(4),
    tid   int(4)
);
--	определение первичного ключа таблицы agen
# ALTER TABLE nd.agen
#     ADD (CONSTRAINT pk_agn PRIMARY KEY (aid));
--	определение первичного и внешнего ключей таблицы tour
# ALTER TABLE tour
#     ADD (CONSTRAINT pk_tou PRIMARY KEY (tid), CONSTRAINT fk_ta FOREIGN KEY (aid)
#         REFERENCES agen(aid));
ALTER TABLE nd.tour
    Add CONSTRAINT fk_ta FOREIGN KEY (aid) REFERENCES agen(aid);
--	определение первичного и внешних ключей таблицы bus
# ALTER TABLE bus
#     ADD (CONSTRAINT pk_bus PRIMARY KEY (bid),
#         CONSTRAINT fk_ba FOREIGN KEY (aid) REFERENCES agen(aid),
#         CONSTRAINT fk_bt FOREIGN KEY (tid) REFERENCES tour(tid));

# drop index fk_ba on bus;
# drop index fk_bt on bus;
#
# alter table bus
#     drop foreign key fk_ba,
#     drop foreign key fk_bt;

ALTER TABLE nd.bus
    Add CONSTRAINT fk_ba FOREIGN KEY (aid) REFERENCES agen(aid),
    ADD CONSTRAINT fk_bt FOREIGN KEY (tid) REFERENCES tour(tid);
