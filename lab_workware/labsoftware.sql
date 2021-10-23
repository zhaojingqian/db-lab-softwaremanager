/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2021/10/19 11:24:30                          */
/*==============================================================*/


drop schema if exists labsoftware;
create schema labsoftware;
use labsoftware;

/*==============================================================*/
/* Table: administrator                                         */
/*==============================================================*/
create table administrator
(
   admin_id             int not null,
   user_id              int not null,
   admin_name           char(20) not null,
   admin_sex            char(10),
   admin_connect        char(20),
   primary key (admin_id)
);

/*==============================================================*/
/* Table: course                                                */
/*==============================================================*/
create table course
(
   course_id            int not null,
   course_name          char(20) not null,
   department           char(20) not null,
   course_period        int not null,
   course_amount        int,
   primary key (course_id)
);

/*==============================================================*/
/* Table: equipment                                             */
/*==============================================================*/
create table equipment
(
   equipment_id         int not null,
   equipment_type       char(20),
   equipment_config     text not null,
   equipment_os         char(20),
   equipment_scale      int not null,
   primary key (equipment_id)
);

/*==============================================================*/
/* Table: lab                                                   */
/*==============================================================*/
create table lab
(
   lab_id               int not null,
   equipment_id         int,
   admin_id             int not null,
   lab_address          char(20) not null,
   lab_scale            int not null,
   primary key (lab_id)
);

/*==============================================================*/
/* Table: lab_course                                            */
/*==============================================================*/
create table lab_course
(
   course_id            int not null,
   lab_id               int not null,
   primary key (course_id, lab_id)
);

/*==============================================================*/
/* Table: software                                              */
/*==============================================================*/
create table software
(
   software_id          int not null,
   software_name        char(20) not null,
   software_version     char(20),
   software_type        char(20),
   software_arch        char(20),
   software_memory      int,
   software_info        text,
   primary key (software_id)
);

/*==============================================================*/
/* Table: software_have                                         */
/*==============================================================*/
create table software_have
(
   software_id          int not null,
   lab_id               int not null,
   primary key (software_id, lab_id)
);

/*==============================================================*/
/* Table: software_need                                         */
/*==============================================================*/
create table software_need
(
   software_id          int not null,
   course_id            int not null,
   primary key (software_id, course_id)
);

/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
create table student
(
   student_id           int not null,
   student_name         char(20) not null,
   student_sex          char(10) not null,
   primary key (student_id)
);

/*==============================================================*/
/* Table: student_course                                        */
/*==============================================================*/
create table student_course
(
   course_id            int not null,
   student_id           int not null,
   primary key (course_id, student_id)
);

/*==============================================================*/
/* Table: teach_course                                          */
/*==============================================================*/
create table teach_course
(
   course_id            int not null,
   teacher_id           int not null,
   primary key (course_id, teacher_id)
);

/*==============================================================*/
/* Table: teacher                                               */
/*==============================================================*/
create table teacher
(
   teacher_id           int not null,
   user_id              int,
   teacher_name         char(20) not null,
   teacher_sex          char(10),
   teacher_connect      char(20),
   primary key (teacher_id)
);

/*==============================================================*/
/* Table: users                                                 */
/*==============================================================*/
create table users
(
   user_id              int not null,
   -- user_name            char(20),
   user_type            char(20) not null,
   user_account         char(10) not null,
   user_password        varchar(20) not null,
   user_state           numeric(1,0) not null,
   -- user_connect         char(20),
   primary key (user_id)
);

alter table administrator add constraint FK_subordinate_1 foreign key (user_id)
      references users (user_id) on delete restrict on update restrict;

alter table lab add constraint FK_manage foreign key (admin_id)
      references administrator (admin_id) on delete restrict on update restrict;

alter table lab add constraint FK_subordinate_3 foreign key (equipment_id)
      references equipment (equipment_id) on delete restrict on update restrict;

alter table lab_course add constraint FK_lab_course foreign key (course_id)
      references course (course_id) on delete restrict on update restrict;

alter table lab_course add constraint FK_lab_course2 foreign key (lab_id)
      references lab (lab_id) on delete restrict on update restrict;

alter table software_have add constraint FK_software_have foreign key (software_id)
      references software (software_id) on delete restrict on update restrict;

alter table software_have add constraint FK_software_have2 foreign key (lab_id)
      references lab (lab_id) on delete restrict on update restrict;

alter table software_need add constraint FK_software_need foreign key (software_id)
      references software (software_id) on delete restrict on update restrict;

alter table software_need add constraint FK_software_need2 foreign key (course_id)
      references course (course_id) on delete restrict on update restrict;

alter table student_course add constraint FK_student_course foreign key (course_id)
      references course (course_id) on delete restrict on update restrict;

alter table student_course add constraint FK_student_course2 foreign key (student_id)
      references student (student_id) on delete restrict on update restrict;

alter table teach_course add constraint FK_teach_course foreign key (course_id)
      references course (course_id) on delete restrict on update restrict;

alter table teach_course add constraint FK_teach_course2 foreign key (teacher_id)
      references teacher (teacher_id) on delete restrict on update restrict;

alter table teacher add constraint FK_subordinate_2 foreign key (user_id)
      references users (user_id) on delete restrict on update restrict;
      
      
-- alter table course add constraint fk_course_lab foreign key (course_id)
-- 	  references lab_course (course_id) on delete cascade;
--       
-- alter table course add constraint fk_course_software foreign key (course_id)
-- 	  references software_need (course_id) on delete cascade;



CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `labsoftware`.`course_software` AS
    SELECT 
        `t`.`course_id` AS `course_id`,
        `t`.`course_name` AS `course_name`,
        GROUP_CONCAT(DISTINCT `t`.`teacher_name`
            SEPARATOR '、') AS teacher,
        `t`.course_period AS course_period,
        `t`.course_amount AS course_amount,
        GROUP_CONCAT(DISTINCT `t`.lab_address
            SEPARATOR '/') AS address,
        GROUP_CONCAT(DISTINCT `t`.software_name
            SEPARATOR ',') AS software
    FROM
        (SELECT 
            labsoftware.course.course_id AS course_id,
                labsoftware.course.course_name AS course_name,
                labsoftware.teacher.teacher_name AS teacher_name,
                labsoftware.course.course_period AS course_period,
                labsoftware.course.course_amount AS course_amount,
                labsoftware.lab.lab_address AS lab_address,
                labsoftware.software.software_name AS software_name
        FROM
            ((((((labsoftware.course
        JOIN labsoftware.teacher)
        JOIN labsoftware.teach_course)
        JOIN labsoftware.lab)
        JOIN labsoftware.software_need)
        JOIN labsoftware.lab_course)
        JOIN labsoftware.software)
        WHERE
            ((labsoftware.course.course_id = labsoftware.teach_course.course_id)
                AND (labsoftware.teacher.teacher_id = labsoftware.teach_course.teacher_id)
                AND (labsoftware.lab_course.lab_id = labsoftware.lab.lab_id)
                AND (labsoftware.lab_course.course_id = labsoftware.course.course_id)
                AND (labsoftware.software_need.software_id = labsoftware.software.software_id)
                AND (labsoftware.software_need.course_id = labsoftware.course.course_id))) t
    GROUP BY `t`.course_id;
    
    CREATE VIEW `lab_software` AS
    SELECT 
        t.lab_id,
        lab_address,
        equipment_config,
        GROUP_CONCAT(software_name
            ORDER BY software_name ASC
            SEPARATOR ',') AS software
    FROM
        (SELECT 
            lab.lab_id, lab_address, equipment_config, software_name
        FROM
            software, software_have, lab, equipment
        WHERE
            lab.lab_id = software_have.lab_id
                AND software.software_id = software_have.software_id
                AND lab.equipment_id = equipment.equipment_id) AS t
    GROUP BY lab_address;
    
CREATE
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `labsoftware`.`teacher_course` AS
    SELECT 
        `t`.`teacher_id` AS `teacher_id`,
        `t`.`teacher_name` AS `teacher_name`,
        GROUP_CONCAT(DISTINCT `t`.`course_name`
            SEPARATOR ',') AS `course_name`,
        GROUP_CONCAT(DISTINCT `t`.`lab_address`
            SEPARATOR '/') AS `lab_address`
    FROM
        (SELECT 
            `t`.`teacher_id` AS `teacher_id`,
                `t`.`teacher_name` AS `teacher_name`,
                `c`.`course_name` AS `course_name`,
                `l`.`lab_address` AS `lab_address`
        FROM
            ((((`labsoftware`.`teacher` `t`
        JOIN `labsoftware`.`course` `c`)
        JOIN `labsoftware`.`lab` `l`)
        JOIN `labsoftware`.`teach_course` `tc`)
        JOIN `labsoftware`.`lab_course` `lc`)
        WHERE
            ((`t`.`teacher_id` = `tc`.`teacher_id`)
                AND (`tc`.`course_id` = `c`.`course_id`)
                AND (`l`.`lab_id` = `lc`.`lab_id`)
                AND (`lc`.`course_id` = `c`.`course_id`))) `t`
    GROUP BY `t`.`teacher_id`;
    
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `course_student` AS
    SELECT 
        `t`.`course_id` AS `course_id`,
        GROUP_CONCAT(`t`.`student_name`
            SEPARATOR ',') AS `student_name`
    FROM
        (SELECT 
            `c`.`course_id` AS `course_id`,
                `s`.`student_name` AS `student_name`
        FROM
            ((`course` `c`
        LEFT JOIN `student_course` `sc` ON ((`c`.`course_id` = `sc`.`course_id`)))
        LEFT JOIN `student` `s` ON ((`sc`.`student_id` = `s`.`student_id`)))) `t`
    GROUP BY `t`.`course_id`;
    
    
DELIMITER ;;
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
END;;
DELIMITER ;

DELIMITER ;;
CREATE DEFINER=`root`@`localhost` TRIGGER `course_BEFORE_DELETE` BEFORE DELETE ON `course` FOR EACH ROW BEGIN
	delete from lab_course where course_id = old.course_id;
    delete from software_need where course_id = old.course_id;
    delete from teach_course where course_id = old.course_id;
    delete from student_course where course_id = old.course_id;
END;;
DELIMITER ;

DELIMITER ;;
CREATE DEFINER=`root`@`localhost` TRIGGER `lab_BEFORE_DELETE` BEFORE DELETE ON `lab` FOR EACH ROW BEGIN
	delete from lab_course where lab_id = old.lab_id;
    delete from software_have where lab_id = old.lab_id;
END;;
DELIMITER ;

create index index_software_name on software
(
   software_name
);

create index index_lab_address on lab
(
	lab_address
);

create index index_student_name on student
(
	student_name
);