-- docker exec -it db_1 bash
-- mysql -u spark -p
USE spark;

CREATE TABLE IF NOT EXISTS assignment_1
(
  result float not null
  
);
CREATE TABLE IF NOT EXISTS assignment_2
(
  result float not null
  
);

CREATE TABLE IF NOT EXISTS assignment_4
(
  result float not null
  
);


CREATE TABLE IF NOT EXISTS assignment_3 (   result float not null, sex varchar(7) not null    );
CREATE TABLE IF NOT EXISTS assignment_5 (   result float not null, sex varchar(7) not null   );
CREATE TABLE IF NOT EXISTS assignment_6 (   result float not null, sex varchar(7) not null,   Pclass int );
