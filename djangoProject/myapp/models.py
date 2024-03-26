from django.db import models


# Create your models here.

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    field4 = models.CharField(max_length=100)
    field5 = models.CharField(max_length=100)

    # 这个方法定义了一个模型实例转换为字符串时的格式。这里使用了Python3.6
    # 及以上版本引入的f - string（格式化字符串字面量）来拼接field1和field2两个字段的值，中间用一个空格隔开。
    def __str__(self):
        return f"{self.field1} {self.field2} {self.field3} {self.field4} {self.field5}"

    class Meta:
        # 指定数据库中的集合名称
        db_table = 'customers'  # 替换为你的集合名称
        # 告诉 Django 不要管理这个集合的数据库表结构
        managed = False

        # abstract = True
        # 当一个模型被标记为抽象基类时，它不会被转换为具体的数据库表。相反，这个抽象基类可以被用作其他模型的基类，来提供通用的字段、方法或其他属性。
        # 这在Django模型设计中是非常有用的，因为它允许你定义一些共享的字段和方法，并在多个具体的模型中使用它们，而不必在每个具体的模型中都重复这些定义。

class MyModel2(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    field4 = models.CharField(max_length=100)
    field5 = models.CharField(max_length=100)

    # 这个方法定义了一个模型实例转换为字符串时的格式。这里使用了Python3.6
    # 及以上版本引入的f - string（格式化字符串字面量）来拼接field1和field2两个字段的值，中间用一个空格隔开。
    def __str__(self):
        return f"{self.field1} {self.field2} {self.field3} {self.field4} {self.field5}"

    class Meta:
        # 指定数据库中的集合名称
        db_table = 'customers'  # 替换为你的集合名称
        # 告诉 Django 不要管理这个集合的数据库表结构
        managed = False

        # abstract = True
        # 当一个模型被标记为抽象基类时，它不会被转换为具体的数据库表。相反，这个抽象基类可以被用作其他模型的基类，来提供通用的字段、方法或其他属性。
        # 这在Django模型设计中是非常有用的，因为它允许你定义一些共享的字段和方法，并在多个具体的模型中使用它们，而不必在每个具体的模型中都重复这些定义。

class MyModel3(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    field3 = models.CharField(max_length=100)
    field4 = models.CharField(max_length=100)
    field5 = models.CharField(max_length=100)

    # 这个方法定义了一个模型实例转换为字符串时的格式。这里使用了Python3.6
    # 及以上版本引入的f - string（格式化字符串字面量）来拼接field1和field2两个字段的值，中间用一个空格隔开。
    def __str__(self):
        return f"{self.field1} {self.field2} {self.field3} {self.field4} {self.field5}"

    class Meta:
        # 指定数据库中的集合名称
        db_table = 'customers'  # 替换为你的集合名称
        # 告诉 Django 不要管理这个集合的数据库表结构
        managed = False

        # abstract = True
        # 当一个模型被标记为抽象基类时，它不会被转换为具体的数据库表。相反，这个抽象基类可以被用作其他模型的基类，来提供通用的字段、方法或其他属性。
        # 这在Django模型设计中是非常有用的，因为它允许你定义一些共享的字段和方法，并在多个具体的模型中使用它们，而不必在每个具体的模型中都重复这些定义。
