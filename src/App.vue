<template>
  <v-app>
    <v-app-bar
      app
      color="teal lighten-2"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Logo"
          class="shrink mr-2"
          contain
          src="./assets/icon_512x512.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="title logo"
          class="shrink mt-1 ml-n4 hidden-xs-only"
          contain
          min-width="350"
          src="./assets/title.png"
          width="100"
        />

        <v-img
          alt="title logo"
          class="shrink mt-1 ml-0 hidden-sm-and-up"
          contain
          min-width="175"
          src="./assets/title_2.png"
          width="100"
        />
      </div>
      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/Okuyuki30cm/dbms-pd-maker/tree/Readme"
        target="_blank"
        text
      >
        <span class="mr-2">Readme</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <PdMakerMain/>
    </v-main>
  </v-app>
</template>

<script>
import PdMakerMain from './components/PdMakerMain';


export default {
  name: 'App',

  components: {
    PdMakerMain,
  },

  data: () => ({
    //
  }),
};
</script>
