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
                <a v-if="!is_auth" v-on:click="loadHome"> Iniciar sesión</a>
              </li>
              <li>
                <a v-if="!is_auth" v-on:click="loadSignUp"> Registrarse</a>
              </li>
              <li><a v-if="is_auth" v-on:click="loadHome"> Inicio</a></li>
              <li><a v-if="is_auth" v-on:click="logOut"> Cerrar sesión</a></li>
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

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>
  </div>
</template>




<script>
export default {
  name: "App",

  data: function () {
    return {
      is_auth: false,
    };
  },

  components: {},

  methods: {
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;

      if (this.is_auth == false) this.$router.push({ name: "logIn" });
      else this.$router.push({ name: "home" });
    },

    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
    },

    loadSignUp: function () {
      this.$router.push({ name: "signUp" });
    },

    completedLogIn: function (data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },

    completedSignUp: function (data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);
    },

    loadHome: function () {
      this.$router.push({ name: "home" });
    },

    loadAccount: function () {
      this.$router.push({ name: "account" });
    },

    logOut: function () {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    },
  },

  created: function () {
    this.verifyAuth();
  },
};
</script>






<style>
body {
  margin: 0 0 0 0;
}

.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;

  background-color: #283747;
  color: #e5e7e9;

  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1 {
  width: 20%;
  text-align: center;
}

.header nav {
  height: 100%;
  width: 20%;

  display: flex;
  justify-content: space-around;
  align-items: center;

  font-size: 20px;
}

.header nav button {
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 20px;
}

.header nav button:hover {
  color: #283747;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}

.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;

  background: #fdfefe;
}
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
  position: absolute;
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
</style>
