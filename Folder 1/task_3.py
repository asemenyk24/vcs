"""Рассчитывает требуемую скорость для
преодоления расстояния за отведенное время"""
route_length = input("Please enter length of the road you need to trevel: ")
route_time = input("Please enter time required to reach point of destination: ")
route_speed = int(route_length) / int(route_time)
print(f"You must move not slower than {int(route_speed)}!")