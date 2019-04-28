import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';

import App from './App.vue';
import router from './router';
import store from './store';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import './assets/styles.scss';

import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faCar,
  faMoneyBillWaveAlt,
  faHourglassHalf,
  faFilePdf,
  faSearchPlus,
  faFileInvoiceDollar,
  faThumbsUp,
  faThumbsDown,
  faDownload,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(
  faCar,
  faFileInvoiceDollar,
  faMoneyBillWaveAlt,
  faHourglassHalf,
  faFilePdf,
  faSearchPlus,
  faDownload,
  faThumbsDown,
  faThumbsUp,
);
Vue.component('fa-icon', FontAwesomeIcon);

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
