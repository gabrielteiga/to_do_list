def show_databases():
    data_query = """SHOW DATABASES;"""
    return data_query


def use_todo():
    data_query = """USE todo;"""
    return data_query


def create_todo():
    data_query = """CREATE DATABASE todo;"""
    return data_query


def create_tbtodo():
    data_query = """CREATE TABLE tbtodo(
    id_task INT PRIMARY KEY AUTO_INCREMENT,
    task_creation_date DATE NULL,
    task VARCHAR(255) NOT NULL,
    deadline DATE NULL);"""
    return data_query


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
    data_query = """SELECT * FROM tbTodo;"""
    return data_query


def select_task_tbTodo():
    data_query = """SELECT * FROM tbTodo WHERE id_task = %s"""
    return data_query


def delete_task_tbTodo():
    data_query = """DELETE FROM tbTodo WHERE id_task = %s;"""
    return data_query
