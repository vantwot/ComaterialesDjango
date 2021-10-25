<template>
  <div id="app" class="app">
    <nav class="navbar">
      <!-- LOGO -->
      <div class="logo">Comateriales</div>
      <!-- NAVIGATION MENU -->
      <ul class="nav-links">
        <!-- NAVIGATION MENUS -->
        <div class="menu">
          <li class="services">
            <a href="/">Cuenta</a>
            <!-- DROPDOWN MENU -->
            <ul class="dropdown">
              <li>
                <a v-if="!is_auth" v-on:click="loadLogIn"> Iniciar Sesión</a>
              </li>
              <li>
                <a v-if="!is_auth" v-on:click="loadSignUp"> Registrarse</a>
              </li>
              <li><a v-if="is_auth">Inicio</a></li>
              <li><a v-if="is_auth">Cuenta</a></li>
              <li><a v-if="is_auth">Cerrar sesion</a></li>
            </ul>
          </li>
          <li class="services">
            <a href="/">Tienda</a>
            <!-- DROPDOWN MENU -->
            <ul class="dropdown">
              <li><a href="/">Baño</a></li>
              <li><a href="/">Cocina</a></li>
              <li><a href="/">Decoración</a></li>
              <li><a href="/">Habitación</a></li>
              <li><a href="/">Sala</a></li>
            </ul>
          </li>
          <li><a href="/">Nosotros</a></li>
          <li><a href="/">Contactanos</a></li>
        </div>
      </ul>
    </nav>
  </div>
</template>

<!-- FALTA ROUTER Y SCRIPT -->

<script>

</script>


<style>
body {
  font-family: cursive;
}
a {
  text-decoration: none;
}
li {
  list-style: none;
}
/* NAVBAR STYLING STARTS */
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  background-color: #94b586;
  color: #fff;
}
.nav-links a {
  color: #fff;
}
/* LOGO */
.logo {
  font-size: 32px;
}
/* NAVBAR MENU */
.menu {
  display: flex;
  gap: 1em;
  font-size: 18px;
}
.menu li:hover {
  background-color: #94b586;
  border-radius: 5px;
  transition: 0.3s ease;
}
.menu li {
  padding: 5px 14px;
}
/* DROPDOWN MENU */
.services {
  position: relative;
}
.dropdown {
  background-color: #647a5b;
  padding: 1em 0;
  position: absolute; /*WITH RESPECT TO PARENT*/
  display: none;
  border-radius: 8px;
  top: 35px;
}
.dropdown li + li {
  margin-top: 10px;
}
.dropdown li {
  padding: 0.5em 1em;
  width: 8em;
  text-align: center;
}
.dropdown li:hover {
  background-color: #303b2b;
}
.services:hover .dropdown {
  display: block;
}

.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background: #fdfefe;
}
</style>
