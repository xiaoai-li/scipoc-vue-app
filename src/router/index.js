import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import About from '../views/About.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/webmap',
    name: 'WebMap',
    component: () => import(/* webpackChunkName: "about" */ '../views/WebView.vue'),
  },
  {
    path: '/upload',
    component: () => import(/* webpackChunkName: "about" */ '../views/UploadView.vue'),
  },
  {
    path: '/download/:id',
    component: () => import(/* webpackChunkName: "about" */ '../views/DownloadView.vue'),
  },

];

const router = new VueRouter({
  routes,
});

export default router;
