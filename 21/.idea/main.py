#@param comsumption wattage consumption of a device [W]
#@param cost cost per kilowatt hour
#@param hour time [h]
#
#@return total_cost [kWh]
def CostCulculation(comsumption, cost, hour=1):
    return cost*(comsumption/1000.0*hour)
    
