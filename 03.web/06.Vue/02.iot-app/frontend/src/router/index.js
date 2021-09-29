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
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/mqtt',
    name: 'Mqtt',
    component: () => import('../views/Mqtt.vue')
  },
  {
    path: '/securecamera',
    name: 'SecureCamera',
    component: () => import('../views/SecureCamera.vue')
  },
  {
    path: '/explorationcar',
    name: 'ExplorationCar',
    component: () => import('../views/ExplorationCar.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  base: '/iot/',
  routes
})

export default router
