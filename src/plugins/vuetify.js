import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import ja from 'vuetify/es5/locale/ja.js'

Vue.use(Vuetify);

Vue.component('my-component', {
  methods: {
    changeLocale () {
      this.$vuetify.lang.current = 'ja'
    },
  },
})

export default new Vuetify({
    lang: {
        locales: { ja },
        current: 'ja',
      },
});
