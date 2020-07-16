"""
RGB values of each atom. 
Colors -> [color, atomic number, van der Waals raddi (angstroms)]
https://doi.org/10.1023/A:1011625728803
https://doi.org/10.1021/ic501364h
"""


colors = {
    "H":  ["rgba(255, 255, 255, 1.0)",  1, 1.2],
    "He": ["rgba(255, 191, 203, 1.0)",  2, 1.4],
    "Li": ["rgba(178, 034, 033, 1.0)",  3, 2.2],
    "Be": ["rgba(255, 019, 147, 1.0)",  4, 1.9],
    "B":  ["rgba(000, 251, 002, 1.0)",  5, 1.8 ],
    "C":  ["rgba(198, 198, 198, 1.0)",  6, 1.7],
    "N":  ["rgba(140, 142, 251, 1.0)",  7, 1.6],
    "O":  ["rgba(236, 000, 000, 1.0)",  8, 1.55],
    "F":  ["rgba(217, 164, 032, 1.0)",  9, 1.5],
    "Ne": ["rgba(253, 020, 146, 1.0)", 10, 1.58],
    "Na": ["rgba(000, 000, 253, 1.0)", 11, 2.4],
    "Mg": ["rgba(030, 124, 030, 1.0)", 12, 2.2],
    "Al": ["rgba(128, 128, 144, 1.0)", 13, 2.1],
    "Si": ["rgba(211, 159, 031, 1.0)", 14, 2.1],
    "P":  ["rgba(241, 156, 000, 1.0)", 15, 1.95],
    "S":  ["rgba(250, 196, 049, 1.0)", 16, 1.8],
    "Cl": ["rgba(000, 241, 000, 1.0)", 17, 1.8],
    "Ar": ["rgba(251, 020, 145, 1.0)", 18, 1.94],  
    "K":  ["rgba(143, 64, 212, 1.0)", 19, 2.8],
    "Ca": ["rgba(61, 255, 0, 1.0)", 20, 2.4],
    "Sc": ["rgba(230, 230, 230, 1.0)", 21, 2.3 ],
    "Ti": ["rgba(191, 194, 199, 1.0)", 22, 2.15 ],
    "V":  ["rgba(166, 166, 171, 1.0)", 23,  2.05],
    "Cr": ["rgba(138, 153, 199, 1.0)", 24,  2.05],
    "Mn": ["rgba(156, 122, 199, 1.0)", 25,  2.05],
    "Fe": ["rgba(224, 102, 51, 1.0)", 26,  2.05],
    "Co": ["rgba(240, 144, 160, 1.0)", 27,  2.0],
    "Ni": ["rgba(80, 208, 80, 1.0)", 28,  2.0],
    "Cu": ["rgba(200, 128, 51, 1.0)", 29,  2.0],
    "Zn": ["rgba(125, 128, 176, 1.0)", 30,  2.1],
    "Ga": ["rgba(194, 143, 143, 1.0)", 31,  2.1],
    "Ge": ["rgba(102, 143, 143, 1.0)", 32,  2.1],
    "As": ["rgba(189, 128, 227, 1.0)", 33,  2.1],
    "Se": ["rgba(255, 161, 0, 1.0)", 34,  2.1],
    "Br": ["rgba(166, 41, 41, 1.0)", 35,  2.05],
    "Kr": ["rgba(92, 184, 209, 1.0)", 36,  2.07],
    "Rb": ["rgba(112, 46, 176, 1.0)", 37,  2.9],
    "Sr": ["rgba(255, 191, 203, 1.0)", 38,  2.55],
    "Y": ["rgba(0, 255, 0, 1.0)", 39,  2.4],
    "Zr": ["rgba(148, 255, 255, 1.0)", 40, 2.3 ],
    "Nb": ["rgba(  115, 194, 201, 1.0)", 41,  2.15],
    "Mo": ["rgba(84, 181, 181, 1.0)", 42,  2.1],
    "Tc": ["rgba(59, 158, 158, 1.0)", 43,  2.05],
    "Ru": ["rgba(36, 143, 143, 1.0)", 44,  2.05],
    "Rh": ["rgba(10, 125, 140, 1.0)", 45,  2.0],
    "Pd": ["rgba(0, 105, 133, 1.0)", 46,  2.05],
    "Ag": ["rgba(192, 192, 192, 1.0)", 47,  2.1],
    "Cd": ["rgba(255, 217, 143, 1.0)", 48,  2.2],
    "In": ["rgba(166, 117, 115, 1.0)", 49,  2.2],
    "Sn": ["rgba(102, 128, 128, 1.0)", 50,  2.2],
    "Sb": ["rgba(158, 99, 181, 1.0)", 51,  2.2],
    "Te": ["rgba(211, 122, 0, 1.0)", 52,  2.1],
    "I": ["rgba(148, 0, 148, 1.0)", 53,  2.1],
    "Xe": ["rgba(66, 158, 176, 1.0)", 54, 2.28 ],
    "Cs" : ["rgba()", 55,  3.0],
    "Ba" : ["rgba()", 56,  2.7],
    "La" : ["rgba()", 57,  2.5],
    "Ce" : ["rgba()", 58,  ],
    "Pr" : ["rgba()", 59,  ],
    "Nd" : ["rgba()", 60,  ],
    "Pm" : ["rgba()", 61,  ],
    "Sm" : ["rgba()", 62,  ],
    "Eu" : ["rgba()", 63,  ],
    "Gd" : ["rgba()", 64,  ],
    "Tb" : ["rgba()", 65,  ],
    "Dy" : ["rgba()", 66,  ],
    "Ho" : ["rgba()", 67,  ],
    "Er" : ["rgba()", 68,  ],
    "Tm" : ["rgba()", 69,  ],
    "Yb" : ["rgba()", 70,  ],
    "Lu" : ["rgba()", 71,  ],
    "Hf" : ["rgba()", 72,  2.25],
    "Ta" : ["rgba()", 73,  2.2],
    "W" : ["rgba()", 74,  2.1],
    "Re" : ["rgba()", 75,  2.05],
    "Os" : ["rgba()", 76,  2.0],
    "Ir" : ["rgba()", 77,  2.0],
    "Pt" : ["rgba()", 78,  2.05],
    "Au" : ["rgba()", 79,  2.1],
    "Hg" : ["rgba()", 80,  2.05],
    "Tl" : ["rgba()", 81,  2.2],
    "Pb" : ["rgba()", 82,  2.3],
    "Bi" : ["rgba()", 83,  2.3],
    "Po" : ["rgba()", 84,  ],
    "At" : ["rgba()", 85,  ],
    "Rn" : ["rgba()", 86,  2.40],
    "Fr" : ["rgba()", 87,  ],
    "Ra" : ["rgba()", 88,  ],
    "Ac" : ["rgba()", 89,  ],
    "Th" : ["rgba()", 90,  ],
    "Pa" : ["rgba()", 91,  ],
    "U" : ["rgba()", 92,  ],
    "Np" : ["rgba()", 93,  ],
    "Pu" : ["rgba()", 94,  ],
    "Am" : ["rgba()", 95,  ],
    "Cm" : ["rgba()", 96,  ],
    "Bk" : ["rgba()", 97,  ],
    "Cf" : ["rgba()", 98,  ],
    "Es" : ["rgba()", 99,  ],
    "Fm" : ["rgba()", 100,  ],
    "Md" : ["rgba()", 101,  ],
    "No" : ["rgba()", 102,  ],
    "Lr" : ["rgba()", 103,  ],
    "Rf" : ["rgba()", 104,  ],
    "Db" : ["rgba()", 105,  ],
    "Sg" : ["rgba()", 106,  ],
    "Bh" : ["rgba()", 107,  ],
    "Hs" : ["rgba()", 108,  ],
    "Mt" : ["rgba()", 109,  ],
}
