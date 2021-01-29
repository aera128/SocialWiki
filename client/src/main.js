import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VuePageTransition from 'vue-page-transition'
import vuetify from './plugins/vuetify';
import store from './store'


Vue.config.productionTip = false

Vue.use(VuePageTransition)

new Vue({
    router,
    vuetify,
    store,
    render: h => h(App)
}).$mount('#app')
