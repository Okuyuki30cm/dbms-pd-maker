# coding utf-8
import json
import csv
import re


DAM_DATA = './dam.csv'
SIRE_DATA = './sire.csv'


def load_csv_as_json(sire_data_as_csv,dam_data_as_csv):
    json_data = {}
    json_list = []
    with open(sire_data_as_csv,'r',encoding='utf-8') as f:
        for line in csv.DictReader(f):
            json_list.append(line)
        json_data['colt_data'] = json_list
    json_list = []
    with open(dam_data_as_csv, 'r',encoding='utf-8') as f:
        for line in csv.DictReader(f):
            json_list.append(line)
        json_data['filly_data'] = json_list
    return json_data

def pedigree_gen(data_as_csv):
    js = []
    for pedigree in data_as_csv:
        t = re.split(r'[,\n]',pedigree)
        ffff = {"name": t[6], "sire": {"name": t[7]}, "dam": {"name": t[8]}}
        fffm = {"name": t[9], "sire": {"name": t[10]}, "dam": {"name": t[11]}}
        ffmf = {"name": t[13], "sire": {"name": t[14]}, "dam": {"name": t[15]}}
        ffmm = {"name": t[16], "sire": {"name": t[17]}, "dam": {"name": t[18]}}
        fmff = {"name": t[21], "sire": {"name": t[22]}, "dam": {"name": t[23]}}
        fmfm = {"name": t[24], "sire": {"name": t[25]}, "dam": {"name": t[26]}}
        fmmf = {"name": t[28], "sire": {"name": t[29]}, "dam": {"name": t[30]}}
        fmmm = {"name": t[31], "sire": {"name": t[32]}, "dam": {"name": t[33]}}
        mfff = {"name": t[37], "sire": {"name": t[38]}, "dam": {"name": t[39]}}
        mffm = {"name": t[40], "sire": {"name": t[41]}, "dam": {"name": t[42]}}
        mfmf = {"name": t[44], "sire": {"name": t[45]}, "dam": {"name": t[46]}}
        mfmm = {"name": t[47], "sire": {"name": t[48]}, "dam": {"name": t[49]}}
        mmff = {"name": t[52], "sire": {"name": t[53]}, "dam": {"name": t[54]}}
        mmfm = {"name": t[55], "sire": {"name": t[56]}, "dam": {"name": t[57]}}
        mmmf = {"name": t[59], "sire": {"name": t[60]}, "dam": {"name": t[61]}}
        mmmm = {"name": t[62], "sire": {"name": t[63]}, "dam": {"name": t[64]}}

        fff = {"name": t[ 5], "sire": ffff, "dam": fffm}
        ffm = {"name": t[12], "sire": ffmf, "dam": ffmm}
        fmf = {"name": t[20], "sire": fmff, "dam": fmfm}
        fmm = {"name": t[27], "sire": fmmf, "dam": fmmm}
        mff = {"name": t[36], "sire": mfff, "dam": mffm}
        mfm = {"name": t[43], "sire": mfmf, "dam": mfmm}
        mmf = {"name": t[51], "sire": mmff, "dam": mmfm}
        mmm = {"name": t[58], "sire": mmmf, "dam": mmmm}

        ff = {"name": t[4], "sire": fff, "dam": ffm}
        fm = {"name": t[19], "sire": fmf, "dam": fmm}
        mf = {"name": t[35], "sire": mff, "dam": mfm}
        mm = {"name": t[50], "sire": mmf, "dam": mmm}

        f = {"name":t[3], "sire":ff, "dam":fm}
        m = {"name": t[34], "sire": mf, "dam": mm}

        js.append({"name":t[0],"sire":f,"dam":m})
    return js

def pedigree_gen2(data_as_csv):
    js = []
    for pedigree in data_as_csv:
        _t = re.split(r'[,\n]',pedigree)
        t = [""] * 63
        t[0] = _t[0]
        for i in range(1,63):
            t[i] = _t[2+i]
        data = [""]*63
        data[ 0] = t[ 0]
        data[ 1] = t[ 1]
        data[ 2] = t[32]
        data[ 3] = t[ 2]
        data[ 4] = t[17]
        data[ 5] = t[33]
        data[ 6] = t[48]
        data[ 7] = t[ 3]
        data[ 8] = t[10]
        data[ 9] = t[18]
        data[10] = t[25]
        data[11] = t[34]
        data[12] = t[41]
        data[13] = t[49]
        data[14] = t[56]
        data[15] = t[ 4]
        data[16] = t[ 7]
        data[17] = t[11]
        data[18] = t[14]
        data[19] = t[19]
        data[20] = t[22]
        data[21] = t[26]
        data[22] = t[29]
        data[23] = t[35]
        data[24] = t[38]
        data[25] = t[42]
        data[26] = t[45]
        data[27] = t[50]
        data[28] = t[53]
        data[29] = t[57]
        data[30] = t[60]
        data[31] = t[ 5]
        data[32] = t[ 6]
        data[33] = t[ 8]
        data[34] = t[ 9]
        data[35] = t[12]
        data[36] = t[13]
        data[37] = t[15]
        data[38] = t[16]
        data[39] = t[20]
        data[40] = t[21]
        data[41] = t[23]
        data[42] = t[24]
        data[43] = t[27]
        data[44] = t[28]
        data[45] = t[30]
        data[46] = t[31]
        data[47] = t[36]
        data[48] = t[37]
        data[49] = t[39]
        data[50] = t[40]
        data[51] = t[43]
        data[52] = t[44]
        data[53] = t[46]
        data[54] = t[47]
        data[55] = t[51]
        data[56] = t[52]
        data[57] = t[54]
        data[58] = t[55]
        data[59] = t[58]
        data[60] = t[59]
        data[61] = t[61]
        data[62] = t[62]
        js.append({"name": t[0], "data":data})
    return js

def trans_attrib():
    with open('./JSON用attrib自動生成.csv') as f:
        l = f.readlines()
    js = []
    for line in l:
        _t = re.split(r'[,\n]', line)
        t = _t[10:]
        data = [""]*63
        data[ 0] = t[ 0]
        data[ 1] = t[ 1]
        data[ 2] = t[32]
        data[ 3] = t[ 2]
        data[ 4] = t[17]
        data[ 5] = t[33]
        data[ 6] = t[48]
        data[ 7] = t[ 3]
        data[ 8] = t[10]
        data[ 9] = t[18]
        data[10] = t[25]
        data[11] = t[34]
        data[12] = t[41]
        data[13] = t[49]
        data[14] = t[52]
        data[15] = t[ 4]
        data[16] = t[ 7]
        data[17] = t[11]
        data[18] = t[14]
        data[19] = t[19]
        data[20] = t[22]
        data[21] = t[26]
        data[22] = t[29]
        data[23] = t[35]
        data[24] = t[38]
        data[25] = t[42]
        data[26] = t[45]
        data[27] = t[50]
        data[28] = t[53]
        data[29] = t[57]
        data[30] = t[60]
        data[31] = t[ 5]
        data[32] = t[ 6]
        data[33] = t[ 8]
        data[34] = t[ 9]
        data[35] = t[12]
        data[36] = t[13]
        data[37] = t[15]
        data[38] = t[16]
        data[39] = t[20]
        data[40] = t[21]
        data[41] = t[23]
        data[42] = t[24]
        data[43] = t[27]
        data[44] = t[28]
        data[45] = t[30]
        data[46] = t[31]
        data[47] = t[36]
        data[48] = t[37]
        data[49] = t[39]
        data[50] = t[40]
        data[51] = t[43]
        data[52] = t[44]
        data[53] = t[46]
        data[54] = t[47]
        data[55] = t[51]
        data[56] = t[52]
        data[57] = t[54]
        data[58] = t[55]
        data[59] = t[58]
        data[60] = t[59]
        data[61] = t[61]
        data[62] = t[62]

        js.append({
            "name": _t[0],
            "attrib": _t[1:10]+data
        })
    return js

if __name__ == '__main__':
    with open(SIRE_DATA, 'r') as f:
        sire_csv = f.readlines()
    with open(DAM_DATA, 'r') as f:
        dam_csv = f.readlines()
    js={}
    js['colt_data'] = pedigree_gen2(sire_csv)
    js['filly_data'] = pedigree_gen2(dam_csv)
    with open('./default_pedigree.json', 'w', encoding='utf-8') as f:
        json.dump(js,f,ensure_ascii=False,indent=3,sort_keys=True,separators=(',',':'))

    js={}
    js['all_attributes'] = trans_attrib()
    with open('./attributes.json','w',encoding='utf-8') as f:
        json.dump(js,f,ensure_ascii=False,indent=3,sort_keys=True,separators=(',',':'))

