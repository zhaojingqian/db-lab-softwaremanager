CREATE VIEW `course_software` AS
    SELECT 
        t.course_id,
        t.course_name,
        GROUP_CONCAT(DISTINCT t.teacher_name
            SEPARATOR '、') AS teacher,
        t.course_period,
        t.course_amount,
        GROUP_CONCAT(DISTINCT t.lab_address
            SEPARATOR '/') AS address,
        GROUP_CONCAT(DISTINCT t.software_name) AS software
    FROM
        (SELECT 
            course.course_id,
                course.course_name,
                teacher.teacher_name,
                course.course_period,
                course.course_amount,
                lab.lab_address,
                software.software_name
        FROM
            course, teacher, teach_course, lab, software_need, lab_course, software
        WHERE
            course.course_id = teach_course.course_id
                AND teacher.teacher_id = teach_course.teacher_id
                AND lab_course.lab_id = lab.lab_id
                AND lab_course.course_id = course.course_id
                AND software_need.software_id = software.software_id
                AND software_need.course_id = course.course_id) AS t
    GROUP BY course_id