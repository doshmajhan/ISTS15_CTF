def grid(text, cols, rows=None):
    text = "".join(text.split())
    grid = [text[n:n+cols] for n in range(0, len(text), cols)]

    # sanity check
    if rows:
        assert len(grid) == rows
    return grid


def rotate(grid, right=True):
    if right:
        new_grid = [
            "".join([row[col] for row in grid[::-1]]) for col in range(len(grid[0]))
            ]
    else:
        new_grid = [
            "".join([row[col] for row in grid]) for col in range(len(grid[0]))
        ][::-1]
    return new_grid


def decode(encoded):
    grid1 = "".join(rotate(grid(encoded, 24, 14), right=True))
    grid2 = "".join(rotate(grid(grid1, 8, 42), right=True))
    return grid2


def encode(plain):
    grid1 = "".join(rotate(grid(plain, 42, 8), right=False))
    grid2 = "".join(rotate(grid(grid1, 14, 24), right=False))
    return grid2


encoded = """ENDyaHrOHNLSRHEOCPTEOIBIDYSHNAIA
CHTNREYULDSLLSLLNOHSNOSMRWXMNE
TPRNGATIHNRARPESLNNELEBLPIIACAE
WMTWNDITEENRAHCTENEUDRETNHAEOE
TFOLSEDTIWENHAEIOYTEYQHEENCTAYCR
EIFTBRSPAMHNEWENATAMATEGYEERLB
TEEFOASFIOTUETUAEOTOARMAEERTNRTI
BSEDDNIAAHTTMSTEWPIEROAGRIEWFEB
AECTDDHILCEIHSITEGOEAOSDDRYDLORIT
RKLMLEHAGTDHARDPNEOHMGFMFEUHE
ECDMRIPFEIMEHNLSSTTRTVDOHW"""

plain = "SLOWLYDESPARATLYSLOWLYTHEREMAINSOFPASSAGEDEBRISTHATENCUMBEREDTHELOWERPArTOFTHEDOORWAYWASREMOVEDWITHTREMBLINGHANDSIMADEATINYBREACNINTHEUPPERLEFTHANDCORNERANDTHENWIDENINGTHEHOLEALITTLEIINSERTEDTHECANDLEANDPEEREDINTHEHOTAIRESCAPINGFROMTHECHAMBERCaUSEDTHEFLAMETOFLICKERBUTPRESENTLYDETAILSOFTHEROOMWITHINEMERGEDFROMTHEMISTXCANYOUSEEANyTHINGQ"


print("Decoded: " + decode(encoded))
print("Encoded: \n" + encode(plain))
print("Expected: \n" + encoded)

