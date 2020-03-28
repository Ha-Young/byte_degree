BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT,     email TEXT, phone TEXT, website TEXT, regdate TEXT);
INSERT INTO "users" VALUES(1,'Kim','Kim@naver.com','010-9999-9999','Kim.com','2020-02-08 01:29:56');
INSERT INTO "users" VALUES(2,'Park','Park@daum.net','010-1111-1111','Park.com','2020-02-08 01:29:56');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2020-02-08 01:29:56');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-3333-3333','Cho.com','2020-02-08 01:29:56');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@gmail.com','010-4444-4444','Yoo.com','2020-02-08 01:29:56');
COMMIT;
