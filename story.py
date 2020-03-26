class Post:
    def __init__(self, id, photo_url, name, body):
        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.body = body

class PostStore:
    def __init__(self):
        self.posts=[]
        
    def get_all(self):
        # get all posts - الحصول على كل المنشورات
       return self.posts
            
    def add(self, post):
        
        # append post - إضافة منشور
        (self.posts).append(post)
    def get_by_id(self, id):
        # search for post by id - id البحث عن منشور بالمعرف
        result=None
        for post in self.posts:
            if id==post.id:
                result=post
                break
       # print( result)
        return result
    
    def update(self, id, fields):
       # update post data - id تعديل منشور بالمعرف
       for post in self.posts:
            if id==post.id:
                post.name=fields['name']
                post.photo_url=fields['photo_url']
                post.body=fields['body']

    def delete(self, id):
        # delete post by id - id حذف منشور بالمعرف
        for post in self.posts:
            if id==post.id:
                (self.posts).remove(post)