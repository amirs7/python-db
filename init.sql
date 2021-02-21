CREATE TABLE book (
  id bigint(20) NOT NULL,
  name varchar(25) DEFAULT NULL,
  author varchar(25) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO book VALUES(1, 'book1', 'author1');
