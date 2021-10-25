import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import login from './components/login.vue'
import singup from './components/singup.vue'


const routes = [{
  path: '/',
  name: 'root',
  component: App
},
{
  path : '/',
  name: 'login',
  component: login
}]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router