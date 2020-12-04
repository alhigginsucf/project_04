from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker

class Position (models.Model):
        stock_name = models.CharField (max_length=10)
        quantity = models.IntegerField()
        average = models.FloatField()

class Trade (models.Model):
        stock_name = models.CharField (max_length=10)
        quantity = models.IntegerField()
        price = models.FloatField()

        trade_type = models.IntegerField()

        @property
        def direction(self):
            return "Buy" if self.trade_type == 0 else "Sell" 
        
        @property
        def total(self):
            return self.quantity*self.price

class User (models.Model):
        balance = models.FloatField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
