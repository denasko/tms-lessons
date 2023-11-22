"""SELECT country,COUNT(*) FROM user GROUP BY(country)"""

"""SELECT first_name,COUNT(*) FROM user GROUP BY(first_name)"""

"""SELECT country,SUM(age) FROM user GROUP BY(country)"""

"""SELECT country,AVG(age) FROM user GROUP BY(country)"""

"""SELECT country,max(age) FROM user GROUP BY(age)"""

"""SELECT country,count(*) FROM user GROUP BY(country) HAVING count(*)>5"""

"""SELECT last_name,count(*) FROM user GROUP BY(last_name) HAVING count(1)>1"""
