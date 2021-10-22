<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Bienvenido a Comateriales
            </p>
            <p class="subtitle">
                Donde los sueños se hacen realidad
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Ultimos productos</h2>
      </div>

        <div class="navbar-end">
          <router-link to="/" class="navbar-item">Sala</router-link>
          <router-link to="/ofertas" class="navbar-item">Cocina</router-link>
          <router-link to="/ofertas" class="navbar-item">Habitación</router-link>
          <router-link to="/" class="navbar-item">Accesorios</router-link>
        </div>


       <!-- esta es el for para mostrar los productos -->

      <!-- <ProductBox 
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product" /> -->

    </div>
  </div>
</template>


// <script> 
// import axios from 'axios'
// import ProductBox from '@/components/ProductBox'
// export default {
//   name: 'Home',
//   data() {
//     return {
//       latestProducts: []
//     }
//   },
//   components: {
//     ProductBox
//   },
//   mounted() {
//     this.getLatestProducts()
//     document.title = 'Home'
//   },
//   methods: {
//     async getLatestProducts() {
//       this.$store.commit('setIsLoading', true)
//       await axios
//         .get('/api/v1/latest-products/')
//         .then(response => {
//           this.latestProducts = response.data
//         })
//         .catch(error => {
//           console.log(error)
//         })
//       this.$store.commit('setIsLoading', false)
//     }
//   }
// }
// </script>