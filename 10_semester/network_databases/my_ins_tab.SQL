--	Заполнение таблиц учебной БД
--
--
--	заполнение таблицы agen
--
INSERT INTO nd.agen(aid,aname,city,rating)
  VALUES(101,'Irtysh','Omsk',50);
INSERT INTO nd.agen(aid,aname,city,rating)
  VALUES(102,'Vostok','Novosibisk',50);
INSERT INTO nd.agen(aid,aname,city,rating)
  VALUES(104,'Ermak','Omsk',45);
INSERT INTO nd.agen(aid,aname,city,rating)
  VALUES(106,'Valday','Moscow',60);
INSERT INTO nd.agen(aid,aname,city,rating)
  VALUES(107,'Kedr','Tomsk',45);
INSERT INTO nd.agen(aid,aname,city,rating)
  VALUES(108,'Saltan','Samara',55);
--
--	заполнение таблицы tour
--
INSERT INTO nd.tour(tid,tname,country,tclass,aid)
  VALUES(201,'Grate Wall','China',2,102);
INSERT INTO nd.tour(tid,tname,country,tclass,aid)
  VALUES(202,'Sea Star','Italy',1,101);
INSERT INTO nd.tour(tid,tname,country,tclass,aid)
  VALUES(203,'Pattaya','Thailand',4,107);
INSERT INTO nd.tour(tid,tname,country,tclass,aid)
  VALUES(205,'Attica','Greece',3,108);
INSERT INTO nd.tour(tid,tname,country,tclass,aid)
  VALUES(206,'Paris','France',1,106);
INSERT INTO nd.tour(tid,tname,country,tclass,aid)
  VALUES(208,'Alvor','Portugal',1,104);
INSERT INTO nd.tour(tid,tname,country,tclass,aid)
  VALUES(209,'Majorka','Spain',1,106);
INSERT INTO nd.tour(tid,tname,country,tclass,aid)
  VALUES(210,'Antalya','Turkey',2,106);
INSERT INTO nd.tour(tid,tname,country,tclass,aid)
  VALUES(211,'Red Sea','Egypt',4,102);
--
--	заполнение таблицы bus
--
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(301,'2019-03-31',2500,101,202);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(302,'2019-03-31',1770.5,107,203);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(303,'2019-06-30',905.4,102,201);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(304,'2019-03-31',3300,102,211);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(305,'2019-12-31',55.9,108,205);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(306,'2019-03-31',9707.1,104,208);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(307,'2019-06-30',777.5,106,209);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(308,'2019-09-30',8097,101,202);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(309,'2019-09-30',8011.1,106,210);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(310,'2019-12-31',4455.6,106,206);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(311,'2019-09-30',7545,102,211);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(312,'2019-09-30',9876.5,104,208);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(313,'2019-09-30',8765.2,107,203);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(314,'2019-09-30',8899.3,108,205);
INSERT INTO nd.bus(bid,bdate,amt,aid,tid)
  VALUES(315,'2019-12-31',5454.3,102,211);
--
# COMMIT;
# --
# --
# --     AID ANAME       CITY          RATING
# ---------- ----------- ------------ -------
# --     101 Irtysh      Omsk              50
# --     102 Vostok      Novosibisk        50
# --     104 Ermak       Omsk              45
# --     106 Valday      Moscow            60
# --     107 Kedr        Tomsk             45
# --     108 Saltan      Samara            55
# --
# --     TID TNAME          COUNTRY     TCLASS     AID
# ---------- -------------- ----------- ------ -------
# --     201 Grate Wall     China            2     102
# --     202 Sea Star       Italy            1     101
# --     203 Pattaya        Thailand         4     107
# --     205 Attica         Greece           3     108
# --     206 Paris          France           1     106
# --     208 Alvor          Portugal         1     104
# --     209 Majorka        Spain            1     106
# --     210 Antalya        Turkey           2     106
# --     211 Red Sea        Egypt            4     102
# --
# --     BID       BDATE       AMT       AID       TID
# ---------- ----------- --------- --------- ---------
# --     301  31.03.2019      2500       101       202
# --     302  31.03.2019    1770,5       107       203
# --     303  30.06.2019     905,4       102       201
# --     304  31.03.2019      3300       102       211
# --     305  31.12.2019      55,9       108       205
# --     306  31.03.2019    9707,1       104       208
# --     307  30.06.2019     777,5       106       209
# --     308  30.09.2019      8097       101       202
# --     309  30.09.2019    8011,1       106       210
# --     310  31.12.2019    4455,6       106       206
# --     311  30.09.2019      7545       102       211
# --     312  30.09.2019    9876,5       104       208
# --     313  30.09.2019    8765,2       107       203
# --     314  30.09.2019    8899,3       108       205
# --     315  31.12.2019    5454,3       102       211
# --
# select * from nd.agen;
# select * from nd.tour;
# select * from nd.bus;
