psql -U postgres
create schema qrio;
    ALTER SCHEMA qrio OWNER TO jann;
CREATE USER jann WITH SUPERUSER PASSWORD '@dmin098';

drop table person;

create table person (
	id SERIAL primary key,
	firstname VARCHAR(100) not null,
	lastname VARCHAR(100) not null,
	age INT,
	active bool default true
)

--CREATE
insert into person (firstname, lastname, age)
values ('Jann','Mercado', 22);

--READ
select * from person;

--UPDATE
update person
set age =23
where id = 1;

--DELETE
delete from person where  AGE >= 23;