import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import Home from './components/Home.vue'

const routes = [{
  path: '/',
  name: 'root',
  component: App
},
{
  path: '/',
  name: 'home',
  component: Home
}]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router