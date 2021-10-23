DELIMITER ;;
CREATE DEFINER=`root`@`localhost` TRIGGER `course_BEFORE_DELETE` BEFORE DELETE ON `course` FOR EACH ROW BEGIN
	delete from lab_course where lab_course.course_id = old.course_id;
    delete from software_need where software_need.course_id = old.course_id;
    delete from teach_course where teacher_course.course_id = old.course_id;
END;;
DELIMITER ;