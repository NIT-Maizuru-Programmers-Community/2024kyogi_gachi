general_patterns_p=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
general_patterns_width=[1,2,2,2,4,4,4,8,8,8,16,16,16,32,32,32,64,64,64,128,128,128,256,256,256]
general_patterns_height=[1,2,2,2,4,4,4,8,8,8,16,16,16,32,32,32,64,64,64,128,128,128,256,256,256]
general_patterns_cells=[
                        [[1]],

                        [[1,1],[1,1]],[[1,1],[0,0]],[[1,0],[1,0]],

                        [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]],
                        [[1,1,1,1],[0,0,0,0],[1,1,1,1],[0,0,0,0]],
                        [[1,0,1,0],[1,0,1,0],[1,0,1,0],[1,0,1,0]],

                        [[1 for num in range(8)]for i in range(8)],#32全部1
                        [[num%2 for i in range(8)]for num in range(1,9)],#32横に1
                        [[i%2 for i in range(1,9)]for num in range(8)],#32縦に1
                        
                        [[1 for num in range(16)]for i in range(16)],#32全部1
                        [[num%2 for i in range(16)]for num in range(1,17)],#32横に1
                        [[i%2 for i in range(1,17)]for num in range(16)],#32縦に1

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

                        ]






