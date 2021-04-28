import array

A = array.array('i', [100, 200, 300, 400, 500])
"""A
array('i', [100, 200, 300, 400, 500])"""

A[1] = -700     # mengubah elemen kedua
A[4] = 800      # mengubah elemen kelima
"""A
array('i', [100, -700, 300, 400, 800])"""

# nilai awal (sebelum dibalik)
"""A
array('i', [100, -700, 300, 400, 800])"""

# membalik urutan elemen array
A.reverse()

# nilai akhir (setelah dibalik)
"""A
array('i', [800, 400, 300, -700, 100])"""