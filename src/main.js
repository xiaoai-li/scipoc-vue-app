import axios from 'axios';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';


import Vue from 'vue';
import App from './App.vue';
import router from './router';


Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.prototype.$axios = axios.create();
Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
