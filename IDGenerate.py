Car_ID = []
def idGenerate(data, color, ID):
    Car_ID = []
    Car_ID.append(ID)
    Car_ID.append(data[:2])
    Car_ID.append(color)
    Car_ID.append(data[-4:])
    return Car_ID
