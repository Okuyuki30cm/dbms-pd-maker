import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false
import lodashGet from 'lodash/get'
Vue.prototype.$get = lodashGet

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
