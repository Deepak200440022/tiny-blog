from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    """
    Model representing a blog post.

    Fields:
        author (ForeignKey): Reference to the user who created the post.
        title (CharField): Title of the post (max length 200).
        text (TextField): Main content of the post.
        created_date (DateTimeField): Timestamp when the post was created.
        published_date (DateTimeField): Timestamp when the post was published (can be null/blank).

    Methods:
        publish(): Sets the published_date to the current time and saves the model.
        __str__(): Returns the title of the post as its string representation.
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """
        Publish the post by setting the published_date to the current time.
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return the string representation of the post, which is its title.
        """
        return self.title
