# Generated by Django 4.1.5 on 2023-01-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='data:image/jpeg;base64,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Sl45WESR3+bfcN+jZfL9GV7d01NJ/FHLEfsLgp5biMXjRwVTebHOppPSx2ZpPmcF4/TLx49DWt80UUw9cbyghjD692+SlZ1Amk+zur2zs1n981Es44sbamYfOGd4joXKScbJ8WirnH/t2x/a94C7t6+X9XTRwA/Cnlzkf+OK9/rBBPggjgjDWNZFGwbgAxrR+CqzXS1hLKQlkW59UW6dRAD+sd8rxR13KVF2b2pDquV1Sd+QgRwtPSIeN9MuWhhpw0bt32IImD4XHTxtjjblaLnUlxc46uc4nVzidSSrJEQFlqM3rMR6PhHo2DT+K1Kz2LUM8VQamCPbNka1s8Qc1jiWXySRl1mk2JaQSLi2umofCoNq3D+pqB6NkD+C1Cz2EUE8lQKqdmxEbSyCLM17hnsZHyFt23NmgAE2F9ddNCgIotaD3DZxaDd2U20AO8cR0SgaQ06WZfuA5swb8q/VWuWzfaSkRFGhERAREQEREBERAREQEREBERARfKZ1iNbA3ubf7suwOJGuvXn1WI9I21WuW+iIi2jhavJiC9og+exC9CML0iDll1EQVdZixY94bE57YgDK4OAyAi+gO/TVWMbw4Bw1BAI8xUOqwmOVxccwzWDwHFokA3ZhxU5rQBYbgpFumemsa/rqIirmIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIOEXQBdRARU2O4TNUPjcyfZBgeLZXEhzmPbmBDhqMw3jgeagT9nJnhnuzWMbtfcm7SzBIx7bMffm5puW6WNrINQipajCJDLNMySz5CzKLhnuYawObnDS5ty07tNdy+M+F1jmuaakHMLHV0ee7XC+g9zsS02F82XW10GgRVVZQzuN45sos0ZbuAIAOYbtCdBm3hfBmDylj2ySlxdJFJfPIQAwR3bbl3PMb6hBeIqH9H1uQtFQ0E31zOJZ3QBY5e9d1zra17C9l7jw2oE0bzLnZGXEAveNDtQARbvGz2anXudboLtERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQf/9k=', max_length=800),
        ),
    ]
