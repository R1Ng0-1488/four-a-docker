import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/news',
    name: 'News',
    component: () => import("../views/News.vue")
  },
  {
      path: '/news/:id',
      name: 'SingleNews',
      component: () => import("../views/SingleNews.vue"),
      props: true
  },
  {
      path: '/news/create/add',
      name: 'CreateNews',
      component: () => import('../views/CreateNews.vue'),
      // props: true
  },
  {
    path: '/videos',
    name: 'Videos',
    component: () => import("../views/Videos.vue")
  },
  {
    path: '/music',
    name: 'Music',
    component: () => import("../views/Music.vue")
  },
  {
    path: '/biog',
    name: 'Bio',
    component: () => import("../views/Bio.vue")
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: () => import("../views/Contacts.vue")
  },
  {
    path: '/images',
    name: 'Images',
    component: () => import("../views/Images.vue")
  },
  {
    path: '/images/:id',
    name: 'SingleImages',
    component: () => import("../views/SingleImages.vue"),
    props: true
  },
  {
    path: '/images/create/add',
    name: 'CreateImages',
    component: () => import("../views/CreateImages.vue"),
  },
  {
    path: '/texts',
    name: 'Texts',
    component: () => import("../views/Texts.vue")
  },
  {
    path: '/texts/:id',
    name: 'SingleTexts',
    component: () => import("../views/SingleTexts.vue"),
    props: true
  },
  {
    path: '/texts/create/add',
    name: 'CreateTexts',
    component: () => import("../views/CreateTexts.vue"),
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  // mode: 'history',
  routes
})

export default router
