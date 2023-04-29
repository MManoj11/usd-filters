from django import template

register=template.Library()


def swap(value):
    return value.swapcase()

def remove(value,arg):
    return value.replace(arg,'')

def count(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg):]==arg:
            c+=1
    return c


register.filter('swap',swap)
register.filter('remove',remove)
register.filter('count',count)