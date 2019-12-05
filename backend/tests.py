from django.test import TestCase
from backend.models import UserGen
# Create your tests here.
def getValues():
    result_set = UserGen.objects.all()\
        .values_list().filter(username="刘正")

    complete_poen = []
    id_list = []
    for poem in result_set:
        id,_,content,title = poem
        print(poem)
        print(id,content,title)
if __name__ == '__main__':
    getValues()