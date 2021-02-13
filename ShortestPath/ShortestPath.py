from queue import Queue
import time

class City:
  def __init__(self, name):
    self.name = name
    self.neighbors = []
    self.sldToValladolid = [] # straight line distance (sld) a Neighbor object 

class Neighbor:
  def __init__(self, city, distance):
    self.city = city
    self.distance = distance


class Graph:
    def __init__(self, cities):
      self.graph = cities
      self.pathCost = 0
      self.path = []

    def greedyFirstSearch(self):
        queue = Queue(0)       
        startCity = self.findCity('Malaga')
        goalCity = self.findCity('Valladolid')
        
        if len(self.path) == 0:           
            nextCity = Neighbor(startCity, 0)
            self.path.append(nextCity)

        while nextCity.city is not goalCity:
            #print('....', nextCity.city.name, '....')
            sortedCities = sorted(nextCity.city.neighbors, key = lambda x: x.city.sldToValladolid[0].distance, reverse = False )
            for c in sortedCities:
                if c.city is goalCity:
                    queue.queue.clear()
                    queue.put(c)
                    break
                if c not in self.path: #avoid loops
                    if len(c.city.neighbors) is not 0: #dead end
                       queue.put(c) # if the queue does not have nodes, return to the last node in the path and select another node
            nextCity = queue.get()
            self.path.append(nextCity)
            queue.queue.clear()
        for c in self.path:
            self.pathCost = self.pathCost + c.distance
            #print(c.city.name, c.distance)
        #print(self.pathCost)
        #for x in list(queue.queue):
            #print(x.city.name)

    def findCity(self, cityName):
         for c in self.graph:
            if cityName == c.name:
                return c      
         return False


def main():
    cities = []

    def findCity(cityName):
         for c in cities:
            if cityName == c.name:
                return c      
         return False

    def createNeighbor(city, neighbor, distance):
        city.neighbors.append(Neighbor(neighbor, distance))
        neighbor.neighbors.append(Neighbor(city, distance))

    def retrieveCitiesFromFile():
        with open("SpainMap.txt", "r") as map:
            content = map.read().splitlines()
            i = content.index('A B Distance') + 1
            z = content.index('SLD ') + 1         
                     
            for x in range(i, z - 2):
                distances = content[x].split() 
                if len(cities) == 0:
                    city = City(distances[0])
                    neighbor = City(distances[1])
                    cities.append(city)
                    cities.append(neighbor)
                    city.neighbors.append(Neighbor(neighbor, int(distances[2])))
                else:
                      if findCity(distances[0]) == False:
                           cities.append(City(distances[0]))
                      if findCity(distances[1]) == False:
                          cities.append(City(distances[1]))
                      createNeighbor(findCity(distances[0]), findCity(distances[1]), int(distances[2]))             

            for sl in range(z, len(content)):
                sld = content[sl].split()
                valladolid = findCity('Valladolid')
                if valladolid != False:
                    addSLD(valladolid, findCity(sld[0]), int(sld[1]))                   

    def addSLD(valladolid, city, distance):
        valladolid.sldToValladolid.append(Neighbor(city, distance))
        if city.name != valladolid.name:
           city.sldToValladolid.append(Neighbor(valladolid, distance))

 
        
    retrieveCitiesFromFile()
    g = Graph(cities)
    start = time.process_time()
    g.greedyFirstSearch()
    end = time.process_time() - start
    print('......Distances......')
    for c in range(0, len(g.path) - 1):
       print(g.path[c].city.name,'',g.path[c + 1].city.name, '=',  g.path[c + 1].distance )
    print('*Pathcost =', g.pathCost)
    print('*Time elapsed =', end)

    
if __name__=="__main__": 
    main() 
