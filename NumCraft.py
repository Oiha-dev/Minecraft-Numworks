from kandinsky import fill_rect, color, set_pixel, fill_polygon
from ion import KEY_LEFT, KEY_DOWN, KEY_UP, KEY_RIGHT, keydown


def create_map(block_map, block_mapping, map_index, x_start, y_start, renderPosition, horyzontal, left_nb):
    print(horyzontal)
    print(left_nb)
    if renderPosition == 'all':
        fill_rect(0, 0, 320, 222, (241,49,64))
        fill_rect(106, 97, 106, 2, "white")
        fill_rect(106, 97, 2, 18, "white")
        fill_rect(212, 97, 2, 18, "white")
        fill_rect(106, 113, 108, 2, "white")
    if renderPosition == 'all':
        right = 0
        left = 0
        y_range_start = 0
        y_range_end = 11
        y_range_pas = 1
        x_range_start = 0
        x_range_end = 11
        x_range_pas = 1
    if renderPosition == 'right':
        right = 1
        left = 0
        y_range_start = 0
        y_range_end = 11
        y_range_pas = 1
        x_range_start = 8 - abs(horyzontal)
        x_range_end = 11
        x_range_pas = 1
    if renderPosition == 'left':
        right = 0
        left = 1
        y_range_start = 0
        y_range_end = 11
        y_range_pas = 1
        x_range_start = 0
        x_range_end = -(9 - horyzontal)
        x_range_pas = 1
    for z in range(12):
        for y in range(y_range_start, y_range_end, y_range_pas):
            co_x = x_start + y * 16
            co_y = y_start - y * 8 + z * 16
            for x in range(x_range_start + y*right, x_range_end + y*left, x_range_pas):
                if renderPosition == 'all':
                    loading = int((z * 144 + y * 12 + x) / 1728 * 100)
                    fill_rect(110, 101, loading, 10, "white")
                co_x_apres = (co_x - x * 16)
                co_y_apres = (co_y - x * 8) * -1
                block = block_mapping.get(block_map[x + y * 12 + 144 * z])
                for cle, valeur in block_mapping.items():
                    if valeur == block:
                        key_block = cle
                if block != 'Air':
                    for i in range(len(map_index)):
                        if map_index[i][0] == (co_x_apres, co_y_apres) and map_index[i][3] < (x + y * 12 + 144 * z):
                            map_index[i][1] = key_block
                            map_index[i][2] = "B"
                            map_index[i][3] = x + y * 12 + 144 * z
                        elif map_index[i][0] == (co_x_apres+16, co_y_apres) and map_index[i][3] < (x + y * 12 + 144 * z):
                            map_index[i][1] = key_block
                            map_index[i][2] = "C"
                            map_index[i][3] = x + y * 12 + 144 * z
                        elif map_index[i][0] == (co_x_apres, co_y_apres + 8) and map_index[i][3] < (x + y * 12 + 144 * z):
                            map_index[i][1] = key_block
                            map_index[i][2] = "D"
                            map_index[i][3] = x + y * 12 + 144 * z
                        elif map_index[i][0] == (co_x_apres+16, co_y_apres+8) and map_index[i][3] < (x + y * 12 + 144 * z):
                            map_index[i][1] = key_block
                            map_index[i][2] = "E"
                            map_index[i][3] = x + y * 12 + 144 * z
                        elif map_index[i][0] == (co_x_apres, co_y_apres+16) and map_index[i][3] < (x + y * 12 + 144 * z):
                            map_index[i][1] = key_block
                            map_index[i][2] = "F"
                            map_index[i][3] = x + y * 12 + 144 * z
                        elif map_index[i][0] == (co_x_apres+16, co_y_apres+16) and map_index[i][3] < (x + y * 12 + 144 * z):
                            map_index[i][1] = key_block
                            map_index[i][2] = "G"
                            map_index[i][3] = x + y * 12 + 144 * z
                            break
    return map_index
def draw_map(map_index, block_mapping):
    for i in range(len(map_index)):
        if map_index[i][2] == 'B':
            fill_polygon([(0+map_index[i][0][0], 8+map_index[i][0][1]-1), (16+map_index[i][0][0], 0+map_index[i][0][1]-1), (16+map_index[i][0][0], 16+map_index[i][0][1]-1)], (0, 0, 0))
        elif map_index[i][2] == 'C':
            fill_polygon([(16+map_index[i][0][0], 8+map_index[i][0][1]-1), (0+map_index[i][0][0], 0+map_index[i][0][1]-1), (0+map_index[i][0][0], 16+map_index[i][0][1]-1)], (0, 0, 0))
        elif map_index[i][2] == 'D':
            fill_polygon([(16+map_index[i][0][0], 8+map_index[i][0][1]-1), (0+map_index[i][0][0], 0+map_index[i][0][1]-1), (0+map_index[i][0][0], 16+map_index[i][0][1]-1)], (0, 0, 0))
        elif map_index[i][2] == 'E':
            fill_polygon([(0+map_index[i][0][0], 8+map_index[i][0][1]-1), (16+map_index[i][0][0], 0+map_index[i][0][1]-1), (16+map_index[i][0][0], 16+map_index[i][0][1]-1)], (0, 0, 0))
        elif map_index[i][2] == 'F':
            fill_polygon([(0+map_index[i][0][0], 8+map_index[i][0][1]-1), (16+map_index[i][0][0], 0+map_index[i][0][1]-1), (16+map_index[i][0][0], 16+map_index[i][0][1]-1)], (0, 0, 0))
        elif map_index[i][2] == 'G':
            fill_polygon([(16+map_index[i][0][0], 8+map_index[i][0][1]-1), (0+map_index[i][0][0], 0+map_index[i][0][1]-1), (0+map_index[i][0][0], 16+map_index[i][0][1]-1)], (0, 0, 0))

def create_Map_index():
    index = []
    Map_y = -16
    for y in range(22):
        Map_y += 8
        Map_x = -16
        for x in range(20):
            Map_x += 16
            index.append([(Map_x, Map_y), "A", "A", 0])
    return index


grass_color = {'A': (0, 0, 0, 0), 'B': (68, 104, 58, 255), 'C': (79, 121, 68, 255), 'D': (88, 135, 76, 255), 'E': (58, 90, 49, 255), 'F': (63, 96, 52, 255), 'G': (74, 111, 63, 255), 'H': (32, 49, 28, 255), 'I': (42, 57, 38, 255), 'J': (41, 28, 17, 255), 'K': (80, 54, 37, 255), 'L': (56, 39, 25, 255), 'M': (148, 106, 73, 255), 'N': (106, 106, 106, 255), 'O': (120, 84, 56, 255), 'P': (183, 131, 91, 255), 'Q': (28, 44, 23, 255), 'R': (115, 87, 67, 255), 'S': (133, 133, 133, 255)}
grass_texture = ['AAAAAAAAAAAAAABBCCAAAAAAAAAAAAAA', 'AAAAAAAAAAAABBDDCCDDAAAAAAAAAAAA', 'AAAAAAAAAABCCDEBEBCFFCAAAAAAAAAA', 'AAAAAAAABBBCCGEGCBBCCEBCAAAAAAAA', 'AAAAAABBEBDEEBBFECBDDDCBBBAAAAAA', 'AAAACCEBBCBEEBBDDBCCCBCCCGCCAAAA', 'AABFFCBCCBBBBDBCCEEBBBBEEFBEECAA', 'BBBCCCCEEBCEEBBCCCBFFBEFFBBBBBBB', 'CECCCCCDDFCBBCCBBEEBBBCBBFFCCBDH', 'CBBBBEEBBBBBBBBBBBBCCEEBBGGBBIHH', 'BBBCCBBBBBBBBCCBBEEEEBBGGBBHHIIJ', 'KKFDDBCEEECCCEECCBBCCBEBBHIHHJHL', 'MNKCCKCBBBBBBBEBBCCCCCBHHHIIILJL', 'OOPBBKBEDCBBBBCEEDBBBBIQIHHJJLJK', 'PKPKKKKKCBCDDEDBBCBHHHIJIJHIILLK', 'OOMOOMOKECCCCECBEHHHHJHJQJJJJLLK', 'OOPMMOOKKKBOOEBBIJIJJJLJJLKKKLJK', 'OMMOOMOPPOKOOKKKHIJKKKJKKJKLLLLL', 'MMOOOMOOMOOOOMKOJLKKKKLLKKKLLKIJ', 'OOPPPKKKOKPOOOOOKJKLLLLJLLLJJKLK', 'OKMMMOPOOMMOOMOPLLLKKKLJLKKLLJKK', 'MMOMMPOMOOMOOOMMKLKKKKJLJKKLLLKK', 'MOORRMPMKPOPPOKMLLLLLJKKILLJJLKJ', 'OOPOOOMONMPMMPOOKKJKKLLKLJKKKLLL', 'AAMMMKOMOOMKKMSMLKLKKKKLLKLLLKAA', 'AAAAOOSKOKOOOMOOLLLLLKKKKKLLAAAA', 'AAAAAAOOPPPOOOPKKJKLLLLJKKAAAAAA', 'AAAAAAAAMMOOOPPPLJLKKJILAAAAAAAA', 'AAAAAAAAAAOMMOMMLKJKKLAAAAAAAAAA', 'AAAAAAAAAAAAMMMMKLKKAAAAAAAAAAAA', 'AAAAAAAAAAAAAAOKKLAAAAAAAAAAAAAA']
grass = (grass_color, grass_texture)

bedrock_color = {'A': (0, 0, 0, 0), 'B': (48, 48, 48, 255), 'C': (86, 86, 86, 255), 'D': (98, 98, 98, 255), 'E': (39, 39, 39, 255), 'F': (149, 149, 149, 255), 'G': (19, 19, 19, 255), 'H': (71, 71, 71, 255)}
bedrock_texture = ['AAAAAAAAAAAAAABBBBAAAAAAAAAAAAAA', 'AAAAAAAAAAAACCCCBBBBAAAAAAAAAAAA', 'AAAAAAAAAABBBDBBCEDBBCCAAAAAAAAA', 'AAAAAAAACEBEEBDFBCCFFFFCAAAAAAAA', 'AAAAAAFFFDBFFDBCDBCBBFBFDDAAAAAA', 'AAAAEEBFBFFCCBFCCBBCCFBBDCBBAAAA', 'AAFCCBFDDBBDDFBDDBBCCBCBBDFBBBAA', 'CCBFFBBDDFFCCDFBBDFCCCBCCBBDDDBB', 'CCBBBCCBBCFBBBBCCCCFFDBBBDDEEBBE', 'BBBBBFFEEFFFFBBBBBBCCCCCCBBCCGGG', 'DCEBBDDDDBBBBCCFFBBCCCCFFBBGGHEG', 'CCCDDCFBBBBCCCCBBBBBBFFCCHEEEGGE', 'BBBCCFFCDFBCCECBBCFDDBCEEEHGGEHG', 'BDFBBCBBFFFEEBBDDBCEEDHGHGGEEGGG', 'EEFFFBCFBDCBBBBDDDCGGEHHGEGGGGEH', 'CBBCCDBCFBFFFBBEDGEGGHGEHGGGGEHE', 'DFCBBFDBBBEDDBEBGEHGGGGGGHHEEGHE', 'BFFDDBECDCBBBDFBEGGHHEGEEEEGGEGE', 'EBBBBFFBBFCCCFBCEEEGGEEGGEGGGGEG', 'CFFFFCDDCCFCCCCEGGGEEHGEEGEEEGEE', 'FBDDDFBBCCCBBDFBGGHEEGHEEHHGGEGE', 'CFBBBCFECBBCCCCFGEGHHHEGGEGEEGHE', 'DBCBBBFFBFCEEFFCEHHGGEGGEGEEEHEG', 'CCCFFEBDDCFBBBBDHHGHHHHHGEGGGGGG', 'AABEEFDBBBBCCFDCEGEEEEHEGGEGGGAA', 'AAAADDCCBCCBBCCDGHHGGGGGGHHHAAAA', 'AAAAAABBBBEFFBBEGGGEEGEEEEAAAAAA', 'AAAAAAAADFCBBDBCEGEEEHEGAAAAAAAA', 'AAAAAAAAAAFBBCFDHHGGGEAAAAAAAAAA', 'AAAAAAAAAAAABBDDEGGGAAAAAAAAAAAA', 'AAAAAAAAAAAAAAEBEEAAAAAAAAAAAAAA']
bedrock = (bedrock_color, bedrock_texture)

dirt_color = {'A': (0, 0, 0, 0), 'B': (120, 84, 56, 255), 'C': (148, 106, 73, 255), 'D': (80, 54, 37, 255), 'E': (183, 131, 91, 255), 'F': (133, 133, 133, 255), 'G': (115, 87, 67, 255), 'H': (106, 106, 106, 255), 'I': (56, 39, 25, 255), 'J': (41, 28, 17, 255), 'K': (56, 56, 56, 255)}
dirt_texture = ['AAAAAAAAAAAAAABBCCAAAAAAAAAAAAAA', 'AAAAAAAAAAAACCDDCCBBAAAAAAAAAAAA', 'AAAAAAAAAABCCBEBCDBCCBAAAAAAAAAA', 'AAAAAAAABFBDDBGCCBBCCCBCAAAAAAAA', 'AAAAAACCEDCCCECEEEBDDBBBBCAAAAAA', 'AAAABBBEDBBBBCBBBBBCCEEBBBCCAAAA', 'AACCCBCEEBCHHDCDDCCCCFBCCBHCCEAA', 'BBCBBBBBBCEEEBBDDBBBBCBEEEEBBCBB', 'ECCCCBBDDDBBBCCCCEEDDBCCCDDDDCCD', 'BCBEEBBCCEEBBCCBBDDBBBBBBBBBBIIJ', 'ECBBBBBBBBBBBEEBBDDCCBBFFEEIIDJI', 'CBDBBECBBCBCCBBHHBBBBEBCCIJIIJDI', 'CHBEECFCBCBBBBCBBBBCCEBDIDDIIIDI', 'BBECCBBDBBEBBDCDDEBBBDDJIIIDDIJD', 'EDEDDDBBEEDBBBBDDEBIIDKIDDIKKIID', 'BBCBBCBECBCEEEBDBDDIIDIDDJIJJIID', 'BBECCBBDDDBBBDEDIIIIIJIJJIDDDIJD', 'BCCBBCBEEBBBBECBDKDDDDJDDJDIIIII', 'CCBBBCBBCBBBBCDBDIDDDDIIDDDIIDKJ', 'BBEEEDDDBDEBBBBBDJDIIIIJIIIJJDID', 'BDCCCBEBBCCBBCBEIIIDDDIJIDDIIJDD', 'CCBCCEBCBBCBBBCCDIDDDDJIJDDIIIDD', 'CBBGGCECDEBEEBDCIIIIIJDDKIIJJIDJ', 'BBEBBBCBHCECCEBBDDJDDIIDIJDDDIII', 'AACCCDBCBBCDDCFCIDIDDDDIIDIIIDAA', 'AAAABBFDBDBBBCBBIIIIIDDDDDIIAAAA', 'AAAAAABBEEEBBBEDDJDIIIIJDDAAAAAA', 'AAAAAAAACCBBBEEEIJIDDJKIAAAAAAAA', 'AAAAAAAAAABCCBCCIDJDDIAAAAAAAAAA', 'AAAAAAAAAAAACCCCDIDDAAAAAAAAAAAA', 'AAAAAAAAAAAAAABDDIAAAAAAAAAAAAAA']
dirt = (dirt_color, dirt_texture)

oak_planks_color = {'A': (0, 0, 0, 0), 'B': (157, 130, 76, 255), 'C': (102, 79, 42, 255), 'D': (192, 155, 97, 255), 'E': (173, 141, 84, 255), 'F': (182, 146, 94, 255), 'G': (125, 97, 52, 255), 'H': (148, 115, 63, 255), 'I': (71, 52, 28, 255), 'J': (85, 69, 42, 255), 'K': (75, 61, 34, 255), 'L': (51, 40, 21, 255)}
oak_planks_texture = ['AAAAAAAAAAAAAABBCCAAAAAAAAAAAAAA', 'AAAAAAAAAAAADDEEBBCCAAAAAAAAAAAA', 'AAAAAAAAAABCCCDFFBBGGCAAAAAAAAAA', 'AAAAAAAABHBFFBCGBEFEEFGHAAAAAAAA', 'AAAAAACCGFDBBEBEHDDFFBFHHHAAAAAA', 'AAAAFFEBBHGDDDBEEGCDDBBEBGCCAAAA', 'AAHCCGBFFEEGGGDBBEBCCCFBBFECCGAA', 'BBBFFCCEEFEFFFCDDBEBBBGDDFFBBBGG', 'FFDFFEEGGDDEEFFCCDDFFFBHHFFEEEII', 'FEDDDEEBBGGDDHHEEGGEEFFEECCDJJJK', 'EFEDDDDFFBBCCDDEEEEGGDDEEDJJJJKI', 'HFFHHDDFFFBEEGGDDEEEEGCFJJJJJJJL', 'FGHEEBEDFDEBBFEHHBFFFBJJJJJJJLLJ', 'EDDHHFEFFDDDDHEFFGDFJJJJJKKLLJKJ', 'BFDDDGCBBFDDDDFFFEJJJJJKKLLJJJJK', 'CBEBBDDCGBEFFDFEJJJJJKJLLJJJJJKL', 'FDGHHEEHBDCCCFFBJJJIILJIKJJLLLJI', 'DEFEEGCHFEDEECGHJLLJJJKIJLLJJJKK', 'CFFFFEDCCFEFFEBCIJKJJJJLLJJKKJJL', 'DCEBBFEDDCFEEFFFJJJJJJLJJKJJJKLJ', 'EBHHHBBBDDGGGBBEJKJLLLJJKJJLLLJJ', 'EEDDDGCBBBDDDHGBKLLJJJJKJLIKKJJK', 'CBFBBFFCEEEEEDFCLJJJJJKKLJJJJJKL', 'GGEFFBEBCGEBBBBBJJJJJKLLJJJKKKLL', 'AACCCEBBDDHGGBFHJJJIILJKKJJLLLAA', 'AAAAGGHHBFDDDCCBJLLJJJJKJLLLAAAA', 'AAAAAAHHFFFFFFDCLKJJJKKIIIAAAAAA', 'AAAAAAAAHGEBBEDDJKJJJJIIAAAAAAAA', 'AAAAAAAAAACCCBEEJJKLLLAAAAAAAAAA', 'AAAAAAAAAAAACCBBJKLLAAAAAAAAAAAA', 'AAAAAAAAAAAAAACCLLAAAAAAAAAAAAAA']
oak_planks = (oak_planks_color, oak_planks_texture)

player_color = {'A': (0, 0, 0, 0), 'B': (195, 195, 195, 255), 'C': (255, 255, 255, 255)}
player_texture = ['AAAAAAAAAAAAAABCCBAAAAAAAAAAAAAA', 'AAAAAAAAAAAABCAAAACBAAAAAAAAAAAA', 'AAAAAAAAAABCAAAAAAAACBAAAAAAAAAA', 'AAAAAAAABCAAAAAAAAAAAACBAAAAAAAA', 'AAAAAABCAAAAAAAAAAAAAAAACBAAAAAA', 'AAAABCAAAAAAAAAAAAAAAAAAAACBAAAA', 'AABCAAAAAAAAAAAAAAAAAAAAAAAACBAA', 'BCAAAAAAAAAAAAAAAAAAAAAAAAAAAACB', 'CABCAAAAAAAAAAAAAAAAAAAAAAAACBAC', 'BAAABCAAAAAAAAAAAAAAAAAAAACBAAAB', 'CAAAAABCAAAAAAAAAAAAAAAACBAAAAAC', 'BAAAAAAABCAAAAAAAAAAAACBAAAAAAAB', 'CAAAAAAAAABCAAAAAAAACBAAAAAAAAAC', 'BAAAAAAAAAAABCAAAACBAAAAAAAAAAAB', 'CAAAAAAAAAAAAABCCBAAAAAAAAAAAAAC', 'BAAAAAAAAAAAAAABBAAAAAAAAAAAAAAB', 'CAAAAAAAAAAAAAACCAAAAAAAAAAAAAAC', 'BAAAAAAAAAAAAAABBAAAAAAAAAAAAAAB', 'CAAAAAAAAAAAAAACCAAAAAAAAAAAAAAC', 'BAAAAAAAAAAAAAABBAAAAAAAAAAAAAAB', 'CAAAAAAAAAAAAAACCAAAAAAAAAAAAAAC', 'BAAAAAAAAAAAAAABBAAAAAAAAAAAAAAB', 'CAAAAAAAAAAAAAACCAAAAAAAAAAAAAAC', 'BCAAAAAAAAAAAAABBAAAAAAAAAAAAACB', 'AABCAAAAAAAAAAACCAAAAAAAAAAACBAA', 'AAAABCAAAAAAAAABBAAAAAAAAACBAAAA', 'AAAAAABCAAAAAAACCAAAAAAACBAAAAAA', 'AAAAAAAABCAAAAABBAAAAACBAAAAAAAA', 'AAAAAAAAAABCAAACCAAACBAAAAAAAAAA', 'AAAAAAAAAAAABCABBACBAAAAAAAAAAAA', 'AAAAAAAAAAAAAABCCBAAAAAAAAAAAAAA']
player = (player_color, player_texture)


Map = ''
for i in range(144):
    Map+='C'
for i in range(144):
    Map+='B'
for i in range(1440):
    Map+='A'

#the following code is just to show the cabin and the block list
Map = Map[:408]+"E"+Map[409:]
Map = Map[:409]+"B"+Map[410:]
Map = Map[:410]+"C"+Map[411:]
Map = Map[:411]+"D"+Map[412:]
Map = Map[:412]+"F"+Map[413:]
Map = Map[:325]+"F"+Map[326:]
Map = Map[:326]+"F"+Map[327:]
Map = Map[:327]+"F"+Map[328:]
Map = Map[:328]+"F"+Map[329:]
Map = Map[:329]+"F"+Map[330:]
Map = Map[:337]+"F"+Map[338:]
Map = Map[:341]+"F"+Map[342:]
Map = Map[:349]+"F"+Map[350:]
Map = Map[:361]+"F"+Map[362:]
Map = Map[:365]+"F"+Map[366:]
Map = Map[:373]+"F"+Map[374:]
Map = Map[:374]+"F"+Map[375:]
Map = Map[:375]+"F"+Map[376:]
Map = Map[:376]+"F"+Map[377:]
Map = Map[:377]+"F"+Map[378:]
Map = Map[:469]+"F"+Map[470:]
Map = Map[:470]+"F"+Map[471:]
Map = Map[:471]+"F"+Map[472:]
Map = Map[:472]+"F"+Map[473:]
Map = Map[:473]+"F"+Map[474:]
Map = Map[:481]+"F"+Map[482:]
Map = Map[:485]+"F"+Map[486:]
Map = Map[:493]+"F"+Map[494:]
Map = Map[:505]+"F"+Map[506:]
Map = Map[:509]+"F"+Map[510:]
Map = Map[:517]+"F"+Map[518:]
Map = Map[:518]+"F"+Map[519:]
Map = Map[:519]+"F"+Map[520:]
Map = Map[:520]+"F"+Map[521:]
Map = Map[:521]+"F"+Map[522:]
Map = Map[:613]+"F"+Map[614:]
Map = Map[:614]+"F"+Map[615:]
Map = Map[:615]+"F"+Map[616:]
Map = Map[:616]+"F"+Map[617:]
Map = Map[:617]+"F"+Map[618:]
Map = Map[:625]+"F"+Map[626:]
Map = Map[:626]+"F"+Map[627:]
Map = Map[:627]+"F"+Map[628:]
Map = Map[:628]+"F"+Map[629:]
Map = Map[:629]+"F"+Map[630:]
Map = Map[:637]+"F"+Map[638:]
Map = Map[:638]+"F"+Map[639:]
Map = Map[:639]+"F"+Map[640:]
Map = Map[:640]+"F"+Map[641:]
Map = Map[:641]+"F"+Map[642:]
Map = Map[:649]+"F"+Map[650:]
Map = Map[:650]+"F"+Map[651:]
Map = Map[:651]+"F"+Map[652:]
Map = Map[:652]+"F"+Map[653:]
Map = Map[:653]+"F"+Map[654:]
Map = Map[:661]+"F"+Map[662:]
Map = Map[:662]+"F"+Map[663:]
Map = Map[:663]+"F"+Map[664:]
Map = Map[:664]+"F"+Map[665:]
Map = Map[:665]+"F"+Map[666:]



Map_index = create_Map_index()
block_index = {'A': 'Air', 'B': grass, 'C': bedrock, 'D': dirt, 'E': player, 'F': oak_planks}
x_start = 128
y_start = 0
horyzontal = 0
vertical = 0
Map_index = create_map(Map, block_index, Map_index, x_start, y_start, 'all', horyzontal, vertical)
fill_rect(0, 0, 320, 222, (255, 255, 255))
draw_map(Map_index, block_index)
while True:
    if keydown(KEY_UP):
        Map_index = []
        Map_index = create_Map_index()
        y_start += 16
        Map_index = create_map(Map, block_index, Map_index, x_start, y_start, 'all', horyzontal, vertical)
        fill_rect(0, 0, 320, 222, (255, 255, 255))
        draw_map(Map_index, block_index)
    if keydown(KEY_DOWN):
        Map_index = []
        Map_index = create_Map_index()
        y_start -= 16
        Map_index = create_map(Map, block_index, Map_index, x_start, y_start, 'all', horyzontal, vertical)
        fill_rect(0, 0, 320, 222, (255, 255, 255))
        draw_map(Map_index, block_index)
    if keydown(KEY_LEFT):
        if horyzontal > -9:
            Index_del = [19, 39, 59, 79, 99, 119, 139, 159, 179, 199, 219, 239, 259, 279, 299, 319, 339, 359, 379, 399, 419, 439]
            for i in range(22):
                Map_index[i * 20][1] = 'A'
                Map_index[i * 20][2] = 'A'
                Map_index[i * 20][3] = 0
            for i in range(0, len(Map_index), 1):
                if i not in Index_del:
                    Map_index[i][1] = Map_index[i + 1][1]
                    Map_index[i][2] = Map_index[i + 1][2]
                    Map_index[i][3] = Map_index[i + 1][3]
                else:
                    Map_index[i][1] = 'A'
                    Map_index[i][2] = 'A'
                    Map_index[i][3] = 0
            x_start -= 16
            horyzontal -= 1
            Map_index = create_map(Map, block_index, Map_index, x_start, y_start, 'left', horyzontal, vertical)
            fill_rect(0, 0, 320, 222, (255, 255, 255))
            draw_map(Map_index, block_index)
    if keydown(KEY_RIGHT):
        if horyzontal < 11:
            Index_del = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280,300, 320, 340, 360, 380, 400, 420]
            for i in range(22):
                Map_index[i * 20 - 1][1] = 'A'
                Map_index[i * 20 - 1][2] = 'A'
                Map_index[i * 20 - 1][3] = 0
            for i in range(len(Map_index) - 1, -1, -1):
                if i not in Index_del:
                    Map_index[i][1] = Map_index[i - 1][1]
                    Map_index[i][2] = Map_index[i - 1][2]
                    Map_index[i][3] = Map_index[i - 1][3]
                else:
                    Map_index[i][1] = 'A'
                    Map_index[i][2] = 'A'
                    Map_index[i][3] = 0
            x_start += 16
            horyzontal += 1
            Map_index = create_map(Map, block_index, Map_index, x_start, y_start, 'right', horyzontal, vertical)
            fill_rect(0, 0, 320, 222, (255, 255, 255))
            draw_map(Map_index, block_index)
