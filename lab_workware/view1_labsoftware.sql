CREATE VIEW `lab_software` AS
select  t.lab_id, lab_address, equipment_config, group_concat(software_name order by software_name asc separator ',') as software from
(select lab.lab_id, lab_address, equipment_config, software_name
from software, software_have, lab, equipment 
where lab.lab_id=software_have.lab_id and software.software_id=software_have.software_id and lab.equipment_id=equipment.equipment_id) as t
group by lab_address;