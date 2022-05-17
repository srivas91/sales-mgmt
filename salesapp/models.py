from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=40)
    default_price = models.DecimalField(max_digits=6, decimal_places=2, default=50)



    def __str__(self):
        return self.name


class SaleDetail(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    # deposit = models.ForeignKey(Deposit)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    # sale = models.ForeignKey(Sale)

    def save(self, *args, **kwargs):
        # Make sure this is the first save (pk should be None) and there is no unit_price set
        if self.pk is None and not self.unit_price:
            self.unit_price = self.item.default_price
        elif not self.unit_price:
            self.unit_price = self.item.default_price

        # Call the original save method
        super(SaleDetail, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.item}-{self.quantity}-{self.unit_price}'