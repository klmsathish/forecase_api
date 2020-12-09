from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import CharField, PositiveIntegerRelDbTypeMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Creates and saves a new user
        if not email:
            raise ValueError('Useres must have an email')
        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        # Creates a new superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # Custom User model that supports using email instead of username
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    mobile = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'


class Profile(models.Model):
    profileId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    profilePicture = models.URLField(max_length = 500)
    profileARR = ArrayField(models.URLField(max_length = 500))
    is_private = models.BooleanField(default=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    lastLoggedin = models.DateTimeField()


class Photo(models.Model):
    photoId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    photoURL = ArrayField(models.URLField(max_length = 500))
    photoLatitude = models.FloatField(null=True)
    photoLongitude = models.FloatField(null=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(editable=True,null=True, blank=True)

    def __str__(self):
        return "%s" % (self.photoURL)

class Video(models.Model):
    videoId = models.AutoField(primary_key=True)
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    videoURL = ArrayField(models.URLField())
    videoLatitude = models.FloatField(null=True)
    videoLongitude = models.FloatField(null=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(editable=True)


class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    postCaption = models.TextField()
    postIsVisible = models.BooleanField(default = True)
    postType = models.CharField(max_length = 50,default="photo")
    postImage = models.OneToOneField(Photo,on_delete=models.CASCADE,null=True, blank=True)
    postVideo = models.OneToOneField(Video,on_delete=models.CASCADE,null=True, blank=True)
    postDescription = models.TextField(null=True, blank=True)
    postHashTags = ArrayField(models.CharField(max_length=100))
    postLocation = models.CharField(max_length=255)
    postDate = models.DateTimeField(auto_now=True)
    postTag = ArrayField(models.CharField(max_length = 100))

class like(models.Model):
    likeId = models.AutoField(primary_key=True)
    likeDate = models.DateTimeField(auto_now_add=True)
    userId = models.ManyToManyField(User)
    postId = models.ForeignKey(Post,on_delete=models.CASCADE)

class Follow(models.Model):
    followId = models.AutoField(primary_key=True)
    followers = models.OneToOneField(User,on_delete=models.CASCADE,related_name = 'followers')
    following = models.OneToOneField(User,on_delete=models.CASCADE,related_name = 'following')

class Comment(models.Model):
    commentId = models.AutoField(primary_key=True)
    postID = models.ForeignKey(Post,on_delete=models.CASCADE)
    userId = models.ManyToManyField(User)
    comment = models.CharField(max_length = 150)

class CommentLike(models.Model):
    commentLikeId = models.AutoField(primary_key=True)
    commentId = models.ForeignKey(Comment,on_delete=models.CASCADE)
    userId = models.ManyToManyField(User)

class CommentReply(models.Model):
    commentReplyId = models.AutoField(primary_key=True)
    commentId = models.ForeignKey(Comment,on_delete=models.CASCADE)
    userId = models.ManyToManyField(User)
    commentReply = models.CharField(max_length = 150)

class CommentReplyLike(models.Model):
    commentReplyLikeId = models.AutoField(primary_key=True)
    commentReplyId = models.ForeignKey(CommentReply,on_delete=models.CASCADE)
    userId = models.ManyToManyField(User)

class Story(models.Model):
    storyId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    storyImage = models.OneToOneField(Photo,on_delete=models.CASCADE,default=0,null=True, blank=True)
    storyVideo = models.OneToOneField(Video,on_delete=models.CASCADE,null=True, blank=True)
    storyDate = models.DateTimeField(auto_now=True)

class StoryView(models.Model):
    storyViewId = models.AutoField(primary_key=True)
    storyId = models.ForeignKey(Story,on_delete=models.CASCADE)
    userId = models.ManyToManyField(User)

# class PostColab(models.Model):
#     postId = models.IntegerField(primary_key=True,auto_created=True)
#     postCaption = models.TextField()
#     postImage = ArrayField(models.OneToOneField(Photo))
#     postVideo = ArrayField(models.OneToOneField(Video))
#     postTags = ArrayField(models.CharField(max_length=100))
#     postLocation = models.CharField(max_length=255)
#     postColabPpl = ArrayField


