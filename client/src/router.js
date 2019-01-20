import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import View from './views/View.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      children: [
        {
          path: '/login',
          component: Login,
        },
      ],
    },
    {
      path: '/view',
      name: 'view',
      component: View,
    },
  ],
});
