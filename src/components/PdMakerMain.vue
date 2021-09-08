<template>
  <v-container>
    <v-layout >
      <v-row class="mx-5" align-content="center">
        <v-col cols="12" sm="12" md="6" lg="6" xl="6">
          <v-card style="width:100%" elevation=2 class="my-5">
            <v-spacer class="mx-5 py-3">
              <v-card-title style="font-size:24px;font-weight:bolder;" class="px-0" outlined>
                種牡馬検索
              </v-card-title>
              <v-spacer class="my-n5">
                <v-row dense>
                  <v-col cols="12" class="pb-2">        
                    <v-autocomplete
                      v-on:change="sire_selected"
                      :items="mySire"
                      item-text="name"
                      v-model="Sire_data"
                      hint="自家製は名前の頭に ★ を付けています"
                      persistent-hint
                      return-object
                    >
                  </v-autocomplete>
                  </v-col>  
                </v-row>
              </v-spacer>
              <v-spacer class="my-0"/>
              <v-row>
                <v-col cols="6" sm="6" md="6" lg="6" xl="6">
                  <v-card elevation="0"> 
                    <table style="table-layout: fixed; width: 100%;border-collapse:collapse;">
                      <tbody>
                        <tr>
                          <td style="border:hidden; border-bottom:1px; text-align:center; font-weight:bold" colspan="2">面白血統</td>
                        </tr>
                        <tr>
                          <td id="sire_group_1" class="UndefinedGr" width="20%">{{Sire_grp_attrib[0]}}</td>
                          <td id="sire_group_5" class="UndefinedGr" width="20%">{{Sire_grp_attrib[2]}}</td>
                        </tr>
                        <tr>
                          <td id="sire_group_9" class="UndefinedGr" width="20%">{{Sire_grp_attrib[1]}}</td>
                          <td id="sire_group_13" class="UndefinedGr" width="20%">{{Sire_grp_attrib[3]}}</td>
                        </tr>
                      </tbody>
                    </table>
                  </v-card>
                </v-col>
                <v-col cols="6" sm="6" md="6" lg="6" xl="6">
                  <v-card elevation="0"> 
                    <table style="table-layout: fixed; width: 100%; border-collapse:collapse;">
                      <tbody>
                        <tr>
                          <td style="border:hidden; border-bottom:1px; text-align:center; font-weight:bold" colspan="2">見事血統</td>
                        </tr>
                        <tr>
                          <td id="sire_group_17" class="UndefinedGr" width="20%">{{Sire_grp_attrib[4]}}</td>
                          <td id="sire_group_25" class="UndefinedGr" width="20%">{{Sire_grp_attrib[6]}}</td>
                        </tr>
                        <tr>
                          <td id="sire_group_21" class="UndefinedGr" width="20%">{{Sire_grp_attrib[5]}}</td>
                          <td id="sire_group_29" class="UndefinedGr" width="20%">{{Sire_grp_attrib[7]}}</td>
                        </tr>
                      </tbody>
                    </table>
                  </v-card>
                </v-col>
              </v-row>
              <v-checkbox  v-model="sire_pedigree_active" label="血統を表示" />   
              <v-expand-transition>
                <v-card v-show="sire_pedigree_active" elevation=0>
                  <v-spacer class="my-n4"/>
                  <table>
                    <tbody>
                      <tr>
                        <td class="colt" rowspan="8" width="5%">父</td>
                        <td id="sire-name-1" colspan="4">{{Sire_data.data[1]}}</td>
                        <td id="sire-attrib-1-1" width="10%">{{def_attrib[Sire_pdg_attrib[1][0]]}}</td>
                        <td id="sire-attrib-1-2" width="10%">{{def_attrib[Sire_pdg_attrib[1][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="4" width="5%">父</td>
                        <td id="sire-name-3" colspan="3">{{Sire_data.data[3]}}</td>
                        <td id="sire-attrib-3-1">{{def_attrib[Sire_pdg_attrib[3][0]]}}</td>
                        <td id="sire-attrib-3-2">{{def_attrib[Sire_pdg_attrib[3][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="2" width="5%">父</td>
                        <td id="sire-name-7" colspan="2">{{Sire_data.data[7]}}</td>
                        <td id="sire-attrib-7-1">{{def_attrib[Sire_pdg_attrib[7][0]]}}</td>
                        <td id="sire-attrib-7-2">{{def_attrib[Sire_pdg_attrib[7][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" style="width:5%">父</td>
                        <td id="sire-name-15" >{{Sire_data.data[15]}}</td>
                        <td id="sire-attrib-15-1">{{def_attrib[Sire_pdg_attrib[15][0]]}}</td>
                        <td id="sire-attrib-15-2">{{def_attrib[Sire_pdg_attrib[15][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="sire-name-17" >{{Sire_data.data[17]}}</td>
                        <td id="sire-attrib-17-1">{{def_attrib[Sire_pdg_attrib[17][0]]}}</td>
                        <td id="sire-attrib-17-2">{{def_attrib[Sire_pdg_attrib[17][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="3">母</td>
                        <td class="colt" rowspan="2">父</td>
                        <td id="sire-name-9" colspan="2">{{Sire_data.data[9]}}</td>
                        <td id="sire-attrib-9-1">{{def_attrib[Sire_pdg_attrib[9][0]]}}</td>
                        <td id="sire-attrib-9-2">{{def_attrib[Sire_pdg_attrib[9][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" >父</td>
                        <td id="sire-name-19" >{{Sire_data.data[19]}}</td>
                        <td id="sire-attrib-19-1">{{def_attrib[Sire_pdg_attrib[19][0]]}}</td>
                        <td id="sire-attrib-19-2">{{def_attrib[Sire_pdg_attrib[19][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="sire-name-21" >{{Sire_data.data[21]}}</td>
                        <td id="sire-attrib-21-1">{{def_attrib[Sire_pdg_attrib[21][0]]}}</td>
                        <td id="sire-attrib-21-2">{{def_attrib[Sire_pdg_attrib[21][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="7">母</td>
                        <td class="colt" rowspan="4">父</td>
                        <td id="sire-name-5" colspan="3">{{Sire_data.data[5]}}</td>
                        <td id="sire-attrib-5-1">{{def_attrib[Sire_pdg_attrib[5][0]]}}</td>
                        <td id="sire-attrib-5-2">{{def_attrib[Sire_pdg_attrib[5][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="2">父</td>
                        <td id="sire-name-11" colspan="2">{{Sire_data.data[11]}}</td>
                        <td id="sire-attrib-11-1">{{def_attrib[Sire_pdg_attrib[11][0]]}}</td>
                        <td id="sire-attrib-11-2">{{def_attrib[Sire_pdg_attrib[11][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" >父</td>
                        <td id="sire-name-23" >{{Sire_data.data[23]}}</td>
                        <td id="sire-attrib-23-1">{{def_attrib[Sire_pdg_attrib[23][0]]}}</td>
                        <td id="sire-attrib-23-2">{{def_attrib[Sire_pdg_attrib[23][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="sire-name-25" >{{Sire_data.data[25]}}</td>
                        <td id="sire-attrib-25-1">{{def_attrib[Sire_pdg_attrib[25][0]]}}</td>
                        <td id="sire-attrib-25-2">{{def_attrib[Sire_pdg_attrib[25][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="3">母</td>
                        <td class="colt" rowspan="2">父</td>
                        <td id="sire-name-13" colspan="2">{{Sire_data.data[13]}}</td>
                        <td id="sire-attrib-13-1">{{def_attrib[Sire_pdg_attrib[13][0]]}}</td>
                        <td id="sire-attrib-13-2">{{def_attrib[Sire_pdg_attrib[13][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt">父</td>
                        <td id="sire-name-27" >{{Sire_data.data[27]}}</td>
                        <td id="sire-attrib-27-1">{{def_attrib[Sire_pdg_attrib[27][0]]}}</td>
                        <td id="sire-attrib-27-2">{{def_attrib[Sire_pdg_attrib[27][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="sire-name-29" >{{Sire_data.data[29]}}</td>
                        <td id="sire-attrib-29-1">{{def_attrib[Sire_pdg_attrib[29][0]]}}</td>
                        <td id="sire-attrib-29-2">{{def_attrib[Sire_pdg_attrib[29][1]]}}</td>
                      </tr>                
                    </tbody>
                  </table>
                </v-card>
              </v-expand-transition>
            </v-spacer>
          </v-card>
        </v-col>
        <v-col cols="12" sm="12" md="6" lg="6" xl="6">
          <v-card style="width:100%" elevation=2 class="my-5">
            <v-spacer class="mx-5 py-3">
              <v-card-title style="font-size:24px;font-weight:bolder;" class="px-0" outlined>
                繁殖牝馬検索
              </v-card-title>
              <v-spacer class="my-n5">
                <v-row dense>
                  <v-col cols="12" class="pb-2">        
                    <v-autocomplete
                      :items="myDam"
                      item-text="name"
                      v-model="Dam_data"
                      hint="自家製は名前の頭に ★ を付けています"
                      persistent-hint
                      return-object
                      v-on:change="dam_selected"

                    >
                  </v-autocomplete>
                  </v-col>  
                </v-row>
              </v-spacer>
              <v-spacer class="my-0"/>
              <v-row>
                <v-col cols="6" sm="6" md="6" lg="6" xl="6">
                  <v-card elevation="0"> 
                    <table style="table-layout: fixed; width: 100%;border-collapse:collapse;">
                      <tbody>
                        <tr>
                          <td style="border:hidden; border-bottom:1px; text-align:center; font-weight:bold" colspan="2">面白血統</td>
                        </tr>
                        <tr>
                          <td id="dam_group_1" class="UndefinedGr" width="20%">{{Dam_grp_attrib[0]}}</td>
                          <td id="dam_group_5" class="UndefinedGr" width="20%">{{Dam_grp_attrib[2]}}</td>
                        </tr>
                        <tr>
                          <td id="dam_group_9" class="UndefinedGr" width="20%">{{Dam_grp_attrib[1]}}</td>
                          <td id="dam_group_13" class="UndefinedGr" width="20%">{{Dam_grp_attrib[3]}}</td>
                        </tr>
                      </tbody>
                    </table>
                  </v-card>
                </v-col>
                <v-col cols="6" sm="6" md="6" lg="6" xl="6">
                  <v-card elevation="0"> 
                    <table style="table-layout: fixed; width: 100%; border-collapse:collapse;">
                      <tbody>
                        <tr>
                          <td style="border:hidden; border-bottom:1px; text-align:center; font-weight:bold" colspan="2">見事血統</td>
                        </tr>
                        <tr>
                          <td id="dam_group_17" class="UndefinedGr" width="20%">{{Dam_grp_attrib[4]}}</td>
                          <td id="dam_group_25" class="UndefinedGr" width="20%">{{Dam_grp_attrib[6]}}</td>
                        </tr>
                        <tr>
                          <td id="dam_group_21" class="UndefinedGr" width="20%">{{Dam_grp_attrib[5]}}</td>
                          <td id="dam_group_29" class="UndefinedGr" width="20%">{{Dam_grp_attrib[7]}}</td>
                        </tr>
                      </tbody>
                    </table>
                  </v-card>
                </v-col>
              </v-row>
              <v-checkbox  v-model="dam_pedigree_active" label="血統を表示" />   
              <v-expand-transition>
                <v-card v-show="dam_pedigree_active" elevation=0>
                  <v-spacer class="my-n4"/>
                  <table>
                    <tbody>
                      <tr>
                        <td class="colt" rowspan="8" width="5%">父</td>
                        <td id="dam-name-1" colspan="4">{{Dam_data.data[1]}}</td>
                        <td id="dam-attrib-1-1" width="10%">{{def_attrib[Dam_pdg_attrib[1][0]]}}</td>
                        <td id="dam-attrib-1-2" width="10%">{{def_attrib[Dam_pdg_attrib[1][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="4" width="5%">父</td>
                        <td id="dam-name-3" colspan="3">{{Dam_data.data[3]}}</td>
                        <td id="dam-attrib-3-1">{{def_attrib[Dam_pdg_attrib[3][0]]}}</td>
                        <td id="dam-attrib-3-2">{{def_attrib[Dam_pdg_attrib[3][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="2" width="5%">父</td>
                        <td id="dam-name-7" colspan="2">{{Dam_data.data[7]}}</td>
                        <td id="dam-attrib-7-1">{{def_attrib[Dam_pdg_attrib[7][0]]}}</td>
                        <td id="dam-attrib-7-2">{{def_attrib[Dam_pdg_attrib[7][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" style="width:5%">父</td>
                        <td id="dam-name-15" >{{Dam_data.data[15]}}</td>
                        <td id="dam-attrib-15-1">{{def_attrib[Dam_pdg_attrib[15][0]]}}</td>
                        <td id="dam-attrib-15-2">{{def_attrib[Dam_pdg_attrib[15][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="dam-name-17" >{{Dam_data.data[17]}}</td>
                        <td id="dam-attrib-17-1">{{def_attrib[Dam_pdg_attrib[17][0]]}}</td>
                        <td id="dam-attrib-17-2">{{def_attrib[Dam_pdg_attrib[17][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="3">母</td>
                        <td class="colt" rowspan="2">父</td>
                        <td id="dam-name-9" colspan="2">{{Dam_data.data[9]}}</td>
                        <td id="dam-attrib-9-1">{{def_attrib[Dam_pdg_attrib[9][0]]}}</td>
                        <td id="dam-attrib-9-2">{{def_attrib[Dam_pdg_attrib[9][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" >父</td>
                        <td id="dam-name-19" >{{Dam_data.data[19]}}</td>
                        <td id="dam-attrib-19-1">{{def_attrib[Dam_pdg_attrib[19][0]]}}</td>
                        <td id="dam-attrib-19-2">{{def_attrib[Dam_pdg_attrib[19][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="dam-name-21" >{{Dam_data.data[21]}}</td>
                        <td id="dam-attrib-21-1">{{def_attrib[Dam_pdg_attrib[21][0]]}}</td>
                        <td id="dam-attrib-21-2">{{def_attrib[Dam_pdg_attrib[21][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="7">母</td>
                        <td class="colt" rowspan="4">父</td>
                        <td id="dam-name-5" colspan="3">{{Dam_data.data[5]}}</td>
                        <td id="dam-attrib-5-1">{{def_attrib[Dam_pdg_attrib[5][0]]}}</td>
                        <td id="dam-attrib-5-2">{{def_attrib[Dam_pdg_attrib[5][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" rowspan="2">父</td>
                        <td id="dam-name-11" colspan="2">{{Dam_data.data[11]}}</td>
                        <td id="dam-attrib-11-1">{{def_attrib[Dam_pdg_attrib[11][0]]}}</td>
                        <td id="dam-attrib-11-2">{{def_attrib[Dam_pdg_attrib[11][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt" >父</td>
                        <td id="dam-name-23" >{{Dam_data.data[23]}}</td>
                        <td id="dam-attrib-23-1">{{def_attrib[Dam_pdg_attrib[23][0]]}}</td>
                        <td id="dam-attrib-23-2">{{def_attrib[Dam_pdg_attrib[23][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="dam-name-25" >{{Dam_data.data[25]}}</td>
                        <td id="dam-attrib-25-1">{{def_attrib[Dam_pdg_attrib[25][0]]}}</td>
                        <td id="dam-attrib-25-2">{{def_attrib[Dam_pdg_attrib[25][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly" rowspan="3">母</td>
                        <td class="colt" rowspan="2">父</td>
                        <td id="dam-name-13" colspan="2">{{Dam_data.data[13]}}</td>
                        <td id="dam-attrib-13-1">{{def_attrib[Dam_pdg_attrib[13][0]]}}</td>
                        <td id="dam-attrib-13-2">{{def_attrib[Dam_pdg_attrib[13][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="colt">父</td>
                        <td id="dam-name-27" >{{Dam_data.data[27]}}</td>
                        <td id="dam-attrib-27-1">{{def_attrib[Dam_pdg_attrib[27][0]]}}</td>
                        <td id="dam-attrib-27-2">{{def_attrib[Dam_pdg_attrib[27][1]]}}</td>
                      </tr>
                      <tr>
                        <td class="filly">母</td>
                        <td class="colt" >父</td>
                        <td id="dam-name-29" >{{Dam_data.data[29]}}</td>
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
      </v-row>
    </v-layout>
    <v-spacer class="my-10 px-0 mx-0 my-0" />
    <v-layout justify-center>
      <v-row class="mx-5">
        <v-col cols="12" sm="12" md="12" lg="6" xl="6">
          <v-expand-transition>
            <v-card v-show="mating_result_active" style="width:100%" elevation=5 class="py-n3 pb-n5">
              <v-spacer class="mx-5 py-3 my-1">
                <v-card-title style="font-size:24px;font-weight:bolder;" class="px-0" outlined>
                  {{this.Sire_data.name}} × {{this.Dam_data.name}}
                </v-card-title>
                <v-row>
                  <v-col cols="6" sm="6" md="6" lg="6" xl="3">
                    <v-card elevation="0"> 
                      <table style="table-layout: fixed; width: 100%;border-collapse:collapse;">
                        <tbody>
                          <tr>
                            <td style="border:hidden; border-bottom:1px; text-align:center; font-weight:bold" colspan="2">面白血統</td>
                          </tr>
                          <tr>
                            <td id="foal_group_1" class="UndefinedGr" width="20%">{{Sire_grp_attrib[0]}}</td>
                            <td id="foal_group_5" class="UndefinedGr" width="20%">{{Dam_grp_attrib[0]}}</td>
                          </tr>
                          <tr>
                            <td id="foal_group_9" class="UndefinedGr" width="20%">{{Sire_grp_attrib[2]}}</td>
                            <td id="foal_group_13" class="UndefinedGr" width="20%">{{Dam_grp_attrib[2]}}</td>
                          </tr>
                        </tbody>
                      </table>
                    </v-card>
                  </v-col>
                  <v-col cols="6" sm="6" md="6" lg="6" xl="3">
                    <v-card elevation="0"> 
                      <table style="table-layout: fixed; width: 100%; border-collapse:collapse;">
                        <tbody>
                          <tr>
                            <td style="border:hidden; border-bottom:1px; text-align:center; font-weight:bold" colspan="2">見事血統</td>
                          </tr>
                          <tr>
                            <td id="foal_group_17" class="UndefinedGr" width="20%">{{Sire_grp_attrib[1]}}</td>
                            <td id="foal_group_25" class="UndefinedGr" width="20%">{{Dam_grp_attrib[1]}}</td>
                          </tr>
                          <tr>
                            <td id="foal_group_21" class="UndefinedGr" width="20%">{{Sire_grp_attrib[3]}}</td>
                            <td id="foal_group_29" class="UndefinedGr" width="20%">{{Dam_grp_attrib[3]}}</td>
                          </tr>
                        </tbody>
                      </table>
                    </v-card>
                  </v-col>
                </v-row>
                <v-spacer class="my-5"/>
                <v-card max-width="100%">
                  <v-row class="mx-auto">
                    <v-col cols="12" sm="4" md="4" lg="4" xl="4">
                      <v-card id="mating_result" class="px-3 mt-4 boundary_bold mating1" height="80%">
                        <v-row align-content="center">
                          <v-col>
                            <p  style="font-size:15px; font-weight:bolder;text-align:center;" >
                              {{mating_result.Result}}
                            </p>
                          </v-col>
                        </v-row>
                      </v-card>
                    </v-col>
                    <v-col>
                      <v-row >
                        <v-col cols="4" sm="4" md="3" lg="3" xl="3" v-for="attr in mating_result.attrib" v-bind:key="attr.name">
                          <v-card class="mx-auto my-4" max-width="100%" elevation=0 >
                            <v-row >
                              <v-col cols="2" class="mx-3">
                                <v-avatar
                                  :class="def_attrib_class[def_attrib.indexOf(attr.name)]"
                                  style="border:outset;"
                                  tile
                                  size="24"
                                >
                                  <span class="text-body-2">{{attr.name}}</span>
                                </v-avatar>
                              </v-col>
                              <v-col>
                                <v-avatar
                                  title
                                  size="24"
                                  class="mx-n2"
                                >
                                  <span class="text-h6">{{attr.num}}</span>
                                </v-avatar>
                              </v-col>
                            </v-row>
                          </v-card>
                        </v-col>
                      </v-row>
                    </v-col>                      
                  </v-row>
                  <v-spacer class="my-5"/>
                  <v-row align-content="center" class="my-n8" v-if="mating_result.inbleed.length>0">
                    <v-col cols="12" v-for="inbleeded in mating_result.inbleed" v-bind:key="inbleeded.name">
                      <v-card class="mx-auto" max-width="100%" max-height="50%" elevation=0 >
                        <v-card-text class="text-center my-n5">
                          <h3 style="color: red">
                            {{inbleeded.name}}
                          </h3>
                      </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                  <v-row align-content="center" class="my-n13" v-if="mating_result.inbleed.length==0">
                    <v-col >
                      <v-card class="mx-auto" max-width="100%" elevation=0 >
                        <v-card-text class="text-center my-n2">
                          <h3 style="color: black">
                            なし
                          </h3>
                      </v-card-text>
                      </v-card>
                    </v-col>
                  </v-row>
                </v-card>

                <v-checkbox class="my-13 py-5 mb-n13" v-model="foal_pedigree_active" label="血統を表示" />    
                <v-row>
                  <v-col cols="12" sm="12" md="12" lg="12" xl="12" style="width:120%">
                    <v-expand-transition>
                      <v-card v-show="foal_pedigree_active" elevation=0>
                        <v-spacer class="my-1"/> 
                          <table>
                            <tbody>
                              <tr>
                                <td class="colt" rowspan="8" width="5%">父</td>
                                <td id="foal-name-1" colspan="4">{{Sire_data.data[0]}}</td>
                                <td id="foal-attrib-1-1" width="10%">{{def_attrib[Sire_pdg_attrib[0][0]]}}</td>
                                <td id="foal-attrib-1-2" width="10%">{{def_attrib[Sire_pdg_attrib[0][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="colt" rowspan="4" width="5%">父</td>
                                <td id="foal-name-3" colspan="3">{{Sire_data.data[1]}}</td>
                                <td id="foal-attrib-3-1">{{def_attrib[Sire_pdg_attrib[1][0]]}}</td>
                                <td id="foal-attrib-3-2">{{def_attrib[Sire_pdg_attrib[1][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="colt" rowspan="2" width="5%">父</td>
                                <td id="foal-name-7" colspan="2">{{Sire_data.data[3]}}</td>
                                <td id="foal-attrib-7-1">{{def_attrib[Sire_pdg_attrib[3][0]]}}</td>
                                <td id="foal-attrib-7-2">{{def_attrib[Sire_pdg_attrib[3][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="colt" style="width:5%">父</td>
                                <td id="foal-name-15" >{{Sire_data.data[7]}}</td>
                                <td id="foal-attrib-15-1">{{def_attrib[Sire_pdg_attrib[7][0]]}}</td>
                                <td id="foal-attrib-15-2">{{def_attrib[Sire_pdg_attrib[7][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="filly">母</td>
                                <td class="colt" >父</td>
                                <td id="foal-name-17" >{{Sire_data.data[9]}}</td>
                                <td id="foal-attrib-17-1">{{def_attrib[Sire_pdg_attrib[9][0]]}}</td>
                                <td id="foal-attrib-17-2">{{def_attrib[Sire_pdg_attrib[9][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="filly" rowspan="3">母</td>
                                <td class="colt" rowspan="2">父</td>
                                <td id="foal-name-9" colspan="2">{{Sire_data.data[5]}}</td>
                                <td id="foal-attrib-9-1">{{def_attrib[Sire_pdg_attrib[5][0]]}}</td>
                                <td id="foal-attrib-9-2">{{def_attrib[Sire_pdg_attrib[5][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="colt" >父</td>
                                <td id="foal-name-19" >{{Sire_data.data[11]}}</td>
                                <td id="foal-attrib-19-1">{{def_attrib[Sire_pdg_attrib[11][0]]}}</td>
                                <td id="foal-attrib-19-2">{{def_attrib[Sire_pdg_attrib[11][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="filly">母</td>
                                <td class="colt" >父</td>
                                <td id="foal-name-21" >{{Sire_data.data[13]}}</td>
                                <td id="foal-attrib-21-1">{{def_attrib[Sire_pdg_attrib[13][0]]}}</td>
                                <td id="foal-attrib-21-2">{{def_attrib[Sire_pdg_attrib[13][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="filly" rowspan="7">母</td>
                                <td class="colt" rowspan="4">父</td>
                                <td id="foal-name-5" colspan="3">{{Dam_data.data[1]}}</td>
                                <td id="foal-attrib-5-1">{{def_attrib[Dam_pdg_attrib[1][0]]}}</td>
                                <td id="foal-attrib-5-2">{{def_attrib[Dam_pdg_attrib[1][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="colt" rowspan="2">父</td>
                                <td id="foal-name-11" colspan="2">{{Dam_data.data[3]}}</td>
                                <td id="foal-attrib-11-1">{{def_attrib[Dam_pdg_attrib[3][0]]}}</td>
                                <td id="foal-attrib-11-2">{{def_attrib[Dam_pdg_attrib[3][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="colt" >父</td>
                                <td id="foal-name-23" >{{Dam_data.data[7]}}</td>
                                <td id="foal-attrib-23-1">{{def_attrib[Dam_pdg_attrib[7][0]]}}</td>
                                <td id="foal-attrib-23-2">{{def_attrib[Dam_pdg_attrib[7][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="filly">母</td>
                                <td class="colt" >父</td>
                                <td id="foal-name-25" >{{Dam_data.data[9]}}</td>
                                <td id="foal-attrib-25-1">{{def_attrib[Dam_pdg_attrib[9][0]]}}</td>
                                <td id="foal-attrib-25-2">{{def_attrib[Dam_pdg_attrib[9][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="filly" rowspan="3">母</td>
                                <td class="colt" rowspan="2">父</td>
                                <td id="foal-name-13" colspan="2">{{Dam_data.data[5]}}</td>
                                <td id="foal-attrib-13-1">{{def_attrib[Dam_pdg_attrib[5][0]]}}</td>
                                <td id="foal-attrib-13-2">{{def_attrib[Dam_pdg_attrib[5][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="colt">父</td>
                                <td id="foal-name-27" >{{Dam_data.data[11]}}</td>
                                <td id="foal-attrib-27-1">{{def_attrib[Dam_pdg_attrib[11][0]]}}</td>
                                <td id="foal-attrib-27-2">{{def_attrib[Dam_pdg_attrib[11][1]]}}</td>
                              </tr>
                              <tr>
                                <td class="filly">母</td>
                                <td class="colt" >父</td>
                                <td id="foal-name-29" >{{Dam_data.data[13]}}</td>
                                <td id="foal-attrib-29-1">{{def_attrib[Dam_pdg_attrib[13][0]]}}</td>
                                <td id="foal-attrib-29-2">{{def_attrib[Dam_pdg_attrib[13][1]]}}</td>
                              </tr>                
                            </tbody>
                          </table>
                        <v-spacer class="pb-3"/>
                      </v-card>
                    </v-expand-transition>
                  </v-col>
                </v-row>
              </v-spacer>
            </v-card>
          </v-expand-transition>
        </v-col>
        <v-col cols="12" sm="12" md="12" lg="6" xl="6">
          <v-expand-transition>
            <v-card v-show="mating_result_active" style="width:100%" elevation=5 class="py-n3 pb-n5">
              <v-spacer class="mx-5 py-3 my-1">
                <v-card-title style="font-size:24px;font-weight:bolder;" class="px-0" outlined>
                  産駒登録フォーム
                </v-card-title>
                <v-row>
                  <v-col>
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
                  </v-col>
                </v-row>
              </v-spacer>
            </v-card>
          </v-expand-transition>
        </v-col>
      </v-row>
    </v-layout>
    <v-spacer class="my-0 px-0 mx-0 py-0" />
    <v-layout justify-center>
      <v-row class="mx-5">
        <v-col cols="12"> 
          <v-btn color="deep-orange" @click="erase" block>
            <h2 style="color: white;">自家製データを全てクリアする</h2>
          </v-btn>
        </v-col>
      </v-row>
    </v-layout>
  </v-container>
</template>

<script>
  import Dexie from 'dexie';
  //import FilterableDropDown from './FilterableDropDown.vue'

  export default {
    name: 'PdMakerMain',

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
      Sire_grp_attrib:Array(9).fill(""),
      Dam_grp_attrib: Array(9).fill(""),
      Foal_grp_attrib: Array(9).fill(""),
      sire_pedigree_active: false,
      dam_pedigree_active: false,
      def_attrib: ["","短","速","底","長","ダ","丈","早","晩","堅","難"],
      def_attrib_class: ["","tankyori","sokuryoku","sokodikara","chokyori","dart","jobu","sojuku","bansei","kenjitu","kishonan"],

      mating_props: false,
      mating_result_active: false,
      mating_result:{"Result": "理論なし", "inbleed": [{"name":""}], "attrib":[{"name":"", "num": 0}]},

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
        indexes.map((data,index)=>{
          var item = document.getElementById('sire_group_' + data[0]);
          item.className = this.Sire_grp_attrib[index];
          
          data.map(d_data=>{
            var item = document.getElementById('sire-attrib-'+d_data+'-1');
            item.className = attributes[this.Sire_pdg_attrib[d_data][0]];
            item = document.getElementById('sire-attrib-'+d_data+'-2');
            item.className = attributes[this.Sire_pdg_attrib[d_data][1]];
            return true;
          })
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
        indexes.map((data,index)=>{
          var item = document.getElementById('dam_group_' + data[0]);
          item.className = this.Dam_grp_attrib[index];
          
          data.map(d_data=>{
            var item = document.getElementById('dam-attrib-'+d_data+'-1');
            item.className = attributes[this.Dam_pdg_attrib[d_data][0]];
            item = document.getElementById('dam-attrib-'+d_data+'-2');
            item.className = attributes[this.Dam_pdg_attrib[d_data][1]];
            return true;
          })
        })
        this.compute_relative()
      },

      toHex(num,fm){
        var s=num.toString(16);
        if(fm==undefined) return s;
        var dLen=s.toString(16).length;
        s= Array(fm.length-dLen+1).join('0')+s;
        return  s;
      },

      submit_foal(){
        if(this.Dam_data==="" | this.Sire_data===""){
          alert("両親のいずれかが未定義です。\n父馬・母馬双方を選択してください。")
          return false
        }
        var data_string=JSON.stringify(this.mySire) + JSON.stringify(this.myDam)
        var name_list=data_string.split(/,|{|}|:|\[|\]|"/);
        name_list = Array.from(new Set(name_list))
        if (name_list.includes("★"+this.foal_name) | name_list.includes(this.foal_name)){
          alert(this.foal_name + " は既に別の馬で使用されています。\n別の馬名を指定してください。");
          return false;
        }else{
          {
            this.foal_name = "★" + this.foal_name
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

            this.Foal_pdg_attrib[0] = ["",""]
            this.Foal_pdg_attrib[1] = this.Sire_pdg_attrib[0]
            this.Foal_pdg_attrib[3] = this.Sire_pdg_attrib[1]
            this.Foal_pdg_attrib[4] = this.Sire_pdg_attrib[2]
            this.Foal_pdg_attrib[7] = this.Sire_pdg_attrib[3]
            this.Foal_pdg_attrib[8] = this.Sire_pdg_attrib[4]
            this.Foal_pdg_attrib[9] = this.Sire_pdg_attrib[5]
            this.Foal_pdg_attrib[10] = this.Sire_pdg_attrib[6]
            this.Foal_pdg_attrib[15] = this.Sire_pdg_attrib[7]
            this.Foal_pdg_attrib[16] = this.Sire_pdg_attrib[8]
            this.Foal_pdg_attrib[17] = this.Sire_pdg_attrib[9]
            this.Foal_pdg_attrib[18] = this.Sire_pdg_attrib[10]
            this.Foal_pdg_attrib[19] = this.Sire_pdg_attrib[11]
            this.Foal_pdg_attrib[20] = this.Sire_pdg_attrib[12]
            this.Foal_pdg_attrib[21] = this.Sire_pdg_attrib[13]
            this.Foal_pdg_attrib[22] = this.Sire_pdg_attrib[14]
            this.Foal_pdg_attrib[31] = this.Sire_pdg_attrib[15]
            this.Foal_pdg_attrib[32] = this.Sire_pdg_attrib[16]
            this.Foal_pdg_attrib[33] = this.Sire_pdg_attrib[17]
            this.Foal_pdg_attrib[34] = this.Sire_pdg_attrib[18]
            this.Foal_pdg_attrib[35] = this.Sire_pdg_attrib[19]
            this.Foal_pdg_attrib[36] = this.Sire_pdg_attrib[20]
            this.Foal_pdg_attrib[37] = this.Sire_pdg_attrib[21]
            this.Foal_pdg_attrib[38] = this.Sire_pdg_attrib[22]
            this.Foal_pdg_attrib[39] = this.Sire_pdg_attrib[23]
            this.Foal_pdg_attrib[40] = this.Sire_pdg_attrib[24]
            this.Foal_pdg_attrib[41] = this.Sire_pdg_attrib[25]
            this.Foal_pdg_attrib[42] = this.Sire_pdg_attrib[26]
            this.Foal_pdg_attrib[43] = this.Sire_pdg_attrib[27]
            this.Foal_pdg_attrib[44] = this.Sire_pdg_attrib[28]
            this.Foal_pdg_attrib[45] = this.Sire_pdg_attrib[29]
            this.Foal_pdg_attrib[46] = this.Sire_pdg_attrib[30]

            this.Foal_pdg_attrib[2] = this.Dam_pdg_attrib[0]
            this.Foal_pdg_attrib[5] = this.Dam_pdg_attrib[1]
            this.Foal_pdg_attrib[6] = this.Dam_pdg_attrib[2]
            this.Foal_pdg_attrib[11] = this.Dam_pdg_attrib[3]
            this.Foal_pdg_attrib[12] = this.Dam_pdg_attrib[4]
            this.Foal_pdg_attrib[13] = this.Dam_pdg_attrib[5]
            this.Foal_pdg_attrib[14] = this.Dam_pdg_attrib[6]
            this.Foal_pdg_attrib[23] = this.Dam_pdg_attrib[7]
            this.Foal_pdg_attrib[24] = this.Dam_pdg_attrib[8]
            this.Foal_pdg_attrib[25] = this.Dam_pdg_attrib[9]
            this.Foal_pdg_attrib[26] = this.Dam_pdg_attrib[10]
            this.Foal_pdg_attrib[27] = this.Dam_pdg_attrib[11]
            this.Foal_pdg_attrib[28] = this.Dam_pdg_attrib[12]
            this.Foal_pdg_attrib[29] = this.Dam_pdg_attrib[13]
            this.Foal_pdg_attrib[30] = this.Dam_pdg_attrib[14]
            this.Foal_pdg_attrib[47] = this.Dam_pdg_attrib[15]
            this.Foal_pdg_attrib[48] = this.Dam_pdg_attrib[16]
            this.Foal_pdg_attrib[49] = this.Dam_pdg_attrib[17]
            this.Foal_pdg_attrib[50] = this.Dam_pdg_attrib[18]
            this.Foal_pdg_attrib[51] = this.Dam_pdg_attrib[19]
            this.Foal_pdg_attrib[52] = this.Dam_pdg_attrib[20]
            this.Foal_pdg_attrib[53] = this.Dam_pdg_attrib[21]
            this.Foal_pdg_attrib[54] = this.Dam_pdg_attrib[22]
            this.Foal_pdg_attrib[55] = this.Dam_pdg_attrib[23]
            this.Foal_pdg_attrib[56] = this.Dam_pdg_attrib[24]
            this.Foal_pdg_attrib[57] = this.Dam_pdg_attrib[25]
            this.Foal_pdg_attrib[58] = this.Dam_pdg_attrib[26]
            this.Foal_pdg_attrib[59] = this.Dam_pdg_attrib[27]
            this.Foal_pdg_attrib[60] = this.Dam_pdg_attrib[28]
            this.Foal_pdg_attrib[61] = this.Dam_pdg_attrib[29]
            this.Foal_pdg_attrib[62] = this.Dam_pdg_attrib[30]

          }

          var foal_attrib = this.Foal_grp_attrib.concat(this.Foal_pdg_attrib.map(elm=>{
            return this.toHex(elm[0]*256+elm[1],'0000')
          }))
          foal_attrib = [{"name": this.foal_name, "attrib": foal_attrib}]
          
          this.dexie_db.PdStore.get("attrib_data")
          .then(data=>{
            if ((typeof data === "undefined")){
              return foal_attrib
            }else{
              var tmp_append_foal_data = data.dict_content
              tmp_append_foal_data = tmp_append_foal_data.concat(foal_attrib);
              return tmp_append_foal_data;
            }
          })
          .then(data=>{
            this.dexie_db.PdStore.put({"dict_name":"attrib_data","dict_content":data});
            this.attrib_data = this.attrib_data.concat(foal_attrib);
          })
          .catch(err=>{
            alert(err)
          });

          if(this.foal_sex === "0"){
            this.dexie_db.PdStore.get("sire_data")
            .then(data=>{
              if ((typeof data === "undefined")){
                return [this.foal_pedigree]
              }else{
                var tmp_append_sire_data = data.dict_content
                tmp_append_sire_data = tmp_append_sire_data.concat([this.foal_pedigree]);
                return tmp_append_sire_data;
              }
            })
            .then(data=>{
              this.dexie_db.PdStore.put({"dict_name":"sire_data","dict_content":data});
              return true
            }).then(data=>{
              alert(this.foal_name + " のデータ追加が正しく完了しました");
              this.mySire = this.mySire.concat([this.foal_pedigree]);
              this.mySire.sort((a,b)=>{
                if(a.name < b.name) return -1;
                if(a.name > b.name) return 1;
                return 0;
              })
              this.myDam.sort((a,b)=>{
                if(a.name < b.name) return -1;
                if(a.name > b.name) return 1;
                return 0;
              })
              data
              this.refreshfoal()
            })
            .catch(err=>{
              alert(err)
            });
          }else{
            this.dexie_db.PdStore.get("dam_data")
            .then(data=>{
              if ((typeof data === "undefined")){
                return [this.foal_pedigree]
              }else{
                var tmp_append_dam_data = data.dict_content
                tmp_append_dam_data = tmp_append_dam_data.concat([this.foal_pedigree]);
                return tmp_append_dam_data;
              }
            })
            .then(data=>{
              this.dexie_db.PdStore.put({"dict_name":"dam_data","dict_content":data});
              return true
            }).then(data=>{
              alert(this.foal_name + " のデータ追加が正しく完了しました");
              this.myDam = this.myDam.concat([this.foal_pedigree]);
              this.mySire.sort((a,b)=>{
                if(a.name < b.name) return -1;
                if(a.name > b.name) return 1;
                return 0;
              })
              this.myDam.sort((a,b)=>{
                if(a.name < b.name) return -1;
                if(a.name > b.name) return 1;
                return 0;
              })
              data
              this.refreshfoal()
            })
            .catch(err=>{
              alert(err)
            });
          }
        window.scrollTo(0,0)

        }
      },

      refreshfoal(){
        this.Sire_data={"data":Array(62)},
        this.Dam_data={"data":Array(62)},
        this.Foal_pdg_attrib= Array(63).fill(["",""]),
        this.Foal_grp_attrib= Array(9).fill(""),

        this.mating_props=false,
        this.mating_result_active=false,
        this.mating_result={"Result":"理論なし", "inbleed":[{"name":""}], "attrib":[{"name":"", "num":0}]},

        this.foal_name="",
        this.foal_pedigree={"name":"", "data":Array(62)},
        this.foal_sex="0" ,
        this.foal_pedigree_active=false  
      },   

      getAllIndexes(arr, val) {
        var indexes = [], i = -1;
        while ((i = arr.indexOf(val, i+1)) != -1){
            indexes.push(i);
        }
        return indexes;
      },

      compute_inbleed(){

        var inbleed_result = []
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
            _all_father_in.map((father_id_in_dam)=>{
              if(_all_mother_in.findIndex(mother_id_in_dam=> mother_id_in_dam===father_id_in_dam+1) != -1){
                //インブリード対象で，両親が見つかった馬が居ればインブリードとして追加
                var inbleed_index_in_dam = parseInt((father_id_in_dam-1)/2.0)
                inbleed_result.push([index,inbleed_index_in_dam])
                return true
              }else{
                return false
              }
            })
          }
        });

        var inbleed_horse_name = inbleed_result.map((elm)=>{
          return [this.Sire_data.data[elm[0]],this.Dam_data.data[elm[1]]]
        })
        inbleed_horse_name = Array.from(new Set(inbleed_horse_name.flat())) 
        
        inbleed_result = inbleed_result.filter(elm=>{
          var child_data_a = this.Sire_data.data[(elm[0]%2===1)? parseInt((elm[0]-1)/2.0) : parseInt((elm[0]-2)/2.0)];
          var child_data_b = this.Dam_data.data[(elm[1]%2===1)? parseInt((elm[1]-1)/2.0) : parseInt((elm[1]-2)/2.0)];
          return (!(inbleed_horse_name.includes(child_data_a)) & !(inbleed_horse_name.includes(child_data_b)))
        })

        inbleed_horse_name = inbleed_result.map((elm)=>{
          return [this.Sire_data.data[elm[0]],this.Dam_data.data[elm[1]]]
        })
        inbleed_horse_name = Array.from(new Set(inbleed_horse_name.flat()))       
        return [inbleed_result,inbleed_horse_name]
      },

      compute_relative(){
        if((typeof this.Dam_data.data[0]==='undefined') | (typeof this.Sire_data.data[0]==='undefined')){
          return false
        }else{
          this.mating_result_active = true;
          this.mating_props = true;
          this.mating_result = {"Result": "理論なし", "inbleed": [{"name":""}], "attrib":[{"name":"", "num": 0}]};
          //まずは血統関連の処理から
          {
            this.Foal_grp_attrib[0] = this.Sire_grp_attrib[0]
            this.Foal_grp_attrib[1] = this.Sire_grp_attrib[2]
            this.Foal_grp_attrib[2] = this.Dam_grp_attrib[0]
            this.Foal_grp_attrib[3] = this.Dam_grp_attrib[2]
            this.Foal_grp_attrib[4] = this.Sire_grp_attrib[1]
            this.Foal_grp_attrib[5] = this.Sire_grp_attrib[3]
            this.Foal_grp_attrib[6] = this.Dam_grp_attrib[1]
            this.Foal_grp_attrib[7] = this.Dam_grp_attrib[3]
            this.Foal_grp_attrib[8] = this.Sire_grp_attrib[8]
          }

          
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
          {
            var item = document.getElementById('foal_group_1');
            item.className = this.Sire_grp_attrib[0];         
            item = document.getElementById('foal_group_9');
            item.className = this.Sire_grp_attrib[2];     
            item = document.getElementById('foal_group_5');
            item.className = this.Dam_grp_attrib[0];     
            item = document.getElementById('foal_group_13');
            item.className = this.Dam_grp_attrib[2];
            item = document.getElementById('foal_group_17');
            item.className = this.Sire_grp_attrib[1];
            item = document.getElementById('foal_group_21');
            item.className = this.Sire_grp_attrib[3];
            item = document.getElementById('foal_group_25');
            item.className = this.Dam_grp_attrib[1];
            item = document.getElementById('foal_group_29');
            item.className = this.Dam_grp_attrib[3];
            
            var sire_omosiro = this.Sire_grp_attrib.slice(0,4);
            var sire_migoto = this.Sire_grp_attrib.slice(4,8);
            var dam_omosiro = this.Dam_grp_attrib.slice(0,4);
            
            var omosiro_num = Array.from(new Set(sire_omosiro.concat(dam_omosiro))).length;
            var migoto_flag = (sire_migoto.sort().toString()===dam_omosiro.sort().toString())
            var _sire_migoto = Array.from(new Set(sire_migoto))
            var _dam_omosiro = Array.from(new Set(dam_omosiro))
            const reducer = (accumulator, currentValue) => accumulator + currentValue;
            var yokudeki_sire_to_dam = _sire_migoto.map(elm=>{return dam_omosiro.filter(elmb=>elmb===elm).length}).reduce(reducer)
            var yokudeki_dam_to_sire = _dam_omosiro.map(elm=>{return sire_migoto.filter(elmb=>elmb===elm).length}).reduce(reducer)
            var yokudeki_flag = (yokudeki_sire_to_dam>=3 & yokudeki_dam_to_sire>=3);
            item = document.getElementById("mating_result")

            if(omosiro_num >= 7){
              if(migoto_flag){
                //完璧な配合
                this.mating_result.Result = "完璧な配合"
                item.className = "px-3 mt-4 boundary_bold mating5"
              }else{
                if(yokudeki_flag){
                  this.mating_result.Result = "面白＆良出"
                  item.className = "px-3 mt-4 boundary_bold mating3"                  
                }else{
                  this.mating_result.Result = "面白い配合"
                  item.className = "px-3 mt-4 boundary_bold mating1"                      
                }
              }
            }else{
              if(migoto_flag){
                this.mating_result.Result = "見事な配合"
                item.className = "px-3 mt-4 boundary_bold mating4"
              }else{
                if(yokudeki_flag){
                  this.mating_result.Result = "よくできた配合"
                  item.className = "px-3 mt-4 boundary_bold mating2"                  
                }else{
                  this.mating_result.Result = "理論なし"
                  item.className = "px-3 mt-4 boundary_bold mating0"        
                }
              }              
            }
          }
          var counter = 0;
          var counter_b= 0;
          id_index.map((data)=>{
            data.map(d_data=>{
              if(_index_to_foal[counter_b] >= 0){
                var item = document.getElementById('foal-attrib-'+d_data+'-1');
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

          id_index.flat().map((data)=>{
            var _item = document.getElementById('sire-name-'+data);
            _item.className = "outbleed";
            _item = document.getElementById('dam-name-'+data);
            _item.className = "outbleed";
            _item = document.getElementById('foal-name-'+data);
            _item.className = "outbleed";
          })
          var res = this.compute_inbleed()
          

          res[0].map((data)=>{
            var _item = document.getElementById('sire-name-'+data[0]);
            if(_item != null){
              _item.className = "inbleed";
            }
            var _index = _index_to_foal.findIndex(elm=>elm===data[0]);
            _item = document.getElementById('foal-name-'+id_index.flat()[_index]);
            if(_item != null){
              _item.className = "inbleed";
            }
            _item = document.getElementById('dam-name-'+data[1]);
            if(_item != null){
              _item.className = "inbleed";
            }
            _index = _index_to_foal.findIndex(elm=>elm===(-data[1]));
            _item = document.getElementById('foal-name-'+id_index.flat()[_index]);
            if(_item != null){
              _item.className = "inbleed";
            }
          })

          //インブリードしてる馬を集める
          this.mating_result.inbleed = res[0].map((elm=>{
            if(this.Sire_data.data[elm[0]]!=this.Dam_data.data[elm[1]]){
              var inbleed_str_sire = this.getAllIndexes(this.Sire_data.data,this.Sire_data.data[elm[0]])
              .concat(this.getAllIndexes(this.Dam_data.data,this.Sire_data.data[elm[0]]))
              .map(_elm=>{
                return (
                  (_elm >= 31) ? 6 :
                  (_elm < 31 & _elm >= 15) ? 5 :
                  (_elm < 15 & _elm >= 7) ? 4 :
                  (_elm < 7 & _elm >= 3) ? 3 :
                  (_elm < 3 & _elm >= 1) ? 2 : 1
                )
              }).filter((d)=>{
                if(d < 6){
                  return true
                }
                return false
              }).join("x")
              var inbleed_str_dam = this.getAllIndexes(this.Dam_data.data,this.Dam_data.data[elm[1]])
              .concat(this.getAllIndexes(this.Sire_data.data,this.Dam_data.data[elm[1]]))
              .map(_elm=>{
                return (
                  (_elm >= 31) ? 6 :
                  (_elm < 31 & _elm >= 15) ? 5 :
                  (_elm < 15 & _elm >= 7) ? 4 :
                  (_elm < 7 & _elm >= 3) ? 3 :
                  (_elm < 3 & _elm >= 1) ? 2 : 1
                )
              }).filter((d)=>{
                if(d < 6){
                  return true
                }
                return false
              }).join("x")
              return {"name":this.Sire_data.data[elm[0]].toString() + ", " + this.Dam_data.data[elm[1]].toString() + " " +inbleed_str_sire + 'x' + inbleed_str_dam}
            }else{
              var inbleed_indexes = this.getAllIndexes(this.Sire_data.data,this.Sire_data.data[elm[0]]).concat(
                this.getAllIndexes(this.Dam_data.data,this.Dam_data.data[elm[1]])
              )
              var out_str = inbleed_indexes.map(_elm=>{
                return (
                  (_elm >= 31) ? 6 :
                  (_elm < 31 & _elm >= 15) ? 5 :
                  (_elm < 15 & _elm >= 7) ? 4 :
                  (_elm < 7 & _elm >= 3) ? 3 :
                  (_elm < 3 & _elm >= 1) ? 2 : 1
                )
              }).filter((d)=>{
                if(d < 6){
                  return true
                }
                return false
              }).join("x")
              return {"name":this.Sire_data.data[elm[0]].toString() + " " + out_str}
              }
          }))

          this.mating_result.inbleed = this.mating_result.inbleed.filter((elm,index,self)=>{
            return (self.map(_elm=>_elm.name).indexOf(elm.name) === index)
          })
          //危険な配合の処理
          var inbleed_result_txt = this.mating_result.inbleed.map(elm=>elm.name).join()
          if(inbleed_result_txt.match(/1x[1-6]|[1-6]x1|2x2/g)){
            item = document.getElementById("mating_result")
            this.mating_result.Result = "危険な配合"
            item.className = "px-3 mt-4 boundary_bold mating6"
          }

          //配合結果の格納
          var attribs = this.Sire_pdg_attrib.concat(this.Dam_pdg_attrib)
          var names = this.Sire_data.data.concat(this.Dam_data.data)
          attribs = attribs.filter((elm,index)=>{
            return (res[1].includes(names[index]))&(names.indexOf(names[index])===index)
          }).flat()
          var attrib_counter = Array.from(new Set(attribs))
          this.mating_result.attrib = attrib_counter.map((elm)=>{
            var counter_ = attribs.filter(x=>x===elm).length;
            return {"name": this.def_attrib[elm],"num": counter_}
          }).filter(elm=>elm.name!="")
          
        }
      },

      erase(){
        if(window.confirm('自家製産駒をすべてクリアしますか？')){
          this.dexie_db.PdStore.clear();
          this.dbinitializer();
          alert('自家製産駒をすべてクリアしました')
        }
      },

      initializer(){
        this.dexie_db=null,
        this.Sire_data={"data":Array(62)},
        this.mySire= [],
        this.Dam_data={"data":Array(62)},
        this.myDam= [],
        this.attrib_data=[],
        this.Sire_pdg_attrib= Array(63).fill(["",""]),
        this.Dam_pdg_attrib= Array(63).fill(["",""]),
        this.Foal_pdg_attrib= Array(63).fill(["",""]),
        this.Sire_grp_attrib= Array(9).fill(""),
        this.Dam_grp_attrib= Array(9).fill(""),
        this.Foal_grp_attrib= Array(9).fill(""),
        this.sire_pedigree_active= false,
        this.dam_pedigree_active= false,

        this.mating_props=false,
        this.mating_result_active=false,
        this.mating_result={"Result":"理論なし", "inbleed":[{"name":""}], "attrib":[{"name":"", "num":0}]},

        this.foal_name="",
        this.foal_pedigree={"name":"", "data":Array(62)},
        this.foal_sex="0" ,
        this.foal_pedigree_active=false
      },

      dbinitializer(){
        this.initializer()
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
            if (typeof dict_content === "undefined"){
              return false
            }
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
          .then((data)=>{
            if (typeof dict_content === "undefined"){
              return false
            }
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
            return true;
          }).then(tf=>{
            this.mySire.sort((a,b)=>{
              if(a.name < b.name) return -1;
              if(a.name > b.name) return 1;
              return 0;
            })
            this.myDam.sort((a,b)=>{
              if(a.name < b.name) return -1;
              if(a.name > b.name) return 1;
              return 0;
            })
            return tf
          })


        this.dexie_db.PdStore.get("attrib_data")
          .then(data=>{
            if (typeof dict_content === "undefined"){
              return false
            }
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
            return true;
          }).then(tf=>{
            this.mySire.sort((a,b)=>{
              if(a.name < b.name) return -1;
              if(a.name > b.name) return 1;
              return 0;
            })
            this.myDam.sort((a,b)=>{
              if(a.name < b.name) return -1;
              if(a.name > b.name) return 1;
              return 0;
            })
            return tf
          })

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
  font-size: 15px;
  font-size: clamp(10px, 1vw, 15px);
  height: 25px;
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
  font-size: 10px;
  font-size: clamp(6px, 1vw, 10px);
  border-collapse: collapse;
}
.filly{
  border: solid;
  background-color: #e9b380;
  font-weight: bold;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 10px;
  font-size: clamp(6px, 1vw, 10px);
  border-collapse: collapse;
}
.no-attributes{
  border: solid;
  background-color: #FFFFFF;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.tankyori{
  border: solid;
  background-color: #FAFF4D;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.sokuryoku{
  border: solid;
  background-color: #FFFAB4;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.sokodikara{
  border: solid;
  background-color: #F4781A;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.chokyori{
  border: solid;
  background-color: #06F0FB;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.dart{
  border: solid;
  background-color: #FDDBA5;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.jobu{
  border: solid;
  background-color: #FDABDC;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.sojuku{
  border: solid;
  background-color: #3DAC3F;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.bansei{
  border: solid;
  background-color: #A5E319;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.kishonan{
  border: solid black;
  background-color: #FA06FA;
  font-weight: bold;  
  color:white;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.kenjitu{
  border: solid;
  background-color: #999999;
  font-weight: bold;  
  text-shadow: 0px 0px 2px #FFFFFF;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  border-collapse: collapse;
}
.Ec{
  background-color: white;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Ph{
  background-color: lightsteelblue;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Ns{
  background-color: mediumaquamarine;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Ro{
  background-color: lightpink;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Ne{
  background-color: yellow;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Na{
  background-color: lightskyblue;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Fa{
  background-color: khaki;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.To{
  background-color: orange;
  border-color: black;
  text-align: center;
  color: white;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Te{
  background-color: purple;
  border-color: black;
  text-align: center;
  color: white;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Sw{
  background-color: peachpuff;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Ha{
  background-color: chartreuse;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Hi{
  background-color: mediumblue;
  text-align: center;
  color: white;
  border-color: black;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.St{
  background-color: slateblue;
  text-align: center;
  color: white;
  border-color:  black;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.Ma{
  background-color: darkorchid;
  text-align: center;
  border-color:  black;
  color: white;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.He{
  background-color: aqua;
  text-align: center;
  padding: 0px;
  padding-left: 0px;
  font-size: 20px;
  font-size: clamp(15px, 1vw, 20px);
}
.UndefinedGr{
  background-color: white;
  text-align: center;
  border-color:  black;
  color: white;
  padding: 0px;
  padding-left: 0px;
}
.inbleed{
  color: red;
  font-weight: bolder;
  border: 1px solid black !important;
}
.outbleed{
  color: black;
  font-weight: normal;
  text-shadow: 0px 0px 0px;
  
}
.mating0{
  color: black;
  background-color: white;
  font-weight: bold;
}
.mating1{
  color: black;
  font-weight: bold;
  background: 
    -moz-radial-gradient(
      dimgray,
      gray
      ); 
  background: 
    -webkit-radial-gradient(
      dimgray,
      gray
    ); 
  background: 
    radial-gradient(
      dimgray,
      gray
    ); 
}
.mating2{
  color: black;
  font-weight: bold;
  background: 
    -moz-linear-gradient(
      to right top,
      coral,
      coral
      ); 
  background: 
    -webkit-linear-gradient(
      to right top,
      coral,
      coral
    ); 
  background: 
    linear-gradient(
      to right top,
      coral,
      coral
    ); 
}
.mating3{
  color: black;
  font-weight: bold;
  background: 
    -moz-linear-gradient(
      to right top,
      gray,
      coral
      ); 
  background: 
    -webkit-linear-gradient(
      to right top,
      gray,
      coral
      ); 
  background: 
    linear-gradient(
      to right top,
      gray,
      coral
      ); 
}
.mating4{
  color: black;
  font-weight: bold;
  background: 
    -moz-linear-gradient(
      to right top,
      #E2D06E,
      #E2D06E
      ); 
  background: 
    -webkit-linear-gradient(
      to right top,
      #E2D06E,
      #E2D06E
      ); 
  background: 
    linear-gradient(
      to right top,
      #E2D06E,
      #E2D06E
      ); 
}
.mating5{
  color: black;
  font-weight: bold;
  background: 
    -moz-linear-gradient(
      to right top,
      #8DC799,
      #C3E19C 7%,
      #FFF39B 17%,
      #F09C75 32%,
      #EC9EBD 56%,
      #8F82BA 72%,
      #7DCCF2
      ); 
  background: 
    -webkit-linear-gradient(
      to right top,
      #8DC799,
      #C3E19C 7%,
      #FFF39B 17%,
      #F09C75 32%,
      #EC9EBD 56%,
      #8F82BA 72%,
      #7DCCF2
      ); 
  background: 
    linear-gradient(
      to right top,
      #8DC799,
      #C3E19C 7%,
      #FFF39B 17%,
      #F09C75 32%,
      #EC9EBD 56%,
      #8F82BA 72%,
      #7DCCF2
      ); 
}
.mating6{
  color: black;
  font-weight: bold;
  background: 
    -moz-linear-gradient(
      to right top,
      red,
      red
      ); 
  background: 
    -webkit-linear-gradient(
      to right top,
      red,
      red
      ); 
  background: 
    linear-gradient(
      to right top,
      red,
      red
      ); 
}
.boundary_bold{
  text-shadow:
  white 1px 1px 1px,
  white 1px -1px 1px,
  white -1px 1px 1px,
  white -1px -1px 1px;
}
.boundary_bold_black{
  text-shadow:
  dimgray 1px 1px 1px,
  dimgray 1px -1px 1px,
  dimgray -1px 1px 1px,
  dimgray -1px -1px 1px;
}
</style>