# Expected ciphertext shape
# OBKR
# UOXOGHULBSOLIFBBWFLRVQQPRNGKSSO
# TWTQSJQSSEKZZWATJKLUDIAWINFBNYP
# VTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR
# 97 chars

phi = "618033988749894848204586834365638117720309179805762862135448622705260462818902449707207204189391137484754088075386891752126633862223536931793180060766726354433389086595939582905638322661319928290267880675208766892501711696207032221043216269548626296313614438149758701220340805887954454749246185695364864449241044320771344947049565846788509874339442212544877066478091588460749988712400765217057517978834166256249407589069704000281210427621771117778053153171410117046665991466979873176135600670874807101317952368942752194843530567830022878569978297783478458782289110976250030269615617002504643382437764861028383126833037242926752631165339247316711121158818638513316203840052221657912866752946549068113171599343235973494985090409476213222981017261070596116456299098162905552085247903524060201727997471753427775927786256194320827505131218156285512224809394712341451702237358057727861600868838295230459264787801788992199027077690389532196819861514378031499741106926088674296226757560523172777520353613936210767389376455606060592165894667595519004005559089502295309423124823552122124154440064703405657347976639723949499465845788730396230903750339938562102423690251386804145779956981224457471780341731264532204163972321340444494873023154176768937521030687378803441700939544096279558986787232095124268935573097045095956844017555198819218020640529055189349475926007348522821010881946445442223188913192946896220023014437702699230078030852611807545192887705021096842493627135925187607778846658361502389134933331223105339232136243192637289106705033992822652635562090297986424727597725655086154875435748264718141451270006023890162077732244994353088999095016803281121943204819643876758633147985719113978153978074761507722117508269458639320456520989698555678141069683728840587461033781054443909436835835813811311689938555769754841491445341509129540700501947754861630754226417293946803673198058618339183285991303960720144559504497792120761247856459161608370594987860069701894098864007644361709334172709191433650137157660114803814306262380514321173481510055901345610118007905063814215270930858809287570345050780814545881990633612982798141174533927312080928972792221329806429468782427487401745055406778757083237310975915117762978443284747908176518097787268416117632503861211291436834376702350371116330725869883258710336322238109809012110198991768414917512331340152733843837234500934786049792945991582201258104598230925528721241370436149102054718554961180876426576511060545881475604431784798584539731286301625448761148520217064404111660766950597757832570395110878230827106478939021115691039276838453863333215658296597731034360323225457436372041244064088826737584339536795931232213437320995749889469956564736007295999839128810319742631251797141432012311279551894778172691415891177991956481255800184550656329528598591000908621802977563789259991649946428193022293552346674759326951654214021091363018194722707890122087287361707348649998156255472811373479871656952748900814438405327483781378246691744422963491470815700735254570708977267546934382261954686153312095335792380146092735102101191902183606750973089575289577468142295433943854931553396303807291691758461014609950550648036793041472365720398600735507609023173125016132048435836481770484818109916024425232716721901893345963786087875287017393593030133590112371023917126590470263494028307668767436386513271062803231740693173344823435645318505813531085497333507599667787124490583636754132890862406324563953572125242611702780286560432349428373017255744058372782679960317393640132876277012436798311446436947670531272492410471670013824783128656506493434180390041017805339505877245866557552293915823970841772983372823115256926092995942240000560626678674357923972454084817651973436265268944888552720274778747335983536727761407591712051326934483752991649980936024617844267572776790019191907038052204612324823913261043271916845123060236278935454324617699757536890417636502547851382463146583363833760235778992672988632161858395903639981838458276449124598093704305555961"


def decode(cipher):
    msg = ""

    for digit in phi:
        msg += cipher[int(digit) % len(cipher)]
        rotated = cipher[(int(digit) % len(cipher)) + 1:] + cipher[:int(digit) % len(cipher)]
        if rotated:
            cipher = rotated
        else:
            break

    return msg


def rotate(s, amount):
    return s[amount % len(s):] + s[:amount % len(s)]

assert rotate("abcd", 1) == "bcda"
assert rotate("abcd", 2) == "cdab"
assert rotate("abcd", 6) == "cdab"


def encode(plain, index=0):
    if len(plain) == 1:
        return plain
    sol = encode(plain[1:], index + 1)
    p = int(phi[index])
    pp = int(phi[index + 1])
    to_insert = plain[0]
    thinking = to_insert + sol
    t2 = rotate(thinking, -p)
    return t2

x = "testmessage"
y = encode(x)
z = decode(y)
assert x == z


msg = "SolvethecrosswordRotateninetydegreesleftandReadshadedboxesLRTBforimgururlflagitwasphithewholetime".upper()
CIPHER_4 = encode(msg)