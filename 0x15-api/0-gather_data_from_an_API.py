#!/usr/bin/python3
"""Returns TODO list STATUS for an employee."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "employees/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todo", params={"userId": sys.argv[1]}).json()

    done = [t.get("title") for t in todo if t.get("done") is True]
    print("Employee {} is done with tasks({}/{}):".format(employee.get("name"), len(done), len(todo)))
    [print("\t {}".format(done)) for done in done]
