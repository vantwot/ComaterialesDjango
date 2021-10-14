<template>
  <div id = "wrapper">
    <nav class="navbar is-dark"> 
      <div class="navbar-brand">
        <router-link to="/" class = "navbar-item"><strong>Comateriales</strong></router-link>
        

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden = "true"></span>
          <span aria-hidden = "true"></span>
          <span aria-hidden = "true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/tienda" class="navbar-item">Tienda</router-link>
          <router-link to="/ofertas" class="navbar-item">Ofertas</router-link>
          <router-link to="/nosotros" class="navbar-item">Nosotros</router-link>
          <router-link to="/contactenos" class="navbar-item">Contactenos</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Ingresar</router-link>

              <router-link to="/cart" class="button is-succes">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Carrito</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (C) 2021</p>
      
    </footer>

    <router-view/>
  </div>
</template>

<script>
export default{
  data() {
    return{
      showMobileMenu: false,
    }
  }
}
</script>


<style lang="scss">
  @import '../node_modules/bulma';
</style>
