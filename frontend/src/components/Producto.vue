<template>
  <div>
    <div>
      <figure class="image">
          <img v-bind:src="productos.image"  >
        </figure>
    </div>
    <h1>A mimir</h1>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "producto",

  data: function () {
    return {
      productos: {},
      id_producto:"",
    };
  },
  methods: {
    async getProducto() {
      //const producto = this.$route.params.producto;
      this.id_producto = this.$route.params.id_producto;
      await axios
        .get(`https://comateriales-be.herokuapp.com/productos/${this.id_producto}/`)
        .then((result) => {
          this.productos = result.data[0];
          console.log(this.productos);

        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
    created:  function() {
      this.getProducto() 
  }
};
</script>
:
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
  color: white;
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

.box img {
  border-radius: 30px;
  width: 3.8vw;
  height: 4vw;
  margin: 0.2vw 0 0 1.3vw;
  margin-left: auto;
  margin-right: auto;
  display: block;
}
</style>