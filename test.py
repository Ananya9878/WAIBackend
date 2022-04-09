import requests
import json

def test_create_task():
    r = requests.post('http://localhost:5000/v1/tasks/', json={"title": "My First Task"})
    assert isinstance(r.json()["id"], int)
    assert len(r.json()) == 1

def test_list_all_tasks():
    r = requests.get('http://localhost:5000/v1/tasks/')
    assert isinstance(r.json()["tasks"], list)
    assert len(r.json()) == 1
    assert isinstance(r.json()["tasks"][0]["id"], int)
    assert isinstance(r.json()["tasks"][0]["title"], str)
    assert isinstance(r.json()["tasks"][0]["is_completed"], bool)
    assert len(r.json()["tasks"][0]) == 3

def test_get_task():
    r = requests.get('http://localhost:5000/v1/tasks/1/')
    assert isinstance(r.json(),dict)
    assert isinstance(r.json()["id"], int)
    assert isinstance(r.json()["title"], str)
    assert isinstance(r.json()["is_completed"], bool)
    assert len(r.json()) == 3

def test_update_task():
    r = requests.put('http://localhost:5000/v1/tasks/1/', json={"title": "My 1st Task", "is_completed": True})
    assert not r.content

def test_delete_task():
    r = requests.delete('http://localhost:5000/v1/tasks/1/')
    assert not r.content


def main():
    test_create_task()
    print("Create task test completed.")

    test_list_all_tasks()
    print("Get all tasks test completed.")

    test_get_task()
    print("Get task test completed.")

    test_update_task()
    print("Update task test completed.")

    test_delete_task()
    print("Delete task test completed.")


if __name__ == '__main__':
    main()