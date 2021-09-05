<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

    </v-row >
    <v-layout>
      <v-row>
        <v-col cols="12" sm="8" md="8" lg="8" xl="8">          
          <v-card style="width:100%" elevation=2 class="my-5">
            <v-spacer class="mx-5 py-3">
              <v-card-title style="font-size:24px;font-weight:bolder;" class="px-0" outlined>
                種牡馬血統検索
              </v-card-title>
              <v-spacer class="my-n5">
                <v-row dense>
                  <v-col cols="12">        
                    <v-autocomplete
                      :items="mySire"
                      item-text="name"
                      v-model="Sire_data"
                      v-on:change="sire_selected"
                      return-object
                    >
                  </v-autocomplete>
                  </v-col>  
                </v-row>
              </v-spacer>
              <v-checkbox class="my-n5" v-model="sire_pedigree_active" label="血統を表示" />   
              <v-expand-transition>
                <v-card v-show="sire_pedigree_active" elevation=0>
                  <table style="table-layout: fixed; width: 100%;">
                    <tbody>
                      <tr>
                        <td class="Ec">Ec</td>
                        <td class="Ph">Ph</td>
                        <td class="Ns">Ns</td>
                        <td class="Ro">Ro</td>
                        <td class="Ne">Ne</td>
                        <td class="Na">Na</td>
                        <td class="Fa">Fa</td>
                        <td class="To">To</td>
                        <td class="Te">Te</td>
                        <td class="Sw">Sw</td>
                        <td class="Ha">Ha</td>
                        <td class="Hi">Hi</td>
                        <td class="St">St</td>
                        <td class="Ma">Ma</td>
                        <td class="He">He</td>
                      </tr>
                    </tbody>
                  </table>
                  <v-spacer class="my-1"/>
                  <table>
                    <tbody>
                      <tr>
                        <td class="colt" rowspan="8" width="5%">父</td>
                        <td id="sire-name-1" colspan="4">{{Sire_data.data[1]}}</td>
                        <td id="sire-name-1-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-1-1" width="10%">{{def_attrib[Sire_pdg_attrib[1][0]]}}</td>
                        <td id="sire-attrib-1-2" width="10%">{{def_attrib[Sire_pdg_attrib[1][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="4" width="5%">父</td>
                        <td id="sire-name-3" colspan="3">{{Sire_data.data[3]}}</td>
                        <td id="sire-name-3-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-3-1">{{def_attrib[Sire_pdg_attrib[3][0]]}}</td>
                        <td id="sire-attrib-3-2">{{def_attrib[Sire_pdg_attrib[3][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="2" width="5%">父</td>
                        <td id="sire-name-7" colspan="2">{{Sire_data.data[7]}}</td>
                        <td id="sire-name-7-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-7-1">{{def_attrib[Sire_pdg_attrib[7][0]]}}</td>
                        <td id="sire-attrib-7-2">{{def_attrib[Sire_pdg_attrib[7][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" style="width:5%">父</td>
                        <td id="sire-name-15" >{{Sire_data.data[15]}}</td>
                        <td id="sire-name-15-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-15-1">{{def_attrib[Sire_pdg_attrib[15][0]]}}</td>
                        <td id="sire-attrib-15-2">{{def_attrib[Sire_pdg_attrib[15][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="sire-name-17" >{{Sire_data.data[17]}}</td>
                        <td id="sire-name-17-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-17-1">{{def_attrib[Sire_pdg_attrib[17][0]]}}</td>
                        <td id="sire-attrib-17-2">{{def_attrib[Sire_pdg_attrib[17][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="3">母</td>
                        <td class="colt" rowspan="2">父</td>
                        <td id="sire-name-9" colspan="2">{{Sire_data.data[9]}}</td>
                        <td id="sire-name-9-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-9-1">{{def_attrib[Sire_pdg_attrib[9][0]]}}</td>
                        <td id="sire-attrib-9-2">{{def_attrib[Sire_pdg_attrib[9][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" >父</td>
                        <td id="sire-name-19" >{{Sire_data.data[19]}}</td>
                        <td id="sire-name-19-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-19-1">{{def_attrib[Sire_pdg_attrib[19][0]]}}</td>
                        <td id="sire-attrib-19-2">{{def_attrib[Sire_pdg_attrib[19][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="sire-name-21" >{{Sire_data.data[21]}}</td>
                        <td id="sire-name-21-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-21-1">{{def_attrib[Sire_pdg_attrib[21][0]]}}</td>
                        <td id="sire-attrib-21-2">{{def_attrib[Sire_pdg_attrib[21][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="7">母</td>
                        <td class="colt" rowspan="4">父</td>
                        <td id="sire-name-5" colspan="3">{{Sire_data.data[5]}}</td>
                        <td id="sire-name-5-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-5-1">{{def_attrib[Sire_pdg_attrib[5][0]]}}</td>
                        <td id="sire-attrib-5-2">{{def_attrib[Sire_pdg_attrib[5][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="2">父</td>
                        <td id="sire-name-11" colspan="2">{{Sire_data.data[11]}}</td>
                        <td id="sire-name-11-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-11-1">{{def_attrib[Sire_pdg_attrib[11][0]]}}</td>
                        <td id="sire-attrib-11-2">{{def_attrib[Sire_pdg_attrib[11][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" >父</td>
                        <td id="sire-name-23" >{{Sire_data.data[23]}}</td>
                        <td id="sire-name-23-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-23-1">{{def_attrib[Sire_pdg_attrib[23][0]]}}</td>
                        <td id="sire-attrib-23-2">{{def_attrib[Sire_pdg_attrib[23][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="sire-name-25" >{{Sire_data.data[25]}}</td>
                        <td id="sire-name-25-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-25-1">{{def_attrib[Sire_pdg_attrib[25][0]]}}</td>
                        <td id="sire-attrib-25-2">{{def_attrib[Sire_pdg_attrib[25][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="3">母</td>
                        <td class="colt" rowspan="2">父</td>
                        <td id="sire-name-13" colspan="2">{{Sire_data.data[13]}}</td>
                        <td id="sire-name-13-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-13-1">{{def_attrib[Sire_pdg_attrib[13][0]]}}</td>
                        <td id="sire-attrib-13-2">{{def_attrib[Sire_pdg_attrib[13][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt">父</td>
                        <td id="sire-name-27" >{{Sire_data.data[27]}}</td>
                        <td id="sire-name-27-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-27-1">{{def_attrib[Sire_pdg_attrib[27][0]]}}</td>
                        <td id="sire-attrib-27-2">{{def_attrib[Sire_pdg_attrib[27][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="sire-name-29" >{{Sire_data.data[29]}}</td>
                        <td id="sire-name-29-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="sire-attrib-29-1">{{def_attrib[Sire_pdg_attrib[29][0]]}}</td>
                        <td id="sire-attrib-29-2">{{def_attrib[Sire_pdg_attrib[29][1]]}}</td>
                      </tr>                
                    </tbody>
                  </table>
                </v-card>
              </v-expand-transition>
            </v-spacer>
          </v-card>
          <v-spacer/>
          <v-card style="width:100%" elevation=2 class="my-5">
            <v-spacer class="mx-5 py-3">
              <v-card-title style="font-size:24px;font-weight:bolder;" class="px-0" >
                繁殖牝馬血統検索
              </v-card-title>
              <v-spacer class="my-n5">
                <v-row dense>
                  <v-col cols="12">        
                    <v-autocomplete
                      :items="myDam"
                      item-text="name"
                      v-model="Dam_data"
                      v-on:change="dam_selected"
                      return-object
                    >
                  </v-autocomplete>
                  </v-col>
                  
                </v-row>
              </v-spacer>
              <v-checkbox class="my-n5" v-model="dam_pedigree_active" label="血統を表示" /> 
              <v-expand-transition>
                <v-card v-show="dam_pedigree_active" elevation=0>
                  <table style="table-layout: fixed; width: 100%;">
                    <tbody>
                      <tr>
                        <td class="Ec">Ec</td>
                        <td class="Ph">Ph</td>
                        <td class="Ns">Ns</td>
                        <td class="Ro">Ro</td>
                        <td class="Ne">Ne</td>
                        <td class="Na">Na</td>
                        <td class="Fa">Fa</td>
                        <td class="To">To</td>
                        <td class="Te">Te</td>
                        <td class="Sw">Sw</td>
                        <td class="Ha">Ha</td>
                        <td class="Hi">Hi</td>
                        <td class="St">St</td>
                        <td class="Ma">Ma</td>
                        <td class="He">He</td>
                      </tr>
                    </tbody>
                  </table>
                  <v-spacer class="my-1"/>
                  <table>
                    <tbody>
                      <tr>
                        <td class="colt" rowspan="8" width="5%">父</td>
                        <td id="dam-name-1" colspan="4">{{Dam_data.data[1]}}</td>
                        <td id="dam-name-1-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-1-1" width="10%">{{def_attrib[Dam_pdg_attrib[1][0]]}}</td>
                        <td id="dam-attrib-1-2" width="10%">{{def_attrib[Dam_pdg_attrib[1][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="4" width="5%">父</td>
                        <td id="dam-name-3" colspan="3">{{Dam_data.data[3]}}</td>
                        <td id="dam-name-3-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-3-1">{{def_attrib[Dam_pdg_attrib[3][0]]}}</td>
                        <td id="dam-attrib-3-2">{{def_attrib[Dam_pdg_attrib[3][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="2" width="5%">父</td>
                        <td id="dam-name-7" colspan="2">{{Dam_data.data[7]}}</td>
                        <td id="dam-name-7-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-7-1">{{def_attrib[Dam_pdg_attrib[7][0]]}}</td>
                        <td id="dam-attrib-7-2">{{def_attrib[Dam_pdg_attrib[7][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" style="width:5%">父</td>
                        <td id="dam-name-15" >{{Dam_data.data[15]}}</td>
                        <td id="dam-name-15-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-15-1">{{def_attrib[Dam_pdg_attrib[15][0]]}}</td>
                        <td id="dam-attrib-15-2">{{def_attrib[Dam_pdg_attrib[15][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="dam-name-17" >{{Dam_data.data[17]}}</td>
                        <td id="dam-name-17-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-17-1">{{def_attrib[Dam_pdg_attrib[17][0]]}}</td>
                        <td id="dam-attrib-17-2">{{def_attrib[Dam_pdg_attrib[17][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="3">母</td>
                        <td class="colt" rowspan="2">父</td>
                        <td id="dam-name-9" colspan="2">{{Dam_data.data[9]}}</td>
                        <td id="dam-name-9-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-9-1">{{def_attrib[Dam_pdg_attrib[9][0]]}}</td>
                        <td id="dam-attrib-9-2">{{def_attrib[Dam_pdg_attrib[9][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" >父</td>
                        <td id="dam-name-19" >{{Dam_data.data[19]}}</td>
                        <td id="dam-name-19-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-19-1">{{def_attrib[Dam_pdg_attrib[19][0]]}}</td>
                        <td id="dam-attrib-19-2">{{def_attrib[Dam_pdg_attrib[19][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="dam-name-21" >{{Dam_data.data[21]}}</td>
                        <td id="dam-name-21-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-21-1">{{def_attrib[Dam_pdg_attrib[21][0]]}}</td>
                        <td id="dam-attrib-21-2">{{def_attrib[Dam_pdg_attrib[21][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="7">母</td>
                        <td class="colt" rowspan="4">父</td>
                        <td id="dam-name-5" colspan="3">{{Dam_data.data[5]}}</td>
                        <td id="dam-name-5-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-5-1">{{def_attrib[Dam_pdg_attrib[5][0]]}}</td>
                        <td id="dam-attrib-5-2">{{def_attrib[Dam_pdg_attrib[5][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="2">父</td>
                        <td id="dam-name-11" colspan="2">{{Dam_data.data[11]}}</td>
                        <td id="dam-name-11-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-11-1">{{def_attrib[Dam_pdg_attrib[11][0]]}}</td>
                        <td id="dam-attrib-11-2">{{def_attrib[Dam_pdg_attrib[11][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" >父</td>
                        <td id="dam-name-23" >{{Dam_data.data[23]}}</td>
                        <td id="dam-name-23-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-23-1">{{def_attrib[Dam_pdg_attrib[23][0]]}}</td>
                        <td id="dam-attrib-23-2">{{def_attrib[Dam_pdg_attrib[23][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="dam-name-25" >{{Dam_data.data[25]}}</td>
                        <td id="dam-name-25-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-25-1">{{def_attrib[Dam_pdg_attrib[25][0]]}}</td>
                        <td id="dam-attrib-25-2">{{def_attrib[Dam_pdg_attrib[25][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="3">母</td>
                        <td class="colt" rowspan="2">父</td>
                        <td id="dam-name-13" colspan="2">{{Dam_data.data[13]}}</td>
                        <td id="dam-name-13-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-13-1">{{def_attrib[Dam_pdg_attrib[13][0]]}}</td>
                        <td id="dam-attrib-13-2">{{def_attrib[Dam_pdg_attrib[13][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt">父</td>
                        <td id="dam-name-27" >{{Dam_data.data[27]}}</td>
                        <td id="dam-name-27-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-27-1">{{def_attrib[Dam_pdg_attrib[27][0]]}}</td>
                        <td id="dam-attrib-27-2">{{def_attrib[Dam_pdg_attrib[27][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="dam-name-29" >{{Dam_data.data[29]}}</td>
                        <td id="dam-name-29-g" style="border-left: hidden" width="5%">&thinsp;</td>
                        <td id="dam-attrib-29-1">{{def_attrib[Dam_pdg_attrib[29][0]]}}</td>
                        <td id="dam-attrib-29-2">{{def_attrib[Dam_pdg_attrib[29][1]]}}</td>
                      </tr>                
                    </tbody>
                  </table>

                </v-card>
              </v-expand-transition>
            </v-spacer>
          </v-card>
        </v-col>
        <v-spacer/>
        <v-col cols="12" sm="4" md="4" lg="4" xl="4">
          <v-expand-transition>
            <v-card  v-show="mating_props" elevation=2 class="my-5">
              <v-card-title style="font-size:24px;font-weight:bolder;">
                配合結果
              </v-card-title>
              完璧な配合<br>
              速13短1長2
            </v-card>
          </v-expand-transition>
        </v-col>
      </v-row>
    </v-layout>
    <v-spacer class="my-4 px-0 mx-0 my-0" />
    <v-layout >
      <v-expand-transition>
        <v-card v-show="mating_result_active" style="width:100%" elevation=5 class="py-n3 pb-n5">
          <v-spacer class="mx-5 py-3 my-1">
            <v-card-title style="font-size:24px;font-weight:bolder;" class="px-0" outlined>
              産駒登録フォーム
            </v-card-title>
            <v-spacer class="my-n6"/>
            <v-radio-group label="産駒の性別" v-model="foal_sex" mandatory row >
              <v-radio label = "牡" value="0"/>
              <v-radio label = "牝" value="1"/>
            </v-radio-group>
            <v-spacer class="my-n3"/>
            <v-text-field
              v-model="foal_name"
              label="産駒名入力"
              filled
              append-outer-icon="mdi-send"
              @click:append-outer="submit_foal"
              style="width:80%;"
            ></v-text-field>
            <v-checkbox class="my-n5" v-model="foal_pedigree_active" label="血統を表示" />         
            <v-col cols="12" sm="8" md="8" lg="8" xl="8" class="ml-n3 mb-n6">
              <v-expand-transition>
                <v-card v-show="foal_pedigree_active" elevation=0>
                  <table style="table-layout: fixed; width: 100%;">
                    <tbody>
                      <tr>
                        <td class="Ec">Ec</td>
                        <td class="Ph">Ph</td>
                        <td class="Ns">Ns</td>
                        <td class="Ro">Ro</td>
                        <td class="Ne">Ne</td>
                        <td class="Na">Na</td>
                        <td class="Fa">Fa</td>
                        <td class="To">To</td>
                        <td class="Te">Te</td>
                        <td class="Sw">Sw</td>
                        <td class="Ha">Ha</td>
                        <td class="Hi">Hi</td>
                        <td class="St">St</td>
                        <td class="Ma">Ma</td>
                        <td class="He">He</td>
                      </tr>
                    </tbody>
                  </table>
                  <v-spacer class="my-1"/> 
                    <table>
                      <tbody>
                        <tr>
                          <td class="colt" rowspan="8" width="5%">父</td>
                          <td id="foal-name-1" colspan="4">{{Sire_data.data[0]}}</td>
                          <td id="foal-name-1-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-1-1" width="10%">{{def_attrib[Sire_pdg_attrib[0][0]]}}</td>
                          <td id="foal-attrib-1-2" width="10%">{{def_attrib[Sire_pdg_attrib[0][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="colt" rowspan="4" width="5%">父</td>
                          <td id="foal-name-3" colspan="3">{{Sire_data.data[1]}}</td>
                          <td id="foal-name-3-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-3-1">{{def_attrib[Sire_pdg_attrib[1][0]]}}</td>
                          <td id="foal-attrib-3-2">{{def_attrib[Sire_pdg_attrib[1][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="colt" rowspan="2" width="5%">父</td>
                          <td id="foal-name-7" colspan="2">{{Sire_data.data[3]}}</td>
                          <td id="foal-name-7-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-7-1">{{def_attrib[Sire_pdg_attrib[3][0]]}}</td>
                          <td id="foal-attrib-7-2">{{def_attrib[Sire_pdg_attrib[3][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="colt" style="width:5%">父</td>
                          <td id="foal-name-15" >{{Sire_data.data[7]}}</td>
                          <td id="foal-name-15-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-15-1">{{def_attrib[Sire_pdg_attrib[7][0]]}}</td>
                          <td id="foal-attrib-15-2">{{def_attrib[Sire_pdg_attrib[7][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="filly">母</td>
                          <td class="colt" >父</td>
                          <td id="foal-name-17" >{{Sire_data.data[9]}}</td>
                          <td id="foal-name-17-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-17-1">{{def_attrib[Sire_pdg_attrib[9][0]]}}</td>
                          <td id="foal-attrib-17-2">{{def_attrib[Sire_pdg_attrib[9][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="filly" rowspan="3">母</td>
                          <td class="colt" rowspan="2">父</td>
                          <td id="foal-name-9" colspan="2">{{Sire_data.data[5]}}</td>
                          <td id="foal-name-9-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-9-1">{{def_attrib[Sire_pdg_attrib[5][0]]}}</td>
                          <td id="foal-attrib-9-2">{{def_attrib[Sire_pdg_attrib[5][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="colt" >父</td>
                          <td id="foal-name-19" >{{Sire_data.data[11]}}</td>
                          <td id="foal-name-19-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-19-1">{{def_attrib[Sire_pdg_attrib[11][0]]}}</td>
                          <td id="foal-attrib-19-2">{{def_attrib[Sire_pdg_attrib[11][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="filly">母</td>
                          <td class="colt" >父</td>
                          <td id="foal-name-21" >{{Sire_data.data[13]}}</td>
                          <td id="foal-name-21-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-21-1">{{def_attrib[Sire_pdg_attrib[13][0]]}}</td>
                          <td id="foal-attrib-21-2">{{def_attrib[Sire_pdg_attrib[13][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="filly" rowspan="7">母</td>
                          <td class="colt" rowspan="4">父</td>
                          <td id="foal-name-5" colspan="3">{{Dam_data.data[1]}}</td>
                          <td id="foal-name-5-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-5-1">{{def_attrib[Dam_pdg_attrib[1][0]]}}</td>
                          <td id="foal-attrib-5-2">{{def_attrib[Dam_pdg_attrib[1][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="colt" rowspan="2">父</td>
                          <td id="foal-name-11" colspan="2">{{Dam_data.data[3]}}</td>
                          <td id="foal-name-11-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-11-1">{{def_attrib[Dam_pdg_attrib[3][0]]}}</td>
                          <td id="foal-attrib-11-2">{{def_attrib[Dam_pdg_attrib[3][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="colt" >父</td>
                          <td id="foal-name-23" >{{Dam_data.data[7]}}</td>
                          <td id="foal-name-23-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-23-1">{{def_attrib[Dam_pdg_attrib[7][0]]}}</td>
                          <td id="foal-attrib-23-2">{{def_attrib[Dam_pdg_attrib[7][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="filly">母</td>
                          <td class="colt" >父</td>
                          <td id="foal-name-25" >{{Dam_data.data[9]}}</td>
                          <td id="foal-name-25-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-25-1">{{def_attrib[Dam_pdg_attrib[9][0]]}}</td>
                          <td id="foal-attrib-25-2">{{def_attrib[Dam_pdg_attrib[9][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="filly" rowspan="3">母</td>
                          <td class="colt" rowspan="2">父</td>
                          <td id="foal-name-13" colspan="2">{{Dam_data.data[5]}}</td>
                          <td id="foal-name-13-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-13-1">{{def_attrib[Dam_pdg_attrib[5][0]]}}</td>
                          <td id="foal-attrib-13-2">{{def_attrib[Dam_pdg_attrib[5][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="colt">父</td>
                          <td id="foal-name-27" >{{Dam_data.data[11]}}</td>
                          <td id="foal-name-27-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-27-1">{{def_attrib[Dam_pdg_attrib[11][0]]}}</td>
                          <td id="foal-attrib-27-2">{{def_attrib[Dam_pdg_attrib[11][1]]}}</td>
                        </tr>
                        <tr>
                          <td class="filly">母</td>
                          <td class="colt" >父</td>
                          <td id="foal-name-29" >{{Dam_data.data[13]}}</td>
                          <td id="foal-name-29-g" style="border-left: hidden" width="5%">&thinsp;</td>
                          <td id="foal-attrib-29-1">{{def_attrib[Dam_pdg_attrib[13][0]]}}</td>
                          <td id="foal-attrib-29-2">{{def_attrib[Dam_pdg_attrib[13][1]]}}</td>
                        </tr>                
                      </tbody>
                    </table>
                  <v-spacer class="pb-3"/>
                </v-card>
              </v-expand-transition>
            </v-col>
          </v-spacer>
        </v-card>
      </v-expand-transition>

    </v-layout>

  </v-container>
</template>

<script>
  import Dexie from 'dexie';

  export default {
    name: 'HelloWorld',

    data: () => ({
      dexie_db: null,
      Sire_data: {"data": Array(62)},
      mySire:[],
      Dam_data: {"data": Array(62)},
      myDam:[],
      attrib_data: [],
      Sire_pdg_attrib:Array(63).fill(["",""]),
      Dam_pdg_attrib: Array(63).fill(["",""]),
      Foal_pdg_attrib: Array(63).fill(["",""]),
      Sire_grp_attrib:Array(9).fill([""]),
      Dam_grp_attrib: Array(9).fill([""]),
      Foal_grp_attrib: Array(9).fill([""]),
      sire_pedigree_active: false,
      dam_pedigree_active: false,
      editedHorse:0,
      default_horse_name:"",
      def_attrib: ["","短","速","底","長","ダ","丈","早","晩","堅","難"],

      mating_props: false,
      mating_result_active: false,
      mating_result:{"Result": "理論なし", "インブリード": []},

      foal_name: "",
      foal_pedigree: {"name":"", "data":Array(62)},
      foal_sex:"0" ,
      foal_pedigree_active: false,

    }),
    methods:{

      gettime(){
        var now = new Date();
        var timestamp = 
          now.getFullYear() + '/' + (now.getMonth()+1) + '/' + now.getDate()
          + '  ' + ('0'+now.getHours()).slice(-2) + ':' + ('0' + now.getMinutes()).slice(-2); 
        return timestamp;
      },

      ac_selected(_pdgdata){
        //Sireの名前でattribを検索
        var sire_attrib = this.attrib_data.find((v)=> v.name===_pdgdata.name);
        const pdg_attrib = sire_attrib.attrib.slice(9).map(data=>{
          return [
            parseInt(data.substr(0, 2),16),
            parseInt(data.substr(2, 2),16)
          ]
        })
        return [
          pdg_attrib,
          sire_attrib.attrib.slice(0,9)
        ]        
      },

      sire_selected(){
        var res = this.ac_selected(this.Sire_data)
        this.Sire_pdg_attrib = res[0]
        this.Sire_grp_attrib = res[1]
        const indexes = [[1,3,7,15],[9,19],[5,11,23],[13,27],[17],[21],[25],[29]];
        const attributes = [
          "no-attributes",
          "tankyori",
          "sokuryoku",
          "sokodikara",
          "chokyori",
          "dart",
          "jobu",
          "sojuku",
          "bansei",
          "kenjitu",
          "kishonan"
        ]
        var counter = 0;
        indexes.map((data)=>{
          data.map(d_data=>{
            var item = document.getElementById('sire-name-'+d_data+'-g');
            item.className = this.Sire_grp_attrib[counter];
            item = document.getElementById('sire-attrib-'+d_data+'-1');
            item.className = attributes[this.Sire_pdg_attrib[d_data][0]];
            item = document.getElementById('sire-attrib-'+d_data+'-2');
            item.className = attributes[this.Sire_pdg_attrib[d_data][1]];
            return true;
          })
          counter = counter + 1;
        })
        this.compute_relative()
      },
      
      dam_selected(){
        var res = this.ac_selected(this.Dam_data)
        this.Dam_pdg_attrib = res[0]
        this.Dam_grp_attrib = res[1]
        const indexes = [[1,3,7,15],[9,19],[5,11,23],[13,27],[17],[21],[25],[29]];
        const attributes = [
          "no-attributes",
          "tankyori",
          "sokuryoku",
          "sokodikara",
          "chokyori",
          "dart",
          "jobu",
          "sojuku",
          "bansei",
          "kenjitu",
          "kishonan"
        ]
        
        var counter = 0;
        indexes.map((data)=>{
          data.map(d_data=>{
            
            var item = document.getElementById('dam-name-'+d_data+'-g');
            item.className = this.Dam_grp_attrib[counter];
            item = document.getElementById('dam-attrib-'+d_data+'-1');
            item.className = attributes[this.Dam_pdg_attrib[d_data][0]];
            item = document.getElementById('dam-attrib-'+d_data+'-2');
            item.className = attributes[this.Dam_pdg_attrib[d_data][1]];
            return true;
          })
          counter = counter + 1;
        })
        this.compute_relative()
      },


      submit_foal(){
        if(this.Dam_data==="" | this.Sire_data===""){
          alert("両親のいずれかが未定義です。\n父馬・母馬双方を選択してください。")
          return false
        }
        var data_string=JSON.stringify(this.mySire) + JSON.stringify(this.myDam)
        var name_list=data_string.split(/,|{|}|:|\[|\]|"/);
        name_list = Array.from(new Set(name_list))
        if (name_list.includes(this.foal_name)){
          alert(this.foal_name + " は既に別の馬で使用されています。\n別の馬名を指定してください。");
          return false;
        }else{
          this.foal_pedigree.name = this.foal_name
          this.foal_pedigree.data[0] = this.foal_name
          this.foal_pedigree.data[1] = this.Sire_data.data[0]
          this.foal_pedigree.data[3] = this.Sire_data.data[1]
          this.foal_pedigree.data[4] = this.Sire_data.data[2]
          this.foal_pedigree.data[7] = this.Sire_data.data[3]
          this.foal_pedigree.data[8] = this.Sire_data.data[4]
          this.foal_pedigree.data[9] = this.Sire_data.data[5]
          this.foal_pedigree.data[10] = this.Sire_data.data[6]
          this.foal_pedigree.data[15] = this.Sire_data.data[7]
          this.foal_pedigree.data[16] = this.Sire_data.data[8]
          this.foal_pedigree.data[17] = this.Sire_data.data[9]
          this.foal_pedigree.data[18] = this.Sire_data.data[10]
          this.foal_pedigree.data[19] = this.Sire_data.data[11]
          this.foal_pedigree.data[20] = this.Sire_data.data[12]
          this.foal_pedigree.data[21] = this.Sire_data.data[13]
          this.foal_pedigree.data[22] = this.Sire_data.data[14]
          this.foal_pedigree.data[31] = this.Sire_data.data[15]
          this.foal_pedigree.data[32] = this.Sire_data.data[16]
          this.foal_pedigree.data[33] = this.Sire_data.data[17]
          this.foal_pedigree.data[34] = this.Sire_data.data[18]
          this.foal_pedigree.data[35] = this.Sire_data.data[19]
          this.foal_pedigree.data[36] = this.Sire_data.data[20]
          this.foal_pedigree.data[37] = this.Sire_data.data[21]
          this.foal_pedigree.data[38] = this.Sire_data.data[22]
          this.foal_pedigree.data[39] = this.Sire_data.data[23]
          this.foal_pedigree.data[40] = this.Sire_data.data[24]
          this.foal_pedigree.data[41] = this.Sire_data.data[25]
          this.foal_pedigree.data[42] = this.Sire_data.data[26]
          this.foal_pedigree.data[43] = this.Sire_data.data[27]
          this.foal_pedigree.data[44] = this.Sire_data.data[28]
          this.foal_pedigree.data[45] = this.Sire_data.data[29]
          this.foal_pedigree.data[46] = this.Sire_data.data[30]

          this.foal_pedigree.data[2] = this.Dam_data.data[0]
          this.foal_pedigree.data[5] = this.Dam_data.data[1]
          this.foal_pedigree.data[6] = this.Dam_data.data[2]
          this.foal_pedigree.data[11] = this.Dam_data.data[3]
          this.foal_pedigree.data[12] = this.Dam_data.data[4]
          this.foal_pedigree.data[13] = this.Dam_data.data[5]
          this.foal_pedigree.data[14] = this.Dam_data.data[6]
          this.foal_pedigree.data[23] = this.Dam_data.data[7]
          this.foal_pedigree.data[24] = this.Dam_data.data[8]
          this.foal_pedigree.data[25] = this.Dam_data.data[9]
          this.foal_pedigree.data[26] = this.Dam_data.data[10]
          this.foal_pedigree.data[27] = this.Dam_data.data[11]
          this.foal_pedigree.data[28] = this.Dam_data.data[12]
          this.foal_pedigree.data[29] = this.Dam_data.data[13]
          this.foal_pedigree.data[30] = this.Dam_data.data[14]
          this.foal_pedigree.data[47] = this.Dam_data.data[15]
          this.foal_pedigree.data[48] = this.Dam_data.data[16]
          this.foal_pedigree.data[49] = this.Dam_data.data[17]
          this.foal_pedigree.data[50] = this.Dam_data.data[18]
          this.foal_pedigree.data[51] = this.Dam_data.data[19]
          this.foal_pedigree.data[52] = this.Dam_data.data[20]
          this.foal_pedigree.data[53] = this.Dam_data.data[21]
          this.foal_pedigree.data[54] = this.Dam_data.data[22]
          this.foal_pedigree.data[55] = this.Dam_data.data[23]
          this.foal_pedigree.data[56] = this.Dam_data.data[24]
          this.foal_pedigree.data[57] = this.Dam_data.data[25]
          this.foal_pedigree.data[58] = this.Dam_data.data[26]
          this.foal_pedigree.data[59] = this.Dam_data.data[27]
          this.foal_pedigree.data[60] = this.Dam_data.data[28]
          this.foal_pedigree.data[61] = this.Dam_data.data[29]
          this.foal_pedigree.data[62] = this.Dam_data.data[30]

          if(this.foal_sex === "0"){
            this.dexie_db.PdStore.get("sire_data")
            .then(data=>{
              if ((typeof data === "undefined")){
                return [this.foal_pedigree]
              }else{
                var tmp_append_sire_data = data.dict_content
                tmp_append_sire_data = [this.foal_pedigree].concat(tmp_append_sire_data);
                return tmp_append_sire_data;
              }
            })
            .then(data=>{
              this.dexie_db.PdStore.put({"dict_name":"sire_data","dict_content":data});
              this.mySire = this.mySire.concat([this.foal_pedigree]);
              alert(this.foal_name + " のデータ追加が正しく完了しました");
            })
            .catch(err=>{
              alert(err)
            });
          }
        }
      },

      getAllIndexes(arr, val) {
        var indexes = [], i = -1;
        while ((i = arr.indexOf(val, i+1)) != -1){
            indexes.push(i);
        }
        return indexes;
      },

      compute_inbleed(){
        var sire_inbleed = []
        var dam_inbleed = []
        this.Sire_data.data.slice(0,31).map((data,index)=>{
          const _father = this.Sire_data.data[index * 2 + 1];
          const _mother = this.Sire_data.data[index * 2 + 2];
          const _all_father_in = this.getAllIndexes(this.Dam_data.data, _father);
          const _all_mother_in = this.getAllIndexes(this.Dam_data.data, _mother);

          if (
            (_all_father_in.length === 0) |
            (_all_mother_in.length === 0)
          ){
            return [-1]
          }else{
            var inbleed_mother_side = _all_father_in.filter((item)=>{
              if(_all_mother_in.findIndex(_mdata=> _mdata===item+1) > -1){                
                var __index = parseInt((item+1)/2.0-1)
                dam_inbleed.push(__index)
                return __index
              }
            })
            if (inbleed_mother_side.length > 0){
              sire_inbleed.push(index)
            }
            return true
          }
        });
        var _sire_inbleed = sire_inbleed.filter(data=>{
          var child_index = (data%2===1)? parseInt((data-1)/2.0) : parseInt((data-2)/2.0)
          return !sire_inbleed.includes(child_index)
        })

        
        var _dam_inbleed = dam_inbleed.filter(data=>{
          var child_index = (data%2===1)? parseInt((data-1)/2.0) : parseInt((data-2)/2.0)
          return !dam_inbleed.includes(child_index)
        })
        sire_inbleed = Array.from(new Set(_sire_inbleed))
        dam_inbleed = Array.from(new Set(_dam_inbleed))
        return [sire_inbleed,dam_inbleed]
      },

      compute_relative(){
        if((typeof this.Dam_data.data[0]==='undefined') | (typeof this.Sire_data.data[0]==='undefined')){
          return false
        }else{
          
          this.mating_result_active = true;
          this.mating_props = true;

          //まずは血統関連の処理から
          this.Foal_grp_attrib[0] = this.Sire_grp_attrib[0]
          this.Foal_grp_attrib[1] = this.Sire_grp_attrib[2]
          this.Foal_grp_attrib[2] = this.Dam_grp_attrib[0]
          this.Foal_grp_attrib[3] = this.Dam_grp_attrib[2]
          this.Foal_grp_attrib[4] = this.Sire_grp_attrib[1]
          this.Foal_grp_attrib[5] = this.Sire_grp_attrib[3]
          this.Foal_grp_attrib[6] = this.Dam_grp_attrib[1]
          this.Foal_grp_attrib[7] = this.Dam_grp_attrib[3]
          this.Foal_grp_attrib[8] = this.Sire_grp_attrib[8]
          
          const id_index = [[1,3,7,15],[9,19],[5,11,23],[13,27],[17],[21],[25],[29]]
          const _index_to_foal = [0,1,3,7,5,11,-1,-3,-7,-5,-11,9,13,-9,-13]
          const attributes = [
            "no-attributes",
            "tankyori",
            "sokuryoku",
            "sokodikara",
            "chokyori",
            "dart",
            "jobu",
            "sojuku",
            "bansei",
            "kenjitu",
            "kishonan"
          ]
          var counter = 0;
          var counter_b= 0;
          id_index.map((data)=>{
            data.map(d_data=>{
              var item = document.getElementById('foal-name-'+d_data+'-g');
              item.className = this.Dam_grp_attrib[counter];
              if(_index_to_foal[counter_b] >= 0){
                item = document.getElementById('foal-attrib-'+d_data+'-1');
                item.className = attributes[this.Sire_pdg_attrib[_index_to_foal[counter_b]][0]];
                item = document.getElementById('foal-attrib-'+d_data+'-2');
                item.className = attributes[this.Sire_pdg_attrib[_index_to_foal[counter_b]][1]];
              }else{
                item = document.getElementById('foal-attrib-'+d_data+'-1');
                item.className = attributes[this.Dam_pdg_attrib[-_index_to_foal[counter_b]][0]];
                item = document.getElementById('foal-attrib-'+d_data+'-2');
                item.className = attributes[this.Dam_pdg_attrib[-_index_to_foal[counter_b]][1]];                
              }
              counter_b = counter_b + 1;
              return true;
            })
            counter = counter + 1;
          })

          //ここではまだ，foalのpdg_attribは変えない

          //インブリードの評価
          //リフレッシュ
          id_index.flat().map((data)=>{
            var _item = document.getElementById('sire-name-'+data);
            _item.className = "outbleed";
            _item = document.getElementById('dam-name-'+data);
            _item.className = "outbleed";
            _item = document.getElementById('foal-name-'+data);
            _item.className = "outbleed";
          })
          var res = this.compute_inbleed()
          res[0].map(data=>{
            var _item = document.getElementById('sire-name-'+data);
            if(_item != null){
              _item.className = "inbleed";
            }
            var _index = _index_to_foal.findIndex(elm=>elm===data);
            _item = document.getElementById('foal-name-'+id_index.flat()[_index]);
            if(_item != null){
              _item.className = "inbleed";
            }
          })
          res[1].map(data=>{
            var _item = document.getElementById('dam-name-'+data);
            if(_item != null){
              _item.className = "inbleed";
            }
            var _index = _index_to_foal.findIndex(elm=>elm===-data);
            _item = document.getElementById('foal-name-'+id_index.flat()[_index]);
            if(_item != null){
              _item.className = "inbleed";
            }
          })
        }
      },

      erase(){
        this.dexie_db.MsgDB.clear();
        this.dbinitializer();
      },

      dbinitializer(){
        this.dexie_db = new Dexie('DB-PD-MAKER');
        this.dexie_db.version(1).stores({
          PdStore: 'dict_name,dict_content'
        });
        fetch('./json/default_pedigree.json')
          .then(response => {
            return response.json();
          })
          .then(json => {
            this.mySire = json.colt_data
            this.myDam = json.filly_data
          })
        fetch('./json/attributes.json')
          .then(response => {
            return response.json();
          })
          .then(json => {
            this.attrib_data = json.all_attributes
          })
        this.dexie_db.PdStore.get("sire_data")
          .then(data=>{
            var append_mySire=data.dict_content;
            this.mySire = this.mySire.concat(append_mySire);
            this.mySire = this.mySire.filter((item,index,self)=>{
              const nameList = self.map(item=>item['name']);
              if(nameList.indexOf(item.name) === index){
                if (item.name){
                  return item;
                }
              }
            });
          });
        this.dexie_db.PdStore.get("dam_data")
          .then(data=>{
            var append_myDam=data.dict_content;
            this.myDam = this.myDam.concat(append_myDam);
            this.myDam = this.myDam.filter((item,index,self)=>{
              const nameList = self.map(item=>item['name']);
              if(nameList.indexOf(item.name) === index){
                if (item.name){
                  return item;
                }
              }
            });
          });
        this.dexie_db.PdStore.get("attrib_data")
          .then(data=>{
            var append_myAttr=data.dict_content;
            this.attrib_data = this.attrib_data.concat(append_myAttr);
            this.attrib_data = this.attrib_data.filter((item,index,self)=>{
              const nameList = self.map(item=>item['name']);
              if(nameList.indexOf(item.name) === index){
                if (item.name){
                  return item;
                }
              }
            });
          });
      },

    },    
    mounted(){
        this.dbinitializer();
    },

  }
</script>

<style scoped>
th,td{
  border: solid 1px;
  padding: 3px;
  padding-left: 10px;
  font-size: 10px;
  height: 25px;
  font-weight: bold;
}
table {
  width: 100%;
  border-collapse: collapse;
}
.colt{
  border: solid;
  background-color: #B4C6E7;
  font-weight: bold;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.filly{
  border: solid;
  background-color: #e9b380;
  font-weight: bold;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.no-attributes{
  border: solid;
  background-color: #FFFFFF;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.tankyori{
  border: solid;
  background-color: #FAFF4D;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.sokuryoku{
  border: solid;
  background-color: #FFFAB4;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.sokodikara{
  border: solid;
  background-color: #F4781A;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.chokyori{
  border: solid;
  background-color: #06F0FB;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.dart{
  border: solid;
  background-color: #FDDBA5;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.jobu{
  border: solid;
  background-color: #FDABDC;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.sojuku{
  border: solid;
  background-color: #3DAC3F;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.bansei{
  border: solid;
  background-color: #A5E319;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.kishonan{
  border: solid black;
  background-color: #FA06FA;
  font-weight: bold;  
  color:white;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.kenjitu{
  border: solid;
  background-color: #999999;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.Ec{
  background-color: white;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.Ph{
  background-color: lightsteelblue;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.Ns{
  background-color: mediumaquamarine;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.Ro{
  background-color: lightpink;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.Ne{
  background-color: yellow;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.Na{
  background-color: lightskyblue;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.Fa{
  background-color: khaki;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.To{
  background-color: orange;
  border-color: black;
  text-align: center;
  color: white;
  padding: 0px;
  padding-left: 0px;
}
.Te{
  background-color: purple;
  border-color: black;
  text-align: center;
  color: white;
  padding: 0px;
  padding-left: 0px;
}
.Sw{
  background-color: peachpuff;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.Ha{
  background-color: chartreuse;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.Hi{
  background-color: mediumblue;
  text-align: center;
  color: white;
  border-color: black;
  padding: 0px;
  padding-left: 0px;
}
.St{
  background-color: slateblue;
  text-align: center;
  color: white;
  border-color:  black;
  padding: 0px;
  padding-left: 0px;
}
.Ma{
  background-color: darkorchid;
  text-align: center;
  border-color:  black;
  color: white;
  padding: 0px;
  padding-left: 0px;
}
.He{
  background-color: aqua;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
}
.inbleed{
  color: red;
  font-weight: bolder;
  border: black;
}
.outbleed{
  color: black;
  font-weight: normal;
  text-shadow: 0px 0px 0px;
}

</style>