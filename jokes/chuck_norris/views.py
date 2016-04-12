from django.shortcuts import render
import urllib, json
import redis
# Create your views here.
r = redis.StrictRedis(host='localhost', port=6379, db=0)
def index(request):
    #url = "http://api.icndb.com/jokes/random?firstName=John&lastName=Doe"
    #response = urllib.request.urlopen(url)
    #resp = response.read().decode('utf-8')
    #print (resp)

    #data = json.loads(resp)
    #print (data['value']['id'])

    return render(request, 'chuck_norris/index.html')
def add(request):

    voornaam = request.POST['voornaam']
    achternaam = request.POST['achternaam']
    url = "http://api.icndb.com/jokes/random?firstName="+ voornaam +"&lastName=" + achternaam
    response = urllib.request.urlopen(url)
    resp = response.read().decode('utf-8')
    print (resp)

    data = json.loads(resp)
    print (data['value']['id'])
    jokeId = data['value']['id']
    joke = data['value']['joke']
    r.sadd(jokeId, joke )


    return render(request, 'chuck_norris/add.html' ,{'joke': joke})
