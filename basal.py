# This module is setup to generate basal rate insulin delivery charts
# for the day.

import numpy as np
from rayleighcurve import Rayleigh

"""
    c = (m-1)/4.    # to get step only up to 4 hours
    
    xr  = []
    y   = []
    RC  = []

    x = 0           # abscissa
    for x in range(int(m)):
        y.append(x/c)
        x =+ 1

    x = 0
    for x in range(len(y)):
        xr.append((y[x]/(s**2))*np.exp((-y[x]**2)/(2*s**2)))
        x =+ 1
        
    z = sum(xr)

    x = 0
    for x in range(len(xr)):
        RC.append(xr[x]/z)
        x =+ 1
"""


def Basal(s,m):
    RC = Rayleigh(s,m)
    
    # s = 1
    # m = 49 see below

    # These values are multiplied by the basal rate on pump to get insulin
    # release per 5 minute interval.
    ##########################################################################
    # For an entire day there are 288 -
    # 5 minute intervals (24*60)/5 = 288 + 1 (0) = 289
    ##########################################################################
    # Insert 15 minutes of 0.0 to beginning of RC because it takes insulin
    # 15 minutes to react and get into the blood stream
    
    # We are looking at 5 minute intervals, so 15 minutes = inserting int = 2
    
    x = 0
    
    for x in range(2):
        RC.insert(0, 0.0)
        
    # Make RC Array for entire day

    BBL = RC

    x = 0
    for x in range(288-len(RC)):
        BBL.append(0.0)

    #RC1
    RC1 = BBL
    R1  = np.array(RC1)

    #RC2
    RC2 = RC1
    RC2.insert(0,0.0)
    RC2.pop()
    R2 = np.array(RC2)

    #RC3
    RC3 = RC2
    RC3.insert(0,0.0)
    RC3.pop()
    R3 = np.array(RC3)

    #RC4
    RC4 = RC3
    RC4.insert(0,0.0)
    RC4.pop()
    R4 = np.array(RC4)

    #RC5
    RC5 = RC4
    RC5.insert(0,0.0)
    RC5.pop()
    R5 = np.array(RC5)

    #RC6
    RC6 = RC5
    RC6.insert(0,0.0)
    RC6.pop()
    R6 = np.array(RC6)

    #RC7
    RC7 = RC6
    RC7.insert(0,0.0)
    RC7.pop()
    R7 = np.array(RC7)

    #RC8
    RC8 = RC7
    RC8.insert(0,0.0)
    RC8.pop()
    R8 = np.array(RC8)

    #RC9
    RC9 = RC8
    RC9.insert(0,0.0)
    RC9.pop()
    R9 = np.array(RC9)

    #RC10
    RC10 = RC9
    RC10.insert(0,0.0)
    RC10.pop()
    R10 = np.array(RC10)

    #RC11
    RC11 = RC10
    RC11.insert(0,0.0)
    RC11.pop()
    R11 = np.array(RC11)

    #RC12
    RC12 = RC11
    RC12.insert(0,0.0)
    RC12.pop()
    R12 = np.array(RC12)

    #RC13
    RC13 = RC12
    RC13.insert(0,0.0)
    RC13.pop()
    R13 = np.array(RC13)

    #RC14
    RC14 = RC13
    RC14.insert(0,0.0)
    RC14.pop()
    R14 = np.array(RC14)

    #RC15
    RC15 = RC14
    RC15.insert(0,0.0)
    RC15.pop()
    R15 = np.array(RC15)

    #RC16
    RC16 = RC15
    RC16.insert(0,0.0)
    RC16.pop()
    R16 = np.array(RC16)

    #RC17
    RC17 = RC16
    RC17.insert(0,0.0)
    RC17.pop()
    R17 = np.array(RC17)

    #RC18
    RC18 = RC17
    RC18.insert(0,0.0)
    RC18.pop()
    R18 = np.array(RC18)

    #RC19
    RC19 = RC18
    RC19.insert(0,0.0)
    RC19.pop()
    R19 = np.array(RC19)

    #RC20
    RC20 = RC19
    RC20.insert(0,0.0)
    RC20.pop()
    R20 = np.array(RC20)

    #RC21
    RC21 = RC20
    RC21.insert(0,0.0)
    RC21.pop()
    R21 = np.array(RC21)

    #RC22
    RC22 = RC21
    RC22.insert(0,0.0)
    RC22.pop()
    R22 = np.array(RC22)

    #RC23
    RC23 = RC22
    RC23.insert(0,0.0)
    RC23.pop()
    R23 = np.array(RC23)

    #RC24
    RC24 = RC23
    RC24.insert(0,0.0)
    RC24.pop()
    R24 = np.array(RC24)

    #RC25
    RC25 = RC24
    RC25.insert(0,0.0)
    RC25.pop()
    R25 = np.array(RC25)

    #RC26
    RC26 = RC25
    RC26.insert(0,0.0)
    RC26.pop()
    R26 = np.array(RC26)

    #RC27
    RC27 = RC26
    RC27.insert(0,0.0)
    RC27.pop()
    R27 = np.array(RC27)

    #RC28
    RC28 = RC27
    RC28.insert(0,0.0)
    RC28.pop()
    R28 = np.array(RC28)

    #RC29
    RC29 = RC28
    RC29.insert(0,0.0)
    RC29.pop()
    R29 = np.array(RC29)

    #RC30
    RC30 = RC29
    RC30.insert(0,0.0)
    RC30.pop()
    R30 = np.array(RC30)

    #RC31
    RC31 = RC30
    RC31.insert(0,RC30[len(RC30)-1])
    RC31.pop()
    R31 = np.array(RC31)

    #RC32
    RC32 = RC31
    RC32.insert(0,RC31[len(RC31)-1])
    RC32.pop()
    R32 = np.array(RC32)

    #RC33
    RC33 = RC32
    RC33.insert(0,RC32[len(RC32)-1])
    RC33.pop()
    R33 = np.array(RC33)

    #RC34
    RC34 = RC33
    RC34.insert(0,RC33[len(RC33)-1])
    RC34.pop()
    R34 = np.array(RC34)

    #RC35
    RC35 = RC34
    RC35.insert(0,RC34[len(RC34)-1])
    RC35.pop()
    R35 = np.array(RC35)

    #RC36
    RC36 = RC35
    RC36.insert(0,RC35[len(RC35)-1])
    RC36.pop()
    R36 = np.array(RC36)

    #RC37
    RC37 = RC36
    RC37.insert(0,RC36[len(RC36)-1])
    RC37.pop()
    R37 = np.array(RC37)

    #RC38
    RC38 = RC37
    RC38.insert(0,RC37[len(RC37)-1])
    RC38.pop()
    R38 = np.array(RC38)

    #RC39
    RC39 = RC38
    RC39.insert(0,RC38[len(RC38)-1])
    RC39.pop()
    R39 = np.array(RC39)

    #RC40
    RC40 = RC39
    RC40.insert(0,RC39[len(RC39)-1])
    RC40.pop()
    R40 = np.array(RC40)

    #RC41
    RC41 = RC40
    RC41.insert(0,RC40[len(RC40)-1])
    RC41.pop()
    R41 = np.array(RC41)

    #RC42
    RC42 = RC41
    RC42.insert(0,RC41[len(RC41)-1])
    RC42.pop()
    R42 = np.array(RC42)

    #RC43
    RC43 = RC42
    RC43.insert(0,RC42[len(RC42)-1])
    RC43.pop()
    R43 = np.array(RC43)

    #RC44
    RC44 = RC43
    RC44.insert(0,RC43[len(RC43)-1])
    RC44.pop()
    R44 = np.array(RC44)

    #RC45
    RC45 = RC44
    RC45.insert(0,RC44[len(RC44)-1])
    RC45.pop()
    R45 = np.array(RC45)

    #RC46
    RC46 = RC45
    RC46.insert(0,RC45[len(RC45)-1])
    RC46.pop()
    R46 = np.array(RC46)

    #RC47
    RC47 = RC46
    RC47.insert(0,RC46[len(RC46)-1])
    RC47.pop()
    R47 = np.array(RC47)

    #RC48
    RC48 = RC47
    RC48.insert(0,RC47[len(RC47)-1])
    RC48.pop()
    R48 = np.array(RC48)

    #RC49
    RC49 = RC48
    RC49.insert(0,RC48[len(RC48)-1])
    RC49.pop()
    R49 = np.array(RC49)

    #RC50
    RC50 = RC49
    RC50.insert(0,RC49[len(RC49)-1])
    RC50.pop()
    R50 = np.array(RC50)

    #RC51
    RC51 = RC50
    RC51.insert(0,RC50[len(RC50)-1])
    RC51.pop()
    R51 = np.array(RC51)

    #RC52
    RC52 = RC51
    RC52.insert(0,RC51[len(RC51)-1])
    RC52.pop()
    R52 = np.array(RC52)

    #RC53
    RC53 = RC52
    RC53.insert(0,RC52[len(RC52)-1])
    RC53.pop()
    R53 = np.array(RC53)

    #RC54
    RC54 = RC53
    RC54.insert(0,RC53[len(RC53)-1])
    RC54.pop()
    R54 = np.array(RC54)

    #RC55
    RC55 = RC54
    RC55.insert(0,RC54[len(RC54)-1])
    RC55.pop()
    R55 = np.array(RC55)

    #RC56
    RC56 = RC55
    RC56.insert(0,RC55[len(RC55)-1])
    RC56.pop()
    R56 = np.array(RC56)

    #RC57
    RC57 = RC56
    RC57.insert(0,RC56[len(RC56)-1])
    RC57.pop()
    R57 = np.array(RC57)

    #RC58
    RC58 = RC57
    RC58.insert(0,RC57[len(RC57)-1])
    RC58.pop()
    R58 = np.array(RC58)

    #RC59
    RC59 = RC58
    RC59.insert(0,RC58[len(RC58)-1])
    RC59.pop()
    R59 = np.array(RC59)

    #RC60
    RC60 = RC59
    RC60.insert(0,RC59[len(RC59)-1])
    RC60.pop()
    R60 = np.array(RC60)

    #RC61
    RC61 = RC60
    RC61.insert(0,RC60[len(RC60)-1])
    RC61.pop()
    R61 = np.array(RC61)

    #RC62
    RC62 = RC61
    RC62.insert(0,RC61[len(RC61)-1])
    RC62.pop()
    R62 = np.array(RC62)

    #RC63
    RC63 = RC62
    RC63.insert(0,RC62[len(RC62)-1])
    RC63.pop()
    R63 = np.array(RC63)

    #RC64
    RC64 = RC63
    RC64.insert(0,RC63[len(RC63)-1])
    RC64.pop()
    R64 = np.array(RC64)

    #RC65
    RC65 = RC64
    RC65.insert(0,RC64[len(RC64)-1])
    RC65.pop()
    R65 = np.array(RC65)

    #RC66
    RC66 = RC65
    RC66.insert(0,RC65[len(RC65)-1])
    RC66.pop()
    R66 = np.array(RC66)

    #RC67
    RC67 = RC66
    RC67.insert(0,RC66[len(RC66)-1])
    RC67.pop()
    R67 = np.array(RC67)

    #RC68
    RC68 = RC67
    RC68.insert(0,RC67[len(RC67)-1])
    RC68.pop()
    R68 = np.array(RC68)

    #RC69
    RC69 = RC68
    RC69.insert(0,RC68[len(RC68)-1])
    RC69.pop()
    R69 = np.array(RC69)

    #RC70
    RC70 = RC69
    RC70.insert(0,RC69[len(RC69)-1])
    RC70.pop()
    R70 = np.array(RC70)

    #RC71
    RC71 = RC70
    RC71.insert(0,RC70[len(RC70)-1])
    RC71.pop()
    R71 = np.array(RC71)

    #RC72
    RC72 = RC71
    RC72.insert(0,RC71[len(RC71)-1])
    RC72.pop()
    R72= np.array(RC72)

    #RC73
    RC73 = RC72
    RC73.insert(0,RC72[len(RC72)-1])
    RC73.pop()
    R73 = np.array(RC73)

    #RC74
    RC74 = RC73
    RC74.insert(0,RC73[len(RC73)-1])
    RC74.pop()
    R74 = np.array(RC74)

    #RC75
    RC75 = RC74
    RC75.insert(0,RC74[len(RC74)-1])
    RC75.pop()
    R75 = np.array(RC75)

    #RC76
    RC76 = RC75
    RC76.insert(0,RC75[len(RC75)-1])
    RC76.pop()
    R76 = np.array(RC76)

    #RC77
    RC77 = RC76
    RC77.insert(0,RC76[len(RC76)-1])
    RC77.pop()
    R77 = np.array(RC77)

    #RC78
    RC78 = RC77
    RC78.insert(0,RC77[len(RC77)-1])
    RC78.pop()
    R78 = np.array(RC78)

    #RC79
    RC79 = RC78
    RC79.insert(0,RC78[len(RC78)-1])
    RC79.pop()
    R79 = np.array(RC79)

    #RC80
    RC80 = RC79
    RC80.insert(0,RC79[len(RC79)-1])
    RC80.pop()
    R80 = np.array(RC80)

    #RC81
    RC81 = RC80
    RC81.insert(0,RC80[len(RC80)-1])
    RC81.pop()
    R81 = np.array(RC81)

    #RC82
    RC82 = RC81
    RC82.insert(0,RC81[len(RC81)-1])
    RC82.pop()
    R82 = np.array(RC82)

    #RC83
    RC83 = RC82
    RC83.insert(0,RC82[len(RC82)-1])
    RC83.pop()
    R83 = np.array(RC83)

    #RC84
    RC84 = RC83
    RC84.insert(0,RC83[len(RC83)-1])
    RC84.pop()
    R84 = np.array(RC84)

    #RC85
    RC85 = RC84
    RC85.insert(0,RC84[len(RC84)-1])
    RC85.pop()
    R85 = np.array(RC85)

    #RC86
    RC86 = RC85
    RC86.insert(0,RC85[len(RC85)-1])
    RC86.pop()
    R86 = np.array(RC86)

    #RC87
    RC87 = RC86
    RC87.insert(0,RC86[len(RC86)-1])
    RC87.pop()
    R87 = np.array(RC87)

    #RC88
    RC88 = RC87
    RC88.insert(0,RC87[len(RC87)-1])
    RC88.pop()
    R88 = np.array(RC88)

    #RC89
    RC89 = RC88
    RC89.insert(0,RC88[len(RC88)-1])
    RC89.pop()
    R89 = np.array(RC89)

    #RC90
    RC90 = RC89
    RC90.insert(0,RC89[len(RC89)-1])
    RC90.pop()
    R90 = np.array(RC90)

    #RC91
    RC91 = RC90
    RC91.insert(0,RC90[len(RC90)-1])
    RC91.pop()
    R91 = np.array(RC91)

    #RC92
    RC92 = RC91
    RC92.insert(0,RC91[len(RC91)-1])
    RC92.pop()
    R92 = np.array(RC92)

    #RC93
    RC93 = RC92
    RC93.insert(0,RC92[len(RC92)-1])
    RC93.pop()
    R93 = np.array(RC93)

    #RC94
    RC94 = RC93
    RC94.insert(0,RC93[len(RC93)-1])
    RC94.pop()
    R94 = np.array(RC94)

    #RC95
    RC95 = RC94
    RC95.insert(0,RC94[len(RC94)-1])
    RC95.pop()
    R95 = np.array(RC95)

    #RC96
    RC96 = RC95
    RC96.insert(0,RC95[len(RC95)-1])
    RC96.pop()
    R96 = np.array(RC96)

    #RC97
    RC97 = RC96
    RC97.insert(0,RC96[len(RC96)-1])
    RC97.pop()
    R97 = np.array(RC97)

    #RC98
    RC98 = RC97
    RC98.insert(0,RC97[len(RC97)-1])
    RC98.pop()
    R98 = np.array(RC98)

    #RC99
    RC99 = RC98
    RC99.insert(0,RC98[len(RC98)-1])
    RC99.pop()
    R99 = np.array(RC99)

    #RC100
    RC100 = RC99
    RC100.insert(0,RC99[len(RC99)-1])
    RC100.pop()
    R100 = np.array(RC100)

    #RC101
    RC101 = RC100
    RC101.insert(0,RC100[len(RC100)-1])
    RC101.pop()
    R101 = np.array(RC101)

    #RC102
    RC102 = RC101
    RC102.insert(0,RC101[len(RC101)-1])
    RC102.pop()
    R102 = np.array(RC102)

    #RC103
    RC103 = RC102
    RC103.insert(0,RC102[len(RC102)-1])
    RC103.pop()
    R103 = np.array(RC103)

    #RC104
    RC104 = RC103
    RC104.insert(0,RC103[len(RC103)-1])
    RC104.pop()
    R104 = np.array(RC104)

    #RC105
    RC105 = RC104
    RC105.insert(0,RC104[len(RC104)-1])
    RC105.pop()
    R105 = np.array(RC105)

    #RC106
    RC106 = RC105
    RC106.insert(0,RC105[len(RC105)-1])
    RC106.pop()
    R106 = np.array(RC106)

    #RC107
    RC107 = RC106
    RC107.insert(0,RC106[len(RC106)-1])
    RC107.pop()
    R107 = np.array(RC107)

    #RC108
    RC108 = RC107
    RC108.insert(0,RC107[len(RC107)-1])
    RC108.pop()
    R108 = np.array(RC108)

    #RC109
    RC109 = RC108
    RC109.insert(0,RC108[len(RC108)-1])
    RC109.pop()
    R109 = np.array(RC109)

    #RC110
    RC110 = RC109
    RC110.insert(0,RC109[len(RC109)-1])
    RC110.pop()
    R110 = np.array(RC110)

    #RC111
    RC111 = RC110
    RC111.insert(0,RC110[len(RC110)-1])
    RC111.pop()
    R111 = np.array(RC111)

    #RC112
    RC112 = RC111
    RC112.insert(0,RC111[len(RC111)-1])
    RC112.pop()
    R112 = np.array(RC112)

    #RC113
    RC113 = RC112
    RC113.insert(0,RC112[len(RC112)-1])
    RC113.pop()
    R113 = np.array(RC113)

    #RC114
    RC114 = RC113
    RC114.insert(0,RC113[len(RC113)-1])
    RC114.pop()
    R114 = np.array(RC114)

    #RC115
    RC115 = RC114
    RC115.insert(0,RC114[len(RC114)-1])
    RC115.pop()
    R115 = np.array(RC115)

    #RC116
    RC116 = RC115
    RC116.insert(0,RC115[len(RC115)-1])
    RC116.pop()
    R116 = np.array(RC116)

    #RC117
    RC117 = RC116
    RC117.insert(0,RC116[len(RC116)-1])
    RC117.pop()
    R117 = np.array(RC117)

    #RC118
    RC118 = RC117
    RC118.insert(0,RC117[len(RC117)-1])
    RC118.pop()
    R118 = np.array(RC118)

    #RC119
    RC119 = RC118
    RC119.insert(0,RC118[len(RC118)-1])
    RC119.pop()
    R119 = np.array(RC119)

    #RC120
    RC120 = RC119
    RC120.insert(0,RC119[len(RC119)-1])
    RC120.pop()
    R120 = np.array(RC120)

    #RC121
    RC121 = RC120
    RC121.insert(0,RC120[len(RC120)-1])
    RC121.pop()
    R121 = np.array(RC121)

    #RC122
    RC122 = RC121
    RC122.insert(0,RC121[len(RC121)-1])
    RC122.pop()
    R122 = np.array(RC122)

    #RC123
    RC123 = RC122
    RC123.insert(0,RC122[len(RC122)-1])
    RC123.pop()
    R123 = np.array(RC123)

    #RC124
    RC124 = RC123
    RC124.insert(0,RC123[len(RC123)-1])
    RC124.pop()
    R124 = np.array(RC124)

    #RC125
    RC125 = RC124
    RC125.insert(0,RC124[len(RC124)-1])
    RC125.pop()
    R125 = np.array(RC125)

    #RC126
    RC126 = RC125
    RC126.insert(0,RC125[len(RC125)-1])
    RC126.pop()
    R126 = np.array(RC126)

    #RC127
    RC127 = RC126
    RC127.insert(0,RC126[len(RC126)-1])
    RC127.pop()
    R127 = np.array(RC127)

    #RC128
    RC128 = RC127
    RC128.insert(0,RC127[len(RC127)-1])
    RC128.pop()
    R128 = np.array(RC128)

    #RC129
    RC129 = RC128
    RC129.insert(0,RC128[len(RC128)-1])
    RC129.pop()
    R129 = np.array(RC129)

    #RC130
    RC130 = RC129
    RC130.insert(0,RC129[len(RC129)-1])
    RC130.pop()
    R130 = np.array(RC130)

    #RC131
    RC131 = RC130
    RC131.insert(0,RC130[len(RC130)-1])
    RC131.pop()
    R131 = np.array(RC131)

    #RC132
    RC132 = RC131
    RC132.insert(0,RC131[len(RC131)-1])
    RC132.pop()
    R132 = np.array(RC132)

    #RC133
    RC133 = RC132
    RC133.insert(0,RC132[len(RC132)-1])
    RC133.pop()
    R133 = np.array(RC133)

    #RC134
    RC134 = RC133
    RC134.insert(0,RC133[len(RC133)-1])
    RC134.pop()
    R134 = np.array(RC134)

    #RC135
    RC135 = RC134
    RC135.insert(0,RC134[len(RC134)-1])
    RC135.pop()
    R135 = np.array(RC135)

    #RC136
    RC136 = RC135
    RC136.insert(0,RC135[len(RC135)-1])
    RC136.pop()
    R136 = np.array(RC136)

    #RC137
    RC137 = RC136
    RC137.insert(0,RC136[len(RC136)-1])
    RC137.pop()
    R137 = np.array(RC137)

    #RC138
    RC138 = RC137
    RC138.insert(0,RC137[len(RC137)-1])
    RC138.pop()
    R138 = np.array(RC138)

    #RC139
    RC139 = RC138
    RC139.insert(0,RC138[len(RC138)-1])
    RC139.pop()
    R139 = np.array(RC139)

    #RC140
    RC140 = RC139
    RC140.insert(0,RC139[len(RC139)-1])
    RC140.pop()
    R140 = np.array(RC140)

    #RC141
    RC141 = RC140
    RC141.insert(0,RC140[len(RC140)-1])
    RC141.pop()
    R141 = np.array(RC141)

    #RC142
    RC142 = RC141
    RC142.insert(0,RC141[len(RC141)-1])
    RC142.pop()
    R142 = np.array(RC142)

    #RC143
    RC143 = RC142
    RC143.insert(0,RC142[len(RC142)-1])
    RC143.pop()
    R143 = np.array(RC143)

    #RC144
    RC144 = RC143
    RC144.insert(0,RC143[len(RC143)-1])
    RC144.pop()
    R144 = np.array(RC144)

    #RC145
    RC145 = RC144
    RC145.insert(0,RC144[len(RC144)-1])
    RC145.pop()
    R145 = np.array(RC145)

    #RC146
    RC146 = RC145
    RC146.insert(0,RC145[len(RC145)-1])
    RC146.pop()
    R146 = np.array(RC146)

    #RC147
    RC147 = RC146
    RC147.insert(0,RC146[len(RC146)-1])
    RC147.pop()
    R147 = np.array(RC147)

    #RC148
    RC148 = RC147
    RC148.insert(0,RC147[len(RC147)-1])
    RC148.pop()
    R148 = np.array(RC148)

    #RC149
    RC149 = RC148
    RC149.insert(0,RC148[len(RC148)-1])
    RC149.pop()
    R149 = np.array(RC149)

    #RC150
    RC150 = RC149
    RC150.insert(0,RC149[len(RC149)-1])
    RC150.pop()
    R150 = np.array(RC150)

    #RC151
    RC151 = RC150
    RC151.insert(0,RC150[len(RC150)-1])
    RC151.pop()
    R151 = np.array(RC151)

    #RC152
    RC152 = RC151
    RC152.insert(0,RC151[len(RC151)-1])
    RC152.pop()
    R152 = np.array(RC152)

    #RC153
    RC153 = RC152
    RC153.insert(0,RC152[len(RC152)-1])
    RC153.pop()
    R153 = np.array(RC153)

    #RC154
    RC154 = RC153
    RC154.insert(0,RC153[len(RC153)-1])
    RC154.pop()
    R154 = np.array(RC154)

    #RC155
    RC155 = RC154
    RC155.insert(0,RC154[len(RC154)-1])
    RC155.pop()
    R155 = np.array(RC155)

    #RC156
    RC156 = RC155
    RC156.insert(0,RC155[len(RC155)-1])
    RC156.pop()
    R156 = np.array(RC156)

    #RC157
    RC157 = RC156
    RC157.insert(0,RC156[len(RC156)-1])
    RC157.pop()
    R157 = np.array(RC157)

    #RC158
    RC158 = RC157
    RC158.insert(0,RC157[len(RC157)-1])
    RC158.pop()
    R158 = np.array(RC158)

    #RC159
    RC159 = RC158
    RC159.insert(0,RC158[len(RC158)-1])
    RC159.pop()
    R159 = np.array(RC159)

    #RC160
    RC160 = RC159
    RC160.insert(0,RC159[len(RC159)-1])
    RC160.pop()
    R160 = np.array(RC160)

    #RC161
    RC161 = RC160
    RC161.insert(0,RC160[len(RC160)-1])
    RC161.pop()
    R161 = np.array(RC161)

    #RC162
    RC162 = RC161
    RC162.insert(0,RC161[len(RC161)-1])
    RC162.pop()
    R162 = np.array(RC162)

    #RC163
    RC163 = RC162
    RC163.insert(0,RC162[len(RC162)-1])
    RC163.pop()
    R163 = np.array(RC163)

    #RC164
    RC164 = RC163
    RC164.insert(0,RC163[len(RC163)-1])
    RC164.pop()
    R164 = np.array(RC164)

    #RC165
    RC165 = RC164
    RC165.insert(0,RC164[len(RC164)-1])
    RC165.pop()
    R165 = np.array(RC165)

    #RC166
    RC166 = RC165
    RC166.insert(0,RC165[len(RC165)-1])
    RC166.pop()
    R166 = np.array(RC166)

    #RC167
    RC167 = RC166
    RC167.insert(0,RC166[len(RC166)-1])
    RC167.pop()
    R167 = np.array(RC167)

    #RC168
    RC168 = RC167
    RC168.insert(0,RC167[len(RC167)-1])
    RC168.pop()
    R168 = np.array(RC168)

    #RC169
    RC169 = RC168
    RC169.insert(0,RC168[len(RC168)-1])
    RC169.pop()
    R169 = np.array(RC169)

    #RC170
    RC170 = RC169
    RC170.insert(0,RC169[len(RC169)-1])
    RC170.pop()
    R170 = np.array(RC170)

    #RC171
    RC171 = RC170
    RC171.insert(0,RC170[len(RC170)-1])
    RC171.pop()
    R171 = np.array(RC171)

    #RC172
    RC172 = RC171
    RC172.insert(0,RC171[len(RC171)-1])
    RC172.pop()
    R172 = np.array(RC172)

    #RC173
    RC173 = RC172
    RC173.insert(0,RC172[len(RC172)-1])
    RC173.pop()
    R173 = np.array(RC173)

    #RC174
    RC174 = RC173
    RC174.insert(0,RC173[len(RC173)-1])
    RC174.pop()
    R174 = np.array(RC174)

    #RC175
    RC175 = RC174
    RC175.insert(0,RC174[len(RC174)-1])
    RC175.pop()
    R175 = np.array(RC175)

    #RC176
    RC176 = RC175
    RC176.insert(0,RC175[len(RC175)-1])
    RC176.pop()
    R176 = np.array(RC176)

    #RC177
    RC177 = RC176
    RC177.insert(0,RC176[len(RC176)-1])
    RC177.pop()
    R177 = np.array(RC177)

    #RC178
    RC178 = RC177
    RC178.insert(0,RC177[len(RC177)-1])
    RC178.pop()
    R178 = np.array(RC178)

    #RC179
    RC179 = RC178
    RC179.insert(0,RC178[len(RC178)-1])
    RC179.pop()
    R179 = np.array(RC179)

    #RC180
    RC180 = RC179
    RC180.insert(0,RC179[len(RC179)-1])
    RC180.pop()
    R180 = np.array(RC180)

    #RC181
    RC181 = RC180
    RC181.insert(0,RC180[len(RC180)-1])
    RC181.pop()
    R181 = np.array(RC181)

    #RC182
    RC182 = RC181
    RC182.insert(0,RC181[len(RC181)-1])
    RC182.pop()
    R182 = np.array(RC182)

    #RC183
    RC183 = RC182
    RC183.insert(0,RC182[len(RC182)-1])
    RC183.pop()
    R183 = np.array(RC183)

    #RC184
    RC184 = RC183
    RC184.insert(0,RC183[len(RC183)-1])
    RC184.pop()
    R184 = np.array(RC184)

    #RC185
    RC185 = RC184
    RC185.insert(0,RC184[len(RC184)-1])
    RC185.pop()
    R185 = np.array(RC185)

    #RC186
    RC186 = RC185
    RC186.insert(0,RC185[len(RC185)-1])
    RC186.pop()
    R186 = np.array(RC186)

    #RC187
    RC187 = RC186
    RC187.insert(0,RC186[len(RC186)-1])
    RC187.pop()
    R187 = np.array(RC187)

    #RC188
    RC188 = RC187
    RC188.insert(0,RC187[len(RC187)-1])
    RC188.pop()
    R188 = np.array(RC188)

    #RC189
    RC189 = RC188
    RC189.insert(0,RC188[len(RC188)-1])
    RC189.pop()
    R189 = np.array(RC189)

    #RC190
    RC190 = RC189
    RC190.insert(0,RC189[len(RC189)-1])
    RC190.pop()
    R190 = np.array(RC190)

    #RC191
    RC191 = RC190
    RC191.insert(0,RC190[len(RC190)-1])
    RC191.pop()
    R191 = np.array(RC191)

    #RC192
    RC192 = RC191
    RC192.insert(0,RC191[len(RC191)-1])
    RC192.pop()
    R192 = np.array(RC192)

    #RC193
    RC193 = RC192
    RC193.insert(0,RC192[len(RC192)-1])
    RC193.pop()
    R193 = np.array(RC193)

    #RC194
    RC194 = RC193
    RC194.insert(0,RC193[len(RC193)-1])
    RC194.pop()
    R194 = np.array(RC194)

    #RC195
    RC195 = RC194
    RC195.insert(0,RC194[len(RC194)-1])
    RC195.pop()
    R195 = np.array(RC195)

    #RC196
    RC196 = RC195
    RC196.insert(0,RC195[len(RC195)-1])
    RC196.pop()
    R196 = np.array(RC196)

    #RC197
    RC197 = RC196
    RC197.insert(0,RC196[len(RC196)-1])
    RC197.pop()
    R197 = np.array(RC197)

    #RC198
    RC198 = RC197
    RC198.insert(0,RC197[len(RC197)-1])
    RC198.pop()
    R198 = np.array(RC198)

    #RC199
    RC199 = RC198
    RC199.insert(0,RC198[len(RC198)-1])
    RC199.pop()
    R199 = np.array(RC199)

    #RC200
    RC200 = RC199
    RC200.insert(0,RC199[len(RC199)-1])
    RC200.pop()
    R200 = np.array(RC200)

    #RC201
    RC201 = RC200
    RC201.insert(0,RC200[len(RC200)-1])
    RC201.pop()
    R201 = np.array(RC201)

    #RC202
    RC202 = RC201
    RC202.insert(0,RC201[len(RC201)-1])
    RC202.pop()
    R202 = np.array(RC202)

    #RC203
    RC203 = RC202
    RC203.insert(0,RC202[len(RC202)-1])
    RC203.pop()
    R203 = np.array(RC203)

    #RC204
    RC204 = RC203
    RC204.insert(0,RC203[len(RC203)-1])
    RC204.pop()
    R204 = np.array(RC204)

    #RC205
    RC205 = RC204
    RC205.insert(0,RC204[len(RC204)-1])
    RC205.pop()
    R205 = np.array(RC205)

    #RC206
    RC206 = RC205
    RC206.insert(0,RC205[len(RC205)-1])
    RC206.pop()
    R206 = np.array(RC206)

    #RC207
    RC207 = RC206
    RC207.insert(0,RC206[len(RC206)-1])
    RC207.pop()
    R207 = np.array(RC207)

    #RC208
    RC208 = RC207
    RC208.insert(0,RC207[len(RC207)-1])
    RC208.pop()
    R208 = np.array(RC208)

    #RC209
    RC209 = RC208
    RC209.insert(0,RC208[len(RC208)-1])
    RC209.pop()
    R209 = np.array(RC209)

    #RC210
    RC210 = RC209
    RC210.insert(0,RC209[len(RC209)-1])
    RC210.pop()
    R210 = np.array(RC210)

    #RC211
    RC211 = RC210
    RC211.insert(0,RC210[len(RC210)-1])
    RC211.pop()
    R211 = np.array(RC211)

    #RC212
    RC212 = RC211
    RC212.insert(0,RC211[len(RC211)-1])
    RC212.pop()
    R212 = np.array(RC212)

    #RC213
    RC213 = RC212
    RC213.insert(0,RC212[len(RC212)-1])
    RC213.pop()
    R213 = np.array(RC213)

    #RC214
    RC214 = RC213
    RC214.insert(0,RC213[len(RC213)-1])
    RC214.pop()
    R214 = np.array(RC214)

    #RC215
    RC215 = RC214
    RC215.insert(0,RC214[len(RC214)-1])
    RC215.pop()
    R215 = np.array(RC215)

    #RC216
    RC216 = RC215
    RC216.insert(0,RC215[len(RC215)-1])
    RC216.pop()
    R216 = np.array(RC216)

    #RC217
    RC217 = RC216
    RC217.insert(0,RC216[len(RC216)-1])
    RC217.pop()
    R217 = np.array(RC217)

    #RC218
    RC218 = RC217
    RC218.insert(0,RC217[len(RC217)-1])
    RC218.pop()
    R218 = np.array(RC218)

    #RC219
    RC219 = RC218
    RC219.insert(0,RC218[len(RC218)-1])
    RC219.pop()
    R219 = np.array(RC219)

    #RC220
    RC220 = RC219
    RC220.insert(0,RC219[len(RC219)-1])
    RC220.pop()
    R220 = np.array(RC220)

    #RC221
    RC221 = RC220
    RC221.insert(0,RC220[len(RC220)-1])
    RC221.pop()
    R221 = np.array(RC221)

    #RC222
    RC222 = RC221
    RC222.insert(0,RC221[len(RC221)-1])
    RC222.pop()
    R222 = np.array(RC222)

    #RC223
    RC223 = RC222
    RC223.insert(0,RC222[len(RC222)-1])
    RC223.pop()
    R223 = np.array(RC223)

    #RC224
    RC224 = RC223
    RC224.insert(0,RC223[len(RC223)-1])
    RC224.pop()
    R224 = np.array(RC224)

    #RC225
    RC225 = RC224
    RC225.insert(0,RC224[len(RC224)-1])
    RC225.pop()
    R225 = np.array(RC225)

    #RC226
    RC226 = RC225
    RC226.insert(0,RC225[len(RC225)-1])
    RC226.pop()
    R226 = np.array(RC226)

    #RC227
    RC227 = RC226
    RC227.insert(0,RC226[len(RC226)-1])
    RC227.pop()
    R227 = np.array(RC227)

    #RC228
    RC228 = RC227
    RC228.insert(0,RC227[len(RC227)-1])
    RC228.pop()
    R228 = np.array(RC228)

    #RC229
    RC229 = RC228
    RC229.insert(0,RC228[len(RC228)-1])
    RC229.pop()
    R229 = np.array(RC229)

    #RC230
    RC230 = RC229
    RC230.insert(0,RC229[len(RC229)-1])
    RC230.pop()
    R230 = np.array(RC230)

    #RC231
    RC231 = RC230
    RC231.insert(0,RC230[len(RC230)-1])
    RC231.pop()
    R231 = np.array(RC231)

    #RC232
    RC232 = RC231
    RC232.insert(0,RC231[len(RC231)-1])
    RC232.pop()
    R232 = np.array(RC232)

    #RC233
    RC233 = RC232
    RC233.insert(0,RC232[len(RC232)-1])
    RC233.pop()
    R233 = np.array(RC233)

    #RC234
    RC234 = RC233
    RC234.insert(0,RC233[len(RC233)-1])
    RC234.pop()
    R234 = np.array(RC234)

    #RC235
    RC235 = RC234
    RC235.insert(0,RC234[len(RC234)-1])
    RC235.pop()
    R235 = np.array(RC235)

    #RC236
    RC236 = RC235
    RC236.insert(0,RC235[len(RC235)-1])
    RC236.pop()
    R236 = np.array(RC236)

    #RC237
    RC237 = RC236
    RC237.insert(0,RC236[len(RC236)-1])
    RC237.pop()
    R237 = np.array(RC237)

    #RC238
    RC238 = RC237
    RC238.insert(0,RC237[len(RC237)-1])
    RC238.pop()
    R238 = np.array(RC238)

    #RC239
    RC239 = RC238
    RC239.insert(0,RC238[len(RC238)-1])
    RC239.pop()
    R239 = np.array(RC239)

    #RC240
    RC240 = RC239
    RC240.insert(0,RC239[len(RC239)-1])
    RC240.pop()
    R240 = np.array(RC240)

    #RC241
    RC241 = RC240
    RC241.insert(0,RC240[len(RC240)-1])
    RC241.pop()
    R241 = np.array(RC241)

    #RC242
    RC242 = RC241
    RC242.insert(0,RC241[len(RC241)-1])
    RC242.pop()
    R242 = np.array(RC242)

    #RC243
    RC243 = RC242
    RC243.insert(0,RC242[len(RC242)-1])
    RC243.pop()
    R243 = np.array(RC243)

    #RC244
    RC244 = RC243
    RC244.insert(0,RC243[len(RC243)-1])
    RC244.pop()
    R244 = np.array(RC244)

    #RC245
    RC245 = RC244
    RC245.insert(0,RC244[len(RC244)-1])
    RC245.pop()
    R245 = np.array(RC245)

    #RC246
    RC246 = RC245
    RC246.insert(0,RC245[len(RC245)-1])
    RC246.pop()
    R246 = np.array(RC246)

    #RC247
    RC247 = RC246
    RC247.insert(0,RC246[len(RC246)-1])
    RC247.pop()
    R247 = np.array(RC247)

    #RC248
    RC248 = RC247
    RC248.insert(0,RC247[len(RC247)-1])
    RC248.pop()
    R248 = np.array(RC248)

    #RC249
    RC249 = RC248
    RC249.insert(0,RC248[len(RC248)-1])
    RC249.pop()
    R249 = np.array(RC249)

    #RC250
    RC250 = RC249
    RC250.insert(0,RC249[len(RC249)-1])
    RC250.pop()
    R250 = np.array(RC250)

    #RC251
    RC251 = RC250
    RC251.insert(0,RC250[len(RC250)-1])
    RC251.pop()
    R251 = np.array(RC251)

    #RC252
    RC252 = RC251
    RC252.insert(0,RC251[len(RC251)-1])
    RC252.pop()
    R252 = np.array(RC252)

    #RC253
    RC253 = RC252
    RC253.insert(0,RC252[len(RC252)-1])
    RC253.pop()
    R253 = np.array(RC253)

    #RC254
    RC254 = RC253
    RC254.insert(0,RC253[len(RC253)-1])
    RC254.pop()
    R254 = np.array(RC254)

    #RC255
    RC255 = RC254
    RC255.insert(0,RC254[len(RC254)-1])
    RC255.pop()
    R255 = np.array(RC255)

    #RC256
    RC256 = RC255
    RC256.insert(0,RC255[len(RC255)-1])
    RC256.pop()
    R256 = np.array(RC256)

    #RC257
    RC257 = RC256
    RC257.insert(0,RC256[len(RC256)-1])
    RC257.pop()
    R257 = np.array(RC257)

    #RC258
    RC258 = RC257
    RC258.insert(0,RC257[len(RC257)-1])
    RC258.pop()
    R258 = np.array(RC258)

    #RC259
    RC259 = RC258
    RC259.insert(0,RC258[len(RC258)-1])
    RC259.pop()
    R259 = np.array(RC259)

    #RC260
    RC260 = RC259
    RC260.insert(0,RC259[len(RC259)-1])
    RC260.pop()
    R260 = np.array(RC260)

    #RC261
    RC261 = RC260
    RC261.insert(0,RC260[len(RC260)-1])
    RC261.pop()
    R261 = np.array(RC261)

    #RC262
    RC262 = RC261
    RC262.insert(0,RC261[len(RC261)-1])
    RC262.pop()
    R262 = np.array(RC262)

    #RC263
    RC263 = RC262
    RC263.insert(0,RC262[len(RC262)-1])
    RC263.pop()
    R263 = np.array(RC263)

    #RC264
    RC264 = RC263
    RC264.insert(0,RC263[len(RC263)-1])
    RC264.pop()
    R264 = np.array(RC264)

    #RC265
    RC265 = RC264
    RC265.insert(0,RC264[len(RC264)-1])
    RC265.pop()
    R265 = np.array(RC265)

    #RC266
    RC266 = RC265
    RC266.insert(0,RC265[len(RC265)-1])
    RC266.pop()
    R266 = np.array(RC266)

    #RC267
    RC267 = RC266
    RC267.insert(0,RC266[len(RC266)-1])
    RC267.pop()
    R267 = np.array(RC267)

    #RC268
    RC268 = RC267
    RC268.insert(0,RC267[len(RC267)-1])
    RC268.pop()
    R268 = np.array(RC268)

    #RC269
    RC269 = RC268
    RC269.insert(0,RC268[len(RC268)-1])
    RC269.pop()
    R269 = np.array(RC269)

    #RC270
    RC270 = RC269
    RC270.insert(0,RC269[len(RC269)-1])
    RC270.pop()
    R270 = np.array(RC270)

    #RC271
    RC271 = RC270
    RC271.insert(0,RC270[len(RC270)-1])
    RC271.pop()
    R271 = np.array(RC271)

    #RC272
    RC272 = RC271
    RC272.insert(0,RC271[len(RC271)-1])
    RC272.pop()
    R272 = np.array(RC272)

    #RC273
    RC273 = RC272
    RC273.insert(0,RC272[len(RC272)-1])
    RC273.pop()
    R273 = np.array(RC273)

    #RC274
    RC274 = RC273
    RC274.insert(0,RC273[len(RC273)-1])
    RC274.pop()
    R274 = np.array(RC274)

    #RC275
    RC275 = RC274
    RC275.insert(0,RC274[len(RC274)-1])
    RC275.pop()
    R275 = np.array(RC275)

    #RC276
    RC276 = RC275
    RC276.insert(0,RC275[len(RC275)-1])
    RC276.pop()
    R276 = np.array(RC276)

    #RC277
    RC277 = RC276
    RC277.insert(0,RC276[len(RC276)-1])
    RC277.pop()
    R277 = np.array(RC277)

    #RC278
    RC278 = RC277
    RC278.insert(0,RC277[len(RC277)-1])
    RC278.pop()
    R278 = np.array(RC278)

    #RC279
    RC279 = RC278
    RC279.insert(0,RC278[len(RC278)-1])
    RC279.pop()
    R279 = np.array(RC279)

    #RC280
    RC280 = RC279
    RC280.insert(0,RC279[len(RC279)-1])
    RC280.pop()
    R280 = np.array(RC280)

    #RC281
    RC281 = RC280
    RC281.insert(0,RC280[len(RC280)-1])
    RC281.pop()
    R281 = np.array(RC281)

    #RC282
    RC282 = RC281
    RC282.insert(0,RC281[len(RC281)-1])
    RC282.pop()
    R282 = np.array(RC282)

    #RC283
    RC283 = RC282
    RC283.insert(0,RC282[len(RC282)-1])
    RC283.pop()
    R283 = np.array(RC283)

    #RC284
    RC284 = RC283
    RC284.insert(0,RC283[len(RC283)-1])
    RC284.pop()
    R284 = np.array(RC284)

    #RC285
    RC285 = RC284
    RC285.insert(0,RC284[len(RC284)-1])
    RC285.pop()
    R285 = np.array(RC285)

    #RC286
    RC286 = RC285
    RC286.insert(0,RC285[len(RC285)-1])
    RC286.pop()
    R286 = np.array(RC286)

    #RC287
    RC287 = RC286
    RC287.insert(0,RC286[len(RC286)-1])
    RC287.pop()
    R287 = np.array(RC287)

    #RC288
    RC288 = RC287
    RC288.insert(0,RC287[len(RC287)-1])
    RC288.pop()
    R288 = np.array(RC288)

    #RC289
    #RC289 = RC288
    #RC289.insert(0,RC288[len(RC288)-1])
    #RC289.pop()
    #R289 = np.array(RC289)

    RA = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49, R50, R51, R52, R53, R54, R55, R56, R57, R58, R59, R60, R61, R62, R63, R64, R65,R66,R67,R68,R69,R70,R71,R72,R73,R74,R75,R76,R77,R78,R79,R80,R81,R82,R83,R84,R85,R86,R87,R88,R89,R90,R91,R92,R93,R94,R95,R96,R97,R98, R99, R100, R101, R102, R103, R104, R105, R106, R107, R108, R109, R110, R111, R112, R113, R114, R115, R116, R117, R118, R119, R120, R121, R122, R123, R124, R125, R126, R127, R128, R129, R130, R131, R132, R133, R134, R135, R136, R137, R138, R139, R140, R141, R142, R143, R144, R145, R146, R147, R148, R149, R150, R151, R152, R153, R154, R155, R156, R157, R158, R159, R160, R161, R162, R163, R164, R165, R166, R167, R168, R169, R170, R171, R172, R173, R174, R175, R176, R177, R178, R179, R180, R181, R182, R183, R184, R185, R186, R187, R188, R189, R190, R191, R192, R193, R194, R195, R196, R197, R198, R199, R200, R201, R202, R203, R204, R205, R206, R207, R208, R209, R210, R211, R212, R213, R214, R215, R216, R217, R218, R219, R220, R221, R222, R223, R224, R225, R226, R227, R228, R229, R230, R231, R232, R233, R234, R235, R236, R237, R238, R239, R240, R241, R242, R243, R244, R245, R246, R247, R248, R249, R250, R251, R252, R253, R254, R255, R256, R257, R258, R259, R260, R261, R262, R263, R264, R265, R266, R267, R268, R269, R270, R271, R272, R273, R274, R275, R276, R277, R278, R279, R280, R281, R282, R283, R284, R285, R286, R287, R288] #,R289]

    return RA, R1
