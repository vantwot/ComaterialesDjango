<template>
  <div class="menu1">
    <div v-for="producto in productos" :key="producto.id" class="box1">
      <div>
        <figure class="image">
          <img src="../assets/logo.png" />
        </figure>
        <div id="nombre">
          <h3>Nombre : {{ producto.nombre }}</h3>
        </div>
        <div id="especialidad">
          <h3>fabricante: {{ producto.fabricante }}</h3>
        </div>
        <div id="calificacion">
          <h3>Precio : {{ producto.precio }}</h3>
        </div>
<<<<<<< HEAD
          <div id="router">
            <router-link class="router"  v-bind:to="producto.ruta_absoluta">View details
            </router-link>
        </div>
=======
        <!--<router-link class="router" v-bind:to="producto.ruta"
          >Ver detalles
        </router-link>-->
>>>>>>> 7aa28de52e45f2f8918244c2ff4dc0e16a9246d3
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "productos",

  data: function () {
    return {
      productos: [],
    };
  },
  methods: {
    getData: function () {
      axios
        .get("https://comateriales-be.herokuapp.com/productos/", {
          headers: {},
        })
        .then((result) => {
          this.productos = result.data;
        })
        .catch((error) => {
          alert("error al cargar la data");
        });
    },
  },

  created: function () {
    this.getData();
  },
};
</script>

<style>
.box img {
  border-radius: 30px;
  width: 3.8vw;
  height: 4vw;
  margin: 0.2vw 0 0 1.3vw;
  margin-left: auto;
  margin-right: auto;
  display: block;
}

.menu1 {
  display: flex;
  flex-wrap: wrap;
  margin-left: 13%;
}

.box1 {
  margin-left: 5vw;
  margin-top: 5vh;
  margin-bottom: 5vh;
  background-color: white;
  width: 17vw;
  overflow: hidden;
  border-radius: 30px;
  -webkit-border-radius: 30px;
  -moz-border-radius: 30px;
  -ms-border-radius: 30px;
  -o-border-radius: 30px;
  box-shadow: -10px 10px 20px rgb(116, 116, 116);
}

#nombre h3 {
  font: oblique bold 120% cursive;
  font-weight: normal;
  color: #443963;
}
#nombre {
  margin-top: -1vw;
  margin-bottom: -1vw;
}

#especialidad h3 {
  font: oblique bold 120% cursive;
  font-weight: normal;
  color: #443963;
}

#especialidad {
  margin-top: -1vw;
  margin-bottom: -1vw;
}

#calificacion h3 {
  font: oblique bold 120% cursive;
  font-weight: normal;
  color: #443963;
}
#calificacion {
  margin-top: -1vw;
  margin-bottom: -1vw;
}

.box div {
  text-align: center;
  padding: 15px 0;
  align-content: center;
  justify-content: space-between;
}

#router {
  font: oblique bold 120% cursive;
  font-weight: normal;
  padding: 40px 0px;
}
.router {
  text-decoration: none;
<<<<<<< HEAD
  color: rgb(153, 13, 13);
=======
  color: white;
>>>>>>> 7aa28de52e45f2f8918244c2ff4dc0e16a9246d3
  background-color: #283747;
  padding: 0 3%;
  border-radius: 5px;
  box-shadow: -1px 3px 10px rgb(116, 116, 116);
}
.router:hover {
  background-color: white;
  color: #283747;
  border-radius: 5px;
  text-align: center;
  padding: 0 3%;
}
</style>

