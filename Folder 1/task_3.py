"""Рассчитывает требуемую скорость для
преодоления расстояния за отведенное время"""
try:
    route_length = int(input("Please enter length of the road you need to trevel: "))
    route_time = int(input("Please enter time required to reach point of destination: "))
    route_speed = route_length / route_time
    print(f"You must move not slower than {int(route_speed)}!")
except ValueError:
    print("Operate numbers only!")