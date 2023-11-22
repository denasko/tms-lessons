"""SELECT * FROM user ORDER BY age DESC"""

"""SELECT * FROM user ORDER BY last_name,first_name"""

"""SELECT * FROM user ORDER BY country,age DESC"""

"""SELECT * FROM user ORDER BY length(first_name || ' ' ||last_name)"""

"""SELECT * FROM user ORDER BY SUBSTR(first_name,1,1)||'.'||SUBSTR(last_name,1,1)||'.' """