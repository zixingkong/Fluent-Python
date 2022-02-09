# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_2.7
   Description :
   date：          2022/2/9
-------------------------------------------------
"""
"""
元祖除了用作不可变的列表，还可以用于没有字段名的记录
"""

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205865')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # ➊
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # ➋
    if longitude <= 0:  # ➌
        print(fmt.format(name, latitude, longitude))
