USE inf_enterpr;

insert into scores (id, title, address) values (1, 'Первый магазин', 'Красный проспект, 26');
insert into scores (id, title, address) values (2, 'Второй магазин', 'Октябрьская, 50');

insert into providers (id, title, address, head, phone, bank, bill, inn) values (1, 'Первый поставщик', 'Мичурина, 22', 'Вася', 02, 'Сбербанк', 111111, 1111111);
insert into providers (id, title, address, head, phone, bank, bill, inn) values (2, 'Второй поставщик', 'Кирова, 44', 'Игорь', 03, 'Альфа', 222222, 2222222);

insert into goods (id, title, unit, price, provider_id, amount) values (1, 'Зубная щетка', 'шт', 10, 1, 100);
insert into goods (id, title, unit, price, provider_id, amount) values (2, 'Зубная паста', 'шт', 15, 1, 150);
insert into goods (id, title, unit, price, provider_id, amount) values (3, 'Молоко', 'шт', 50, 2, 50);
insert into goods (id, title, unit, price, provider_id, amount) values (4, 'Кефир', 'шт', 25, 2, 30);

insert into score_goods (score_id, goods_id, price, amount) values (1, 1, 15, 10);
insert into score_goods (score_id, goods_id, price, amount) values (1, 2, 25, 15);
insert into score_goods (score_id, goods_id, price, amount) values (1, 3, 70, 20);
insert into score_goods (score_id, goods_id, price, amount) values (1, 4, 50, 10);

insert into deliveries (id, provider_id, delivery_date) values (1, 1, '2020-11-30 18:13:45');
insert into deliveries (id, provider_id, delivery_date) values (2, 2, '2020-11-30 18:13:53');

insert into delivery_details (goods_id, price, amount, delivery_id) values (1, 10, 10, 1);
insert into delivery_details (goods_id, price, amount, delivery_id) values (2, 15, 10, 1);
insert into delivery_details (goods_id, price, amount, delivery_id) values (3, 50, 10, 2);
insert into delivery_details (goods_id, price, amount, delivery_id) values (4, 25, 10, 2);

insert into bids (id, score_id, bid_date, status) values (1, 1, '2020-12-01 15:32:02', 0);
insert into bids (id, score_id, bid_date, status) values (2, 2, '2020-12-01 15:32:07', 0);

insert into bid_details (bid_id, goods_id, amount) values (1, 1, 5);
insert into bid_details (bid_id, goods_id, amount) values (1, 2, 5);
insert into bid_details (bid_id, goods_id, amount) values (1, 3, 5);
insert into bid_details (bid_id, goods_id, amount) values (2, 2, 10);
insert into bid_details (bid_id, goods_id, amount) values (2, 3, 10);
insert into bid_details (bid_id, goods_id, amount) values (2, 4, 10);

insert into sellers (id, score_id, surname, name, patronymic, male, birth_date, address, seniority, qualification) values (1, 1, 'Иванов', 'Иван', 'Иванович', 1, '1969-12-01', 'Новосибирск', 0, null);
insert into sellers (id, score_id, surname, name, patronymic, male, birth_date, address, seniority, qualification) values (2, 2, 'Петров', 'Петр', 'Петрович', 1, '1985-08-08', 'Новосибирск', 0, null);

insert into sales (id, sale_date, seller_id) values (1, '2020-12-02 18:12:18', 1);
insert into sales (id, sale_date, seller_id) values (2, '2020-12-02 16:12:18', 2);
insert into sales (id, sale_date, seller_id) values (3, '2020-12-02 16:12:18', 1);
insert into sales (id, sale_date, seller_id) values (4, '2020-11-29 16:12:18', 1);

insert into sale_details (sale_id, goods_id, amount) values (1, 1, 2);
insert into sale_details (sale_id, goods_id, amount) values (1, 2, 1);
insert into sale_details (sale_id, goods_id, amount) values (2, 3, 2);
insert into sale_details (sale_id, goods_id, amount) values (2, 4, 1);
insert into sale_details (sale_id, goods_id, amount) values (3, 1, 10);
insert into sale_details (sale_id, goods_id, amount) values (3, 2, 10);
insert into sale_details (sale_id, goods_id, amount) values (3, 3, 10);
insert into sale_details (sale_id, goods_id, amount) values (3, 4, 10);
insert into sale_details (sale_id, goods_id, amount) values (4, 1, 5);
insert into sale_details (sale_id, goods_id, amount) values (4, 2, 5);
insert into sale_details (sale_id, goods_id, amount) values (4, 3, 5);
insert into sale_details (sale_id, goods_id, amount) values (4, 4, 5);
