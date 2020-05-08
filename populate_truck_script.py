# 添加和读取数据到数据库中
import os
import re

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "truck.settings")
django.setup()
import csv

# Tags.objects.all().delete()

images = os.listdir('media')


def populate_truck_data():
    # Truck.objects.all().delete()
    opener = open('data/trucks.csv', 'r')
    opener.readline()
    reader = csv.reader(opener)
    # res=re.search('\d+(\.\d+)?',title)
    for line in reader:
        id = line[0]
        category = line[1]
        print(category)
        size = re.search('\d+(\.\d+)?', category)[0]
        car_name = category.replace(size, '')
        # print(car_name, size)
        continue
        weight = line[2]
        print('weight ', weight)
        pic = None
        for image_name in images:
            res = re.search('\d+(\.\d+)?', image_name)[0]
            if res == size:
                pic = image_name
                print(pic)
                break
        # truck = Truck.objects.create(id=id, pic=pic, title=car_name, weight=float(weight))  # for tag in tags:
        # tag_obj, created = Tags.objects.get_or_create(name=size + '米长')
        # print('created', created)
        # truck.tags.add(tag_obj.id)


if __name__ == '__main__':
    populate_truck_data()
