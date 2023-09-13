create table if not exists educa_accounts (
  educaID varchar(255) NOT NULL,
  PASS varchar(255) NOT NULL,
  username varchar(255) NOT NULL,
  PRIMARY KEY (educaID)
);

create table if not exists en_words (
  Num int NOT NULL,
  Word varchar(255) NOT NULL,
  Meaning varchar(255) NOT NULL,
  PRIMARY KEY (Num)
);

create table if not exists kobun_words (
  Num int NOT NULL,
  Word varchar(255) NOT NULL,
  Meaning varchar(255) NOT NULL,
  PRIMARY KEY (Num)
);

create table if not exists educa_rooms (
  roomID varchar(255) NOT NULL,
  roomPASS varchar(255) NOT NULL,
  roomname varchar(255) NOT NULL,
  educaID varchar(255) NOT NULL,
  PRIMARY KEY (roomID),
  FOREIGN KEY(educaID) REFERENCES educa_accounts(educaID)
);

create table if not exists room_members (
  roomID varchar(255) NOT NULL,
  member varchar(255) NOT NULL,
  FOREIGN KEY(roomID) REFERENCES educa_rooms(roomID)
);
