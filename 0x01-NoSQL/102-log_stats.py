#!/usr/bin/env python3
"""
Top Students
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    pipeline = [
        {"$unwind": "$scores"},
        {"$group": {
            "_id": "$_id",
            "averageScore": {"$avg": "$scores.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    result = mongo_collection.aggregate(pipeline)
    return list(result)


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.db.students

    top_students_list = top_students(students_collection)
    for student in top_students_list:
        print(student)
