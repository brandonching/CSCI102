# Brandon Ching
# CSCI102 - Section C
# Python-FunSQLWhatsWrong

table_name_input = input()
student_id_input = input()

"""
A user may enter a table name from a previous year, such as:
`2017_springCSCI101` or `2018_fallCSCI101`
But these databases are under maintenance so
we can only query a semester in 2020.

Therefore, we only need the table name and need to strip out the year.
"""
reformatted_table_name_no_year = table_name_input[4:]

"""
A user tends to enter 001234567800 with an extra `00`
at the beginning and the end of the input.
We only need the middle 8 numbers.
NOTE: list slicing only works with a list or string (aka a list of characters).
It will not work with other types like int or float.
"""
reformatted_student_id = student_id_input[2:10]

headers = ("h1", "h2", "h3", "h4", "h5")


sql_command = (
  f"SELECT {headers[1]}, {headers[4]} "
  f"FROM 2020{reformatted_table_name_no_year} "
  f"WHERE id={reformatted_student_id}"
)

print(sql_command)
# FUTURE TODO: send the sql command
