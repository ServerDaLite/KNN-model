from math import sqrt
import numpy as np

class KNN:
    
    def __init__(self, K=3):
        self.k = K
        self.memory = list()
    
    def equation(self, ID, points, point):
        # Coordinates List
        positions = list()
        
        # Seperating the groups into manage coords
        for dim in range(len(points[0])):
            coords = list()
            for axis in range(len(points)):
                coords.append(points[axis][dim])
            positions.append({ID:coords})
        
        # List of total distances
        distances = list()
        
        # calculate distances
        for index in positions:
            current_id = list(index.keys())[0]
            current_coordinates = index[current_id]
            
            result = sqrt( ((current_coordinates[0] - point[0]) ** 2) + ( (current_coordinates[1]- point[1]) ** 2))
            
            distances.append({current_id:result})
            
        return distances
        
            
            
        
    def fit(self, *points):
        for groups in points:
            self.memory.append(groups)
        
    def predict(self, point):
        distances = []
        
        for group in self.memory:
            ID = list(group.keys())[0]
            COORDS = group[ID]
            
            result = self.equation(ID, COORDS, point)
            
            print(result)

if __name__ == "__main__":
    dataX = np.random.randint(1, 100, 6)
    dataY = np.random.randint(1, 100, 6)
    
    dataX_2 = np.random.randint(1, 100, 6)
    dataY_2 = np.random.randint(1, 100, 6)
    
    knn = KNN()
    knn.fit({"A": [dataX, dataY]}, {"B": [dataX_2, dataY_2]})
    knn.predict((2, 3))
