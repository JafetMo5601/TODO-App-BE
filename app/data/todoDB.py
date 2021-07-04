from app import mysql
import json


class Requests:
    def __init__(self):
        self.mysql = mysql
        self.conn = self.mysql.connection
        self.cur = self.conn.cursor()
    
    def dataProcessing(self, rv):
        if rv != ():
            data, row_headers = [], [x[0] for x in self.cur.description]
            for result in rv:
                data.append(dict(zip(row_headers, result)))
        else:
            data = 'Executed correctly!'
        return data

    def query(self, sp):
        self.cur.execute("CALL " + sp + ";")
        json_data = self.dataProcessing(self.cur.fetchall())
        self.cur.close()
        self.conn.commit()
        return json_data


def changeTaskPriority(taskId, priorityId):
    requests = Requests()
    request = requests.query(
        "spChangeTaskPriority(" + str(taskId) + "," + str(priorityId) + ")"
    )
    return request


def changeTaskStatus(taskId, statusId):
    requests = Requests()
    request = requests.query(
        "spChangeTaskStatus(" + str(taskId) + "," + str(statusId) + ")"
    )
    return request


def changeTaskTag(taskId, tagId):
    requests = Requests()
    request = requests.query("spChangeTaskTag(" + str(taskId) + "," + str(tagId) + ")")
    return request


def entireTasksRetrieve():
    requests = Requests()
    request = requests.query("spEntireTasksRetrieve()")
    return request


def priorityAdd(priorityName):
    requests = Requests()
    request = requests.query("spPriorityAdd('" + str(priorityName) + "')")
    return request


def priorityRetrieve(priorityId):
    requests = Requests()
    request = requests.query("spPriorityTypesRetrieve(" + str(priorityId) + ")")
    return request


def statusAdd(statusName):
    requests = Requests()
    request = requests.query("spStatusTypeAdd('" + str(statusName) + "')")
    return request


def statusRetrieve(statusId):
    requests = Requests()
    request = requests.query("spStatusRetrieve(" + str(statusId) + ")")
    return request


def tagAdd(tagName):
    requests = Requests()
    request = requests.query("spTagsAdd('" + str(tagName) + "')")
    return request


def tagRetrieve(tagId):
    requests = Requests()
    request = requests.query("spTagsRetrieve(" + str(tagId) + ")")
    return request


def taskAdd(taskDescription, taskTypeId, statusId, priorityId, tagId):
    requests = Requests()
    request = requests.query(
        "spTaskAdd('"
        + str(taskDescription)
        + "' ,"
        + str(taskTypeId)
        + " ,"
        + str(statusId)
        + " ,"
        + str(priorityId)
        + " ,"
        + str(tagId)
        + ")"
    )
    return request


def taskEdit(taskId, taskDescription):
    requests = Requests()
    request = requests.query(
        "spTaskEdit(" + str(taskId) + ", '" + str(taskDescription) + "')"
    )
    return request


def taskRetrieve(taskId):
    requests = Requests()
    request = requests.query("spTaskRetrieve(" + str(taskId) + ")")
    return request


def taskTypeAdd(taskTypeName):
    requests = Requests()
    request = requests.query("spTasksTypesAdd('" + str(taskTypeName) + "')")
    return request


def taskTypeRetrieve(taskTypeId):
    requests = Requests()
    request = requests.query("spTasksTypesRetrieve(" + str(taskTypeId) + ")")
    return request
