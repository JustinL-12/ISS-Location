import urllib.request, json, turtle, time

#Load current ISS position from web service
url = 'http://api.open-notify.org/iss-now.json'


def getTimeUntil(x, y):
    # Load time until info from web service
    passUrl = 'http://api.open-notify.org/iss-pass.json'
    passUrl = passUrl + '?lat=' + str(y) + '&lon=' + str(x)
    passResponse = urllib.request.urlopen(passUrl)
    passResult = json.loads(passResponse.read())

    # Get shortest amount of time for pass over
    lowest = passResult['response'][1]['duration']
    passTime = 0
    for i in range(2, len(passResult['response'])):
        if passResult['response'][i]['duration'] < lowest:
            lowest = passResult['response'][i]['duration']
            passTime = passResult['response'][i]['risetime']
    
    # Write time until pass over to screen
    style = ('Arial', 10, 'bold')
    iss.goto(x, y)
    iss.write(time.ctime(passTime), style)



#Render Earth map
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')
screen.onscreenclick(getTimeUntil)

#Create turtle to represent ISS
screen.register_shape('ISS.gif')
iss = turtle.Turtle()
iss.shape('ISS.gif')
iss.setheading(90)

iss.penup()
while True:

    #Get ISS coordinates from website and format as python directory
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    lat = result['iss_position']['latitude']
    lon = result['iss_position']['longitude']

    iss.goto(float(lon), float(lat))
    
