import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'https://comateriales-be.herokuapp.com/'

createApp(App).use(router, axios).mount('#app')
