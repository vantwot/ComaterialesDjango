import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import login from './components/login.vue'
import singup from './components/singup.vue'
import Home from './components/Home.vue'

const routes = [{
  path: '/',
  name: 'root',
  component: App
},
{
  path : '/user/login',
  name: 'login',
  component: login
},
{
  path : '/user/singup',
  name: 'singup',
  component: singup
},
{
  path : '/home',
  name: 'home',
  component: Home
}
]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router