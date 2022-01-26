from django.db import models
from django.urls import reverse

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})


MEALS = (
	('B', 'Breakfast'),
	('L', 'Lunch'),
	('D', 'Dinner'),
)


class Feeding(models.Model):
	date = models.DateField()
	meal = models.CharField(
		max_length = 1,
		choices=MEALS, # this will create a select menu, the values of the select item will be the first letter, and what's between the tags (aka, what the user sees) will be the second item (e.g. breakfast)
		default=MEALS[0][0]
	)
	# create a cat_id FK lowercase singular of your related model
	# inside postgres the column will have _id attached so cat_id
	dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-date', '-meal']
	
	def __str__(self):
		return f"{self.get_meal_display()} on {self.date}"