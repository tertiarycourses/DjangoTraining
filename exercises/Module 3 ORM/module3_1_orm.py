python manage.py shell

from blog.models import Post

posts = Post.objects.all()

posts[0].title
posts[0].date
posts[0].body

item = Post.objects.get(id=1)
item = Post.objects.filter(id=1)
item = Post.objects.exclude(id=1)


item.title

from adoptions.models import Pet

pets = Pet.objects.all()

pets[0].name
pets[0].description

pet = Pet.objects.get(id=1)

pet.name
