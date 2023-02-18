def insert_data_tbTodo():
    data_query = """INSERT INTO tbTodo(
        task_creation_date, task, deadline)VALUES(
            %s,%s,%s
        );"""
    return data_query


def update_data_tbTodo():
    data_query = """UPDATE tbTodo SET deadline = %s WHERE id_task = %s;"""
    return data_query


def select_data_tbTodo():
    data_query = """SELECT id_task, task, deadline FROM tbTodo;"""
    return data_query


def select_task_tbTodo():
    data_query = """SELECT * FROM tbTodo WHERE id_task = %s"""
    return data_query


def delete_task_tbTodo():
    data_query = """DELETE FROM tbTodo WHERE id_task = %s;"""
    return data_query
