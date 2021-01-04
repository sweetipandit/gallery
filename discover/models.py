from django.db import models

# Create your models here.



class RegistrationModel(models.Model):
	userName=models.CharField(max_length=50)
	userContact=models.IntegerField()
	userEmailId=models.CharField(max_length=100)
	userPassword=models.CharField(max_length=30)

	def __str__(self):
		return f'{self.userName}--{self.userContact}--{self.userEmailId}--{self.userPassword}'





class ImageModel(models.Model):

	userImage = models.ImageField(upload_to = 'profile/')
	titele =models.CharField(max_length=50)
	user=models.ForeignKey(RegistrationModel,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.userImage}--{self.titele}--{self.user}'
 


 	
 	
 	
 	
    
