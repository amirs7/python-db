CREATE TABLE author
(
    id        int(11) NOT NULL AUTO_INCREMENT,
    firstname varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE book
(
    id   int(11) NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE bookauthor
(
    id        int(11) NOT NULL AUTO_INCREMENT,
    book_id   int(11) NOT NULL,
    author_id int(11) NOT NULL,
    PRIMARY KEY (id),
    KEY       bookauthor_book_id (book_id),
    KEY       bookauthor_author_id (author_id),
    CONSTRAINT bookauthor_ibfk_1 FOREIGN KEY (book_id) REFERENCES book (id),
    CONSTRAINT bookauthor_ibfk_2 FOREIGN KEY (author_id) REFERENCES author (id)
);

INSERT INTO author VALUES (1, 'amir');
INSERT INTO book VALUES(1, 'b1');
INSERT INTO book VALUES(2, 'b2');
INSERT INTO bookauthor(book_id, author_id) VALUES(1, 1);
INSERT INTO bookauthor(book_id, author_id) VALUES(2, 1);


