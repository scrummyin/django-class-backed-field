# django-classbacked-field

This field will allow you to store a string in the database and passes it as the first and only arg to a constructor.  The best use I've found for this so far is the abbility to store the id of an object in the database, and then make a rest call using that id.  


This is an example of a models.py you could create in your application.


```python
class OverSimplfiedGistPost(object):
    def __init__(self, gist_id):
        json_of_gist = requests.get("https://api.github.com/gists/%s" % gist_id).json()
        self.id = json_of_gist['id']
        self.text = [file_data['content'] for filename, file_data in json_of_gist['files'].items()]
        self.browser_url = json_of_gist['html_url']


id_retriving_lambda = lambda x: str(x.id)


class RemoteGist(models.Model):
    user = fields.ForgeinKey(User)
    gist = fields.ClassBackedField(represents=OverSimplfiedGistPost, db_value_generator=id_retriving_lambda, max_length=255)
```
I could then search this model using the id of the gist.  Also when it will get the latest inforation form github everytime I use the object.  

