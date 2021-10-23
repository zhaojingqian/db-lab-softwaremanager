
-- 不存在有一种软件，（课程所拥有的软件），实验室没有这种软件
select distinct l1.lab_id, l1.lab_address 
from lab as l1, software_have as sh1, software as s1
where l1.lab_id=sh1.lab_id and s1.software_id=sh1.software_id and not exists
(select * from course as c1, software_need as sn1, software as s2
where c1.course_id=sn1.course_id and s2.software_id=sn1.software_id and c1.course_id=4 and not exists
(select * from lab as l2, software_have as sh2, software as s3 where l2.lab_id=l1.lab_id and l2.lab_id=sh2.lab_id and s3.software_id=sh2.software_id
and s3.software_id=s2.software_id))

CREATE DEFINER=`root`@`localhost` TRIGGER `lab_course_BEFORE_INSERT` BEFORE INSERT ON `lab_course` FOR EACH ROW BEGIN
	if new.lab_id not in (select distinct l1.lab_id
from lab as l1, software_have as sh1, software as s1
where l1.lab_id=sh1.lab_id and s1.software_id=sh1.software_id and not exists
(select * from course as c1, software_need as sn1, software as s2
where c1.course_id=sn1.course_id and s2.software_id=sn1.software_id and c1.course_id=new.course_id and not exists
(select * from lab as l2, software_have as sh2, software as s3 where l2.lab_id=l1.lab_id and l2.lab_id=sh2.lab_id and s3.software_id=sh2.software_id
and s3.software_id=s2.software_id)))
then signal sqlstate'45000'set message_text='invalid insert!';
end if;
END

