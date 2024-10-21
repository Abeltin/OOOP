create table components(id int primary key auto_increment, name text)
create table structure(id_pc int, id_component int, amount int)

INSERT INTO tree.components (name) VALUES
	 ('Компьютер'),
	 ('Монитор'),
	 ('Системный блок'),
	 ('Корпус'),
	 ('Мат.плата'),
	 ('Жесткий диск'),
	 ('ОЗУ'),
	 ('Процессор'),
	 ('Клавиатура'),
	 ('Мышь');

INSERT INTO tree.`structure` (id_pc,id_component,amount) VALUES
	 (1,2,1),
	 (1,3,1),
	 (3,4,1),
	 (3,5,1),
	 (3,6,1),
	 (5,7,2),
	 (5,8,1),
	 (1,9,1),
	 (1,10,1);

DELIMITER $$
CREATE PROCEDURE GetComponentHierarchy()
BEGIN
    SELECT c1.id AS parent_id, c1.name AS parent_name, c2.id AS child_id, c2.name AS child_name, s.amount
    FROM components c1
    LEFT JOIN structure s ON c1.id = s.id_pc
    LEFT JOIN components c2 ON s.id_component = c2.id
    ORDER BY c1.id, c2.id;
END $$
DELIMITER ;
