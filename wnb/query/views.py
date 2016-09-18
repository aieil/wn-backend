from django.shortcuts import render
from django.http import HttpResponse

from subprocess import check_output
import re

xinc = 100.0/1113000
yinc = 100.0/80510

#really unsafe hacky garbage is what this is

def query(q):
    prepstmt = "select * from entries where "
    if 'coords' in q:
        coords = q['coords'].split(',')]
        x = float(coords[0])
        xrng = (x - xinc, x + xinc)
        y = float(coords[0])
        yrng = (y - yrng, y + yrng)
        prepstmt.append("_x > {} and _x < {}".format(xrng[0], xrng[1]))
        prepstmt.append(" and _y > {} and _y < {}".format(yrng[0], yrng[1]))
    else:
        pass #error out

    if 'gender' in q:
        prepstmt.append(' and _gender = {}'.format(q['gender']))

    if 'access' in q:
        prepstmt.append(' and _access = {}'.format(q['access'])

    if 'stall' in q:
        prepstmt.append(' and _stalls = {}'.format(q['stalls'])

    if 'urinal' in q:
        prepstmt.append(' and _urinals = {}'.format(q['urinals'])

    if re.search('[;()\\-]', prepstmt):
        pass #error out

    return re.split('.|\n.|', \ 
        check_output(["cockroach", "sql", "-e", "'" + prepstmt + ";'"]))

def index(request):
    query(request.GET)
    return HttpResponse("Hello, world, this is the backend app")
