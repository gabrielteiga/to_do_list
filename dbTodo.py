def insert_data_tbTodo(task_creation_date, description, endline):
    data_query = """INSERT INTO tbTodo(
        task_creation_date, task, endline)VALUES(
            '{}','{}','{}'
        );""".format(task_creation_date, description, endline)
    return data_query

def update_data_tbTodo():
    data_query = """UPDATE tbTodo SET endline = %s WHERE id_task = %s;"""
    return data_query

def select_data_tbTodo():
    data_query = """SELECT id_task, task, endline FROM tbTodo;"""
    return data_query

def delete_task_tbTodo():
    data_query = """DELETE FROM tbTodo WHERE id_task = %s"""
    return data_query
