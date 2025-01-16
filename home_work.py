 fname  
---------
 Derek
 Stacy
 Susan
 Lisa
 Michael
 William
 Eric
 Jandy
 David
 Dinesh
 Shiela
 Paul
 Jun
 Andy
 Ian
 Mark
 Linda
 Charles
 Bruce
 George
 Steven
 Tracy
 Sarah
 Arthur
(24 строки)

 stuid |  lname  |  fname  | age | sex 
-------+---------+---------+-----+-----
  1001 | Smith   | Linda   |  18 | F
  1006 | Schultz | Andy    |  18 | M
  1007 | Apap    | Lisa    |  18 | F
  1014 | Norris  | Charles |  18 | M
  1019 | Pang    | Arthur  |  18 | M
  1024 | Prater  | Stacy   |  18 | F
  1025 | Goldman | Mark    |  18 | M
  1027 | Brody   | Paul    |  18 | M
  1033 | Simms   | William |  18 | M
  1034 | Epp     | Eric    |  18 | M
(10 строк)

stuid |  lname   |  fname  | age | sex 
-------+----------+---------+-----+-----
  1011 | Adams    | David   |  30 | M
  1017 | Wilson   | Bruce   |  27 | M
  1005 | Gompers  | Paul    |  26 | M
  1035 | Schmidt  | Sarah   |  26 | F
  1020 | Thornton | Ian     |  22 | M
  1003 | Jones    | Shiela  |  21 | F
  1030 | Cheng    | Lisa    |  21 | F
  1012 | Davis    | Steven  |  20 | M
  1008 | Nelson   | Jandy   |  20 | F
  1028 | Rugh     | Eric    |  20 | M
  1031 | Smith    | Sarah   |  20 | F
  1023 | Shieber  | David   |  20 | M
  1032 | Brown    | Eric    |  20 | M
  1004 | Kumar    | Dinesh  |  20 | M
  1018 | Leighton | Michael |  20 | M
  1021 | Andreou  | George  |  19 | M
  1026 | Pang     | Eric    |  19 | M
  1009 | Tai      | Eric    |  19 | M
  1002 | Kim      | Tracy   |  19 | F
  1006 | Schultz  | Andy    |  18 | M
  1007 | Apap     | Lisa    |  18 | F
  1014 | Norris   | Charles |  18 | M
  1019 | Pang     | Arthur  |  18 | M
  1001 | Smith    | Linda   |  18 | F
  1024 | Prater   | Stacy   |  18 | F
  1025 | Goldman  | Mark    |  18 | M
  1027 | Brody    | Paul    |  18 | M
  1033 | Simms    | William |  18 | M
  1034 | Epp      | Eric    |  18 | M
  1016 | Schwartz | Mark    |  17 | M
  1010 | Lee      | Derek   |  17 | M
  1029 | Han      | Jun     |  17 | M
  1022 | Woods    | Michael |  17 | M
  1015 | Lee      | Susan   |  16 | F
  (34 строки)

 stuid |  lname  | fname  | age | sex 
-------+---------+--------+-----+-----
  1001 | Smith   | Linda  |  18 | F
  1002 | Kim     | Tracy  |  19 | F
  1003 | Jones   | Shiela |  21 | F
  1004 | Kumar   | Dinesh |  20 | M
  1005 | Gompers | Paul   |  26 | M
(5 строк)

update student set age=(select max(age) from student where gender='F') where stuid=1012;

Жума, [16/1/25 14:11]
 count 
-------
    10
(1 строка)

 total_weight 
--------------
        37.70
(1 строка)

     avarage_age     
---------------------
 19.7941176470588235
(1 строка)

 stuid |  lname   |  fname  | age | sex 
-------+----------+---------+-----+-----
  1001 | Smith    | Linda   |  18 | F
  1006 | Schultz  | Andy    |  18 | M
  1016 | Schwartz | Mark    |  17 | M
  1023 | Shieber  | David   |  20 | M
  1031 | Smith    | Sarah   |  20 | F
  1033 | Simms    | William |  18 | M
  1035 | Schmidt  | Sarah   |  26 | F
(7 строк)

 stuid | lname | fname  | age | sex 
-------+-------+--------+-----+-----
  1001 | Smith | Linda  |  18 | F
  1002 | Kim   | Tracy  |  19 | F
  1003 | Jones | Shiela |  21 | F
(3 строки)

1001 | Smith    | Linda   |  18 | F
  1002 | Kim      | Tracy   |  19 | F
  1004 | Kumar    | Dinesh  |  20 | M
  1006 | Schultz  | Andy    |  18 | M
  1007 | Apap     | Lisa    |  18 | F
  1008 | Nelson   | Jandy   |  20 | F
  1009 | Tai      | Eric    |  19 | M
  1012 | Davis    | Steven  |  20 | M
  1014 | Norris   | Charles |  18 | M
  1018 | Leighton | Michael |  20 | M
  1019 | Pang     | Arthur  |  18 | M
  1021 | Andreou  | George  |  19 | M
  1023 | Shieber  | David   |  20 | M
  1024 | Prater   | Stacy   |  18 | F
  1025 | Goldman  | Mark    |  18 | M
  1026 | Pang     | Eric    |  19 | M
  1027 | Brody    | Paul    |  18 | M
  1028 | Rugh     | Eric    |  20 | M
  1031 | Smith    | Sarah   |  20 | F
  1032 | Brown    | Eric    |  20 | M
  1033 | Simms    | William |  18 | M
  1034 | Epp      | Eric    |  18 | M
  (22 строки)

student_age 
-------------
          18
          19
          21
          20
          26
          18
          18
          20
          19
          17
          20
          18
          16
          17
          27
          20
          18
          22
          19
          17
          20
          18
          16
          17
          27
          20
          18
          22
          19
          17
          20
          18
          18
          19
          18
          20
          17
          21
          20
          20
          18
          18
          26
          30
          (34  строки)