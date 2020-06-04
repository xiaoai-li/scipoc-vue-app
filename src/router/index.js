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
    component: () => import('../views/WebView.vue'),
  },
  {
    path: '/upload',
    name: 'Upload',
    component: () => import('../views/UploadView.vue'),
  },
  {
    path: '/seg',
    name: 'Segmentation',
    component: () => import('../views/SegmentationView.vue'),
  },
  {
    path: '/seg/:id',
    name: 'datapre',
    component: About,
  },
  {
    path: '/download/:id',
    component: () => import('../views/DownloadView.vue'),
  },

];

const router = new VueRouter({
  routes,
});

export default router;
