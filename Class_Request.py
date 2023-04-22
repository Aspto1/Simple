import requests as R
'''
Making a Class to read URL and get User Id
'''
class Url:
    def __init__(self,url):
        self.url = url

    def url_reader(self):
        response = R.get(self.url)
        get_tasks = response.json()
        return get_tasks
    

    def get_task(self,userid):
        tasks = self.url_reader()
        for task in tasks:
            if task['id'] == userid:
                print(task)

url = 'http://jsonplaceholder.typicode.com/todos/'
userid = 7

reader = Url(url)
reader.get_task(userid)