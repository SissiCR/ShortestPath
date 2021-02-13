class City:
  def __init__(self, name):
    self.name = name
    self.neighbors = []
    self.sldToValladolid = [] # straight line distance (sld)

class Neighbor:
  def __init__(self, city, distance):
    self.city = city
    self.distance = distance


class graph:
    def __init__(self, cities):
      self.graph = cities


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
                      createNeighbor(findCity(distances[0]), findCity(distances[1]), distances[2])             

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

   # root = Tree()

    #t = time.process_time()
    #root.bfSearch(allItems, maxWeight)
    #elapsedTime = time.process_time() - t
    #print('Time for BFS is:', elapsedTime)
    #root.bestBenefit.printInfo()
    #print('....................................................')
    #startTime = time.process_time()
    #root.dfSearch(allItems, maxWeight)
    #totalTime = time.process_time() - startTime
    #print('Time for DFS is:', totalTime)
    #root.bestBenefit.printInfo()

    
if __name__=="__main__": 
    main() 
