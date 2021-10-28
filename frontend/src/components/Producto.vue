<template>
  <div class="menu2">
    <div class="box_producto">
      <div>
        <figure>
          <img v-bind:src="productos.image" />
        </figure>
        <div id="nombre">
          <h3>Nombre : {{ productos.nombre }}</h3>
        </div>
        <div id="especialidad">
          <h3>Categoria: {{ productos.categoria }}</h3>
        </div>
        <div id="calificacion">
          <h3>Fabricante : {{ productos.fabricante }}</h3>
        </div>
        <div id="calificacion">
          <h3>Marca : {{ productos.marca }}</h3>
        </div>
        <div id="calificacion">
          <h3>Precio : {{ productos.precio }}</h3>
        </div>
        <br>
        <a class="boton_personalizado" href="https://vinkula.com">Comprar</a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "producto",

  data: function () {
    return {
      productos: {},
      id_producto: "",
    };
  },
  methods: {
    async getProducto() {
      //const producto = this.$route.params.producto;
      this.id_producto = this.$route.params.id_producto;
      await axios
        .get(
          `https://comateriales-be.herokuapp.com/productos/${this.id_producto}/`
        )
        .then((result) => {
          this.productos = result.data[0];
          console.log(this.productos);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created: function () {
    this.getProducto();
  },
};
</script>
:
<style>
.menu2 {
  display: flex;
  flex-wrap: wrap;
  margin-left: 13%;
  align-content: center;
}

#nombre h3 {
  font: oblique bold 120% cursive;
  font-weight: normal;
  color: #443963;
}
#nombre {
  margin-bottom: 1px;
}

#especialidad h3 {
  font: oblique bold 120% cursive;
  font-weight: normal;
  color: #443963;
}

#especialidad {
  margin-bottom: 1px;
}

#calificacion h3 {
  font: oblique bold 120% cursive;
  font-weight: normal;
  color: #443963;
}
#calificacion {
  margin-bottom: 1px;
}

#router {
  font: oblique bold 120% cursive;
  font-weight: normal;
  padding: 40px 0px;
}
.router {
  text-decoration: none;
  color: #ffff;
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

.producto {
  display: flex;
  flex-wrap: wrap;
  margin-left: 10%;
  margin-right: 10%;
}
.box_producto {
  margin-top: 10px;
  margin-bottom: 2px;
  margin-left: 300px;
  background-color: white;
  width: 600px;
  height: 600px;
  overflow: hidden;
  border-radius: 30px;
  -webkit-border-radius: 30px;
  -moz-border-radius: 30px;
  -ms-border-radius: 30px;
  -o-border-radius: 30px;
  box-shadow: -10px 10px 20px rgb(116, 116, 116);
  background-size: cover;
  align-content: center;
}
.box_producto div {
  text-align: center;
  padding: 3px;
  align-content: center;
  justify-content: space-between;
}
.boton_personalizado {
  text-decoration: none;
  padding: 10px;
  font-weight: 600;
  font-size: 20px;
  color: #ffffff;
  background-color: #303b2b;
  border-radius: 6px;
}
</style>