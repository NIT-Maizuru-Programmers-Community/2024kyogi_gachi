matrix = [[i%2 for i in range(1,257)]for num in range(257)]

# 例えば、最初の行と最初の10要素を出力してみましょう
print(matrix[:128])


[[1 for num in range(8)]for i in range(8)],#8全部1
[[num%2 for i in range(8)]for num in range(1,9)],#8横に1
[[i%2 for i in range(1,9)]for num in range(8)],#8縦に1
                        
[[1 for num in range(16)]for i in range(16)],#16全部1
[[num%2 for i in range(16)]for num in range(1,17)],#16横に1
[[i%2 for i in range(1,17)]for num in range(16)],#16縦に1

[[1 for num in range(32)]for i in range(32)],#32全部1
[[num%2 for i in range(32)]for num in range(1,33)],#32横に1
[[i%2 for i in range(1,33)]for num in range(32)],#32縦に1


[[1 for num in range(64)]for i in range(64)],#64全部1
[[num%2 for i in range(64)]for num in range(1,65)],#64横に1
[[i%2 for i in range(1,65)]for num in range(64)],#64縦に1

[[1 for num in range(128)]for i in range(128)],#128全部1
[[num%2 for i in range(128)]for num in range(1,129)],#128横に1
[[i%2 for i in range(1,129)]for num in range(128)],#128縦に1


[[1 for num in range(256)]for i in range(256)],#256全部1
[[num%2 for i in range(256)]for num in range(1,257)],#256横に1
[[i%2 for i in range(1,257)]for num in range(257)]#256縦に1