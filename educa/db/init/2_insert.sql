insert into en_words 
  select * from ( values 
  ( 1, 'Word1', '訳1'),
  ( 2, 'Word2', '訳2'),
  ( 3, 'Word3', '訳3'),
  ( 4, 'Word4', '訳4'),
  ( 5, 'Word5', '訳5'),
  ( 6, 'Word6', '訳6'),
  ( 7, 'Word7', '訳7'),
  ( 8, 'Word8', '訳8'),
  ( 9, 'Word9', '訳9'),
  ( 10, 'Word10', '訳10'),
  ( 11, 'Word11', '訳11'),
  ( 12, 'Word12', '訳12'),
  ( 13, 'Word13', '訳13'),
  ( 14, 'Word14', '訳14'),
  ( 15, 'Word15', '訳15')
  ) as new ( Num, Word, Meaning ) 
    where not exists (select * from en_words where Num = new.Num) ;

insert into kobun_words 
  select * from ( values 
  ( 1, 'ことば壱', '訳1'),
  ( 2, 'ことば弐', '訳2'),
  ( 3, 'ことば参', '訳3'),
  ( 4, 'ことば肆', '訳4'),
  ( 5, 'ことば伍', '訳5'),
  ( 6, 'ことば陸', '訳6'),
  ( 7, 'ことば漆', '訳7'),
  ( 8, 'ことば捌', '訳8'),
  ( 9, 'ことば玖', '訳9'),
  ( 10, 'ことば拾', '訳10')
  ) as new ( Num, Word, Meaning ) 
    where not exists (select * from kobun_words where Num = new.Num) ;
