CREATE DATABASE IF NOT EXISTS inf_enterpr;
USE inf_enterpr;

-- Каждый из магазинов сети характеризуется своим названием и адресом, а также ассортимен-том продаваемых товаров
-- (с указанием названия товара, единицы измерения и количества на складе по каждой позиции).
-- Магазины
CREATE TABLE IF NOT EXISTS scores
(
    id      INT          NOT NULL AUTO_INCREMENT,
    title   VARCHAR(255) NOT NULL,
    address TEXT         NOT NULL,
    PRIMARY KEY (id)
);

-- По каждому поставщику товаров необходимо иметь в БД следующие сведения: название и ад-рес;
-- ФИО руководителя и его телефон; банк поставщика и расчетный счет в этом банке; ИНН поставщика.
-- Поставщики
CREATE TABLE IF NOT EXISTS providers
(
    id      INT          NOT NULL AUTO_INCREMENT,
    title   VARCHAR(255) NOT NULL,
    address TEXT         NOT NULL,
    head    VARCHAR(255) NOT NULL,
    phone   VARCHAR(255) NOT NULL,
    bank    VARCHAR(255) NOT NULL,
    bill    VARCHAR(20)  NOT NULL,
    inn     VARCHAR(20)  NOT NULL,
    PRIMARY KEY (id)
);

-- Запасы товаров, которые хранятся на центральном складе, описываются следующими рекви-зитами:
-- название; единица измерения; цена; остаток на складе; поставщик
-- Товары
CREATE TABLE IF NOT EXISTS goods
(
    id          INT          NOT NULL AUTO_INCREMENT,
    title       VARCHAR(255) NOT NULL,
    unit        VARCHAR(8)   NOT NULL,
    price       FLOAT        NOT NULL CHECK ( price > 0 ),
    provider_id INT          NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (provider_id) REFERENCES providers (id) ON UPDATE RESTRICT ON DELETE RESTRICT
);

-- Основной склад
CREATE TABLE IF NOT EXISTS main_storage
(
    id       INT   NOT NULL AUTO_INCREMENT,
    goods_id INT   NOT NULL,
    amount   FLOAT NOT NULL CHECK ( amount > 0 ),
    PRIMARY KEY (id),
    FOREIGN KEY (goods_id) REFERENCES goods (id) ON UPDATE RESTRICT ON DELETE RESTRICT
);

-- Склады магазинов
CREATE TABLE IF NOT EXISTS score_goods
(
    id       INT   NOT NULL AUTO_INCREMENT,
    score_id INT   NOT NULL,
    goods_id INT   NOT NULL,
    price    FLOAT NOT NULL CHECK ( price > 0 ),
    amount   FLOAT NOT NULL CHECK ( amount > 0 ),
    PRIMARY KEY (id),
    FOREIGN KEY (score_id) REFERENCES scores (id) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (goods_id) REFERENCES goods (id) ON UPDATE RESTRICT ON DELETE RESTRICT
);

-- При регистрации поступления товаров на центральный склад в БД требуется заносить следу-ющую информацию по каждой
-- поставке: поставщик; дата поставки; перечень полученных то-варов (с указанием названия, закупочной цены, единицы
-- измерения и количества для каждой позиции).
-- Доставки
CREATE TABLE IF NOT EXISTS deliveries
(
    id            INT NOT NULL AUTO_INCREMENT,
    provider_id   INT NOT NULL,
    delivery_date DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (id),
    FOREIGN KEY (provider_id) REFERENCES providers (id) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS delivery_details
(
    id          INT   NOT NULL AUTO_INCREMENT,
    goods_id    INT   NOT NULL,
    price       FLOAT NOT NULL CHECK ( price > 0 ),
    amount      FLOAT NOT NULL CHECK ( amount > 0 ),
    delivery_id INT   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (goods_id) REFERENCES goods (id) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (delivery_id) REFERENCES deliveries (id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Распределение товаров по магазинам сети осуществляется с помощью заявок. Для каждой за-явки в БД фиксируется:
-- название магазина; дата заявки; перечень заказанных товаров (с ука-занием названия, единицы измерения и количества
-- для каждой позиции)
-- Заявки
CREATE TABLE IF NOT EXISTS bids
(
    id       INT      NOT NULL AUTO_INCREMENT,
    score_id INT      NOT NULL,
    bid_date DATETIME NOT NULL DEFAULT NOW(),
    status   SMALLINT NOT NULL DEFAULT 0,
    PRIMARY KEY (id),
    FOREIGN KEY (score_id) REFERENCES scores (id) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS bid_details
(
    id       INT   NOT NULL AUTO_INCREMENT,
    bid_id   INT   NOT NULL,
    goods_id INT   NOT NULL,
    amount   FLOAT NOT NULL CHECK ( amount > 0 ),
    PRIMARY KEY (id),
    FOREIGN KEY (bid_id) REFERENCES bids (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (goods_id) REFERENCES goods (id) ON UPDATE RESTRICT ON DELETE RESTRICT
);

-- По каждому из продавцов требуется обеспечить хранение в БД следующих атрибутов: магазин и отдел; ФИО; пол; возраст и
-- адрес проживания; трудовой стаж; квалификация
-- Продавцы
CREATE TABLE IF NOT EXISTS sellers
(
    id            INT          NOT NULL AUTO_INCREMENT,
    score_id      INT          NOT NULL,
    surname       VARCHAR(64)  NOT NULL,
    name          VARCHAR(64)  NOT NULL,
    patronymic    VARCHAR(64),
    male          TINYINT      NOT NULL DEFAULT 1 CHECK ( male IN (0, 1) ),
    birth_date    DATE         NOT NULL,
    address       VARCHAR(255) NOT NULL,
    seniority     SMALLINT     NOT NULL DEFAULT 0 CHECK ( seniority >= 0 ),
    qualification VARCHAR(255),
    PRIMARY KEY (id),
    FOREIGN KEY (score_id) REFERENCES scores (id) ON UPDATE RESTRICT ON DELETE RESTRICT
);

-- Для учета сведений о выручке в БД постоянно фиксируется: дата; продавец; перечень продан-ных товаров (с указанием
-- названия, единицы измерения, количества и размера выручки по каждой позиции).
-- Продажи
CREATE TABLE IF NOT EXISTS sales
(
    id        INT      NOT NULL AUTO_INCREMENT,
    sale_date DATETIME NOT NULL DEFAULT NOW(),
    seller_id INT      NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (seller_id) REFERENCES sellers (id) ON UPDATE RESTRICT ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS sale_details
(
    id       INT   NOT NULL AUTO_INCREMENT,
    sale_id  INT   NOT NULL,
    goods_id INT   NOT NULL,
    amount   FLOAT NOT NULL CHECK ( amount > 0 ),
    PRIMARY KEY (id),
    FOREIGN KEY (sale_id) REFERENCES sales (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (goods_id) REFERENCES goods (id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Товары магазинов
CREATE VIEW main_storage_view AS
SELECT g.title, ms.amount, g.unit, g.price
FROM main_storage ms
         JOIN goods g on ms.goods_id = g.id
ORDER BY ms.id;

-- Товары магазинов
CREATE VIEW score_view AS
SELECT s.title score, g.title goods, sg.amount, g.unit, sg.price
FROM scores s
         JOIN score_goods sg on s.id = sg.score_id
         JOIN goods g on sg.goods_id = g.id
ORDER BY s.id, sg.id;

CREATE VIEW seller_view AS
SELECT CONCAT_WS(' ', s.surname, s.name, s.patronymic)     seller,
       DATE(sa.sale_date)                                  `date`,
       SUM(sd.amount * g.price)                            goods_cost,
       SUM(sd.amount * sg.price)                           sales,
       SUM((sd.amount * sg.price) - (sd.amount * g.price)) proceeds
FROM sellers s
         JOIN sales sa ON s.id = sa.seller_id
         JOIN sale_details sd ON sa.id = sd.sale_id
         JOIN goods g ON g.id = sd.goods_id
         JOIN score_goods sg ON sg.id = sd.goods_id
GROUP BY s.id, `date`
ORDER BY `date`, seller;
