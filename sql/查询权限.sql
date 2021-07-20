select s.employe_no,s.name,s.DEPT_CODE,
       d.dept_name,
       s.ANTIBACTERIAL_LIMIT from staff_dict s left join department_dict d on d.dept_code = s.dept_code
where name = '{name}'
      and d.dept_name = '{keshi}'